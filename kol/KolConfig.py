from PyQt4.QtGui import QApplication, QDialog
import KolConfigGui
import sys
import pickle

CONFIGFILENAME = 'KolConfig.profiles'
DEFAULTCONFIGNAME = 'DEFAULT'

#-------------------------------------------------------------------------------
#-----------------------------   Profile  -------------------------------------
#-------------------------------------------------------------------------------

class KolConfig:

    def __init__(self,
        ProfileName       = '',
        KanjiDeckName     = '',
        KanjiExpression   = '',
        KanjiKeyword      = '',
        KanjiUseCustomDeck                         = False,
        KanjiDisplayWithFuriganaMod                = True,
        KanjiLoadDefaultValuesForNonExistingValues = False,
        KanjiShowColorsForKnownKanji               = True,
        KanjiUseLink                               = False,
        KanjiUseLinkUrl                            = ''):
            self.ProfileName             = ProfileName
            self.KanjiUseCustomDeck      = KanjiUseCustomDeck
            self.KanjiDeckName           = KanjiDeckName
            self.KanjiExpression         = KanjiExpression
            self.KanjiKeyword            = KanjiKeyword
            self.KanjiDisplayWithFuriganaMod                = KanjiDisplayWithFuriganaMod
            self.KanjiLoadDefaultValuesForNonExistingValues = KanjiLoadDefaultValuesForNonExistingValues
            self.KanjiShowColorsForKnownKanji               = KanjiShowColorsForKnownKanji
            self.KanjiUseLink                               = KanjiUseLink
            self.KanjiUseLinkUrl                            = KanjiUseLinkUrl

#-------------------------------------------------------------------------------
#-----------------------------   globals  -------------------------------------
#-------------------------------------------------------------------------------
def loadConfigsFromFs(configFilename):
    #print("DEBUG: loadConfigsFromFs")
    KolConfigFromFs = pickle.load(open( configFilename, "rb" ))
    # basically for saving time finding bugs, as pickler doesn't inform about anything:
    if (KolConfigFromFs.VERSION != KolConfigsManager().VERSION):
        print('Error: wrong Version in stored file')
        raise(Exception('wrong Version in stored file. All old profiles will be deleted'))
    return KolConfigFromFs

def getKolConfigManager(configFilename):
    """@return: KolConfigManager. NEVER! None"""
    print("DEBUG: getKolConfigManager")
    ret = None
    try:
        ret = loadConfigsFromFs(configFilename)
    except:
        # there is no profile, or there was an error loading, we just create a new one
        print('Warning: no config Profile on HDD. Creating new one')
        ret = KolConfigsManager()
        pass
    # we always want one 'DEFAULT' entry
    ret.addNewProfile(DEFAULTCONFIGNAME)

    assert(ret!=None)
    return ret

#-------------------------------------------------------------------------------
#-------------------------  Anki-connection  ----------------------------------
#-------------------------------------------------------------------------------
class ankiConnection:
    """class calls methods in anki. It's encapsulated to keep the whole dialog independend"""
    __mw = None

    def __init__(self, xmw):
        self.__mw = xmw
        pass

    def getProfileNames(self):
        return self.__mw.pm.profiles()
        pass

    def getCurrentProfileName(self):
        return self.__mw.pm.name
        pass

    def getDeckNames(self, profilename):
        deckNames = self.__mw.col.decks.allNames()
        return deckNames
        pass
    def getAllFieldnames(self, profilename):
        # Models = cardlayout (what and how many fields on a card)
        allFieldNamesFromAllModels = []

        allModels = self.__mw.col.models.allNames()
        # create a flat array with all fields
        for modelName in self.__mw.col.models.allNames():
            # dunno how to acces the name from object and no time for finding out,
            #   so we get the model by name
            model = self.__mw.col.models.byName(modelName)
            fieldNames = self.__mw.col.models.fieldNames(model)
            for fieldName in fieldNames:
                allFieldNamesFromAllModels.append(fieldName)
            pass

        return allFieldNamesFromAllModels
        pass

class ankiConnectionMOCK(ankiConnection):
    """can be used for testing, or if the dialog is not called from anki"""
    def __init__(self):
        # just overwrite the parents method
        pass

    def getProfileNames(self):
        return ['prof1','testprof2']
    def getDeckNames(self, profilename):
        if (profilename == 'prof1'):
            return ['deck1','deck2']
        else:
            return ['test deck name1','test deck name2']
    def getAllFieldnames(self, profilename):
        if (profilename == 'prof1'):
            return ['field1','field2']
        else:
            return ['test field name1','test field name2']
    def getCurrentProfileName(self):
        return 'testprof2'
        pass
#-------------------------------------------------------------------------------
#-------------------------   Profile Manager  ----------------------------------
#-------------------------------------------------------------------------------

class KolConfigsManager:
    allProfiles = dict()
    VERSION = 3 # change Version in init-method

    def __init__(self):
        self.VERSION = 4
        self.allProfiles = dict()

    def getProfileByName(self, profileName):
        """
        @param: profileName: type = string
        @return: Always a profile! None will NEVER be returned
        """
        ret = None
        if(profileName in self.allProfiles):
            ret = self.allProfiles[profileName]
            self.migrateProfile(ret)
        else:
            ret = self.addNewProfile(profileName)

        return ret
        pass

    def migrateProfile(self, profile):
        if hasattr(profile, 'KanjiUseLink') == False:
            profile.KanjiUseLink = False
        if hasattr(profile, 'KanjiUseLinkUrl') == False:
            profile.KanjiUseLinkUrl = ''

    def getAllProfileNames(self):
        ret = self.allProfiles.keys()
        return ret

    def addNewProfile(self, profilename):
        """ creates a new empty profile"""
        newProfile = KolConfig(ProfileName=profilename)
        self.allProfiles.update({profilename : newProfile})
        #self.allProfiles[profilename] = newProfile
        return newProfile

#-------------------------------------------------------------------------------
#-----------------------------   Dialog    -------------------------------------
#-------------------------------------------------------------------------------

class KolConfigDlg(QDialog):
    __gui = None
    __firstTimeShow = True
    __kolConfigs = None
    __guiUpdatingInProcess = False
    __STRFORNEWPROFILE = '<<add>>'
    __PreviousChosenProfileIndex = -1
    __ankiConnection = None
    __configFilename = ''

    def __init__(self, gui, ankiConnection, configFilename ,parent=None):
        super(self.__class__, self).__init__(parent)
        self.__gui = gui
        self.__kolConfigs = KolConfigsManager()
        self.__ankiConnection = ankiConnection
        self.__configFilename = configFilename

    def closeEvent(self, event):
        #print("DEBUG: closeEvent")
        self.updateConfigFromGui()
        self.safeConfigsToFs()
        QDialog.closeEvent(self, event)

    def safeConfigsToFs(self):
        #print("DEBUG: safeConfigsToFs")
        pickle.dump( self.__kolConfigs , open(self.__configFilename, 'wb'))
        pass

    def showEvent(self, event):
        #print("DEBUG: showEvent")
        QDialog.showEvent(self,event)
        if(self.__firstTimeShow):
            self.onLoad()

    def onLoad(self):
        #print("DEBUG: onLoad")

        # we don't want to be disturbed by GUI-Events during the load
        #   (they will appear as we fill the checkbox)
        #self.__guiUpdatingInProcess = True

        self.__kolConfigs = getKolConfigManager(self.__configFilename)
        self.__firstTimeShow = False
        # fill ComboBoxes
        currentSelectedProfile = self.fillCboProfileFromAnki(self.__ankiConnection)
        self.fillProfileDependendCbos(self.__ankiConnection,currentSelectedProfile)

        self.__guiUpdatingInProcess = False

        # now (at the end) we can load the current
        self.updateGuiFromConfig(currentSelectedProfile)

    def fillCboProfileFromAnki(self,anki):
        """fill the combo-boxes on the GUI with the lists got from Anki
        @return: current chosen Profile
        @param anki: type = ankiConnection"""
        print("fillCboProfileFromAnki")

        # first fill the profile:
        # (because the next data is based on the current profile chosen)
        # ------------------------
        self.__gui.cboProfiles.clear()
        self.__gui.cboProfiles.addItems(anki.getProfileNames())

        # ------select initial item------
        currentProfile = self.__gui.cboProfiles.findText(anki.getCurrentProfileName())
        if(currentProfile < 0):
            currentProfile = 0
        self.__gui.cboProfiles.setCurrentIndex(currentProfile)
        # we MUST set this index here as initial data
        self.__PreviousChosenProfileIndex = currentProfile

        # str will fail, if the profile is unicoded (damn python non-unicode-support!)
        #   short workarround: just return the QString. Is works fine with the rest code
        tmp1 = self.__gui.cboProfiles.currentText()
        tmp2 = tmp1 #str(tmp1)

        return tmp2

    def fillProfileDependendCbos(self, anki, profilename):
            #print("DEBUG: fillProfileDependedCbos")
            gui = self.__gui

        # clear
            gui.cboCustomDeckName.   clear()
            gui.cboCustomExpression. clear()
            gui.cboCustomKeyword.    clear()
        # fill
            gui.cboCustomDeckName    .addItems(anki.getDeckNames(profilename))
            gui.cboCustomExpression  .addItems(anki.getAllFieldnames(profilename))
            gui.cboCustomKeyword     .addItems(anki.getAllFieldnames(profilename))

    def updateGuiFromConfig(self, ProfileName):
        print("DEBUG: updateGuiFromConfig")
        gui = self.__gui


        curProf = self.__kolConfigs.getProfileByName(ProfileName)

        gui.chkKanjiLink.stateChanged.connect(self.kanjiLinkCbkChanged)
        self.kanjiLinkCbkChanged(0)

        if(curProf != None):
            self.fillProfileDependendCbos(self.__ankiConnection,ProfileName)

            # set all the other variables
            gui.cboCustomDeckName.           setEditText(curProf.KanjiDeckName)
            gui.cboCustomExpression.         setEditText(curProf.KanjiExpression)
            gui.cboCustomKeyword.            setEditText(curProf.KanjiKeyword)


            gui.chkUseCustomDeck            .setChecked(curProf.KanjiUseCustomDeck)
            gui.chkDisplayWithFuriganaMod   .setChecked(curProf.KanjiDisplayWithFuriganaMod)
            gui.chkAlsoLoadDefaultDB        .setChecked(curProf.KanjiLoadDefaultValuesForNonExistingValues)
            gui.chkColorizeKanjis           .setChecked(curProf.KanjiShowColorsForKnownKanji)
            gui.chkKanjiLink                .setChecked(curProf.KanjiUseLink)
            gui.editKanjiLink               .setText(curProf.KanjiUseLinkUrl)
        else:
            print('current profile could not be found')
            pass

        #print('DEBUG: ' + str(self.__kolConfigs.getAllProfileNames()))

    def kanjiLinkCbkChanged(self, int):
        self.__gui.editKanjiLink.setEnabled(self.__gui.chkKanjiLink.isChecked())

    def updateConfigFromGui(self, bProfilesChanged = False):
        #print("DEBUG: updateConfigFromGui")
        """bProfileChanged: if the Profile was changed, the previous chosen profile is used"""
        gui = self.__gui

        # find the profile
        curProf = None
        if bProfilesChanged:
            curProf = self.__kolConfigs.getProfileByName(
                gui.cboProfiles.itemText(self.__PreviousChosenProfileIndex))
        else:
            curProf = self.__kolConfigs.getProfileByName(
                gui.cboProfiles.currentText())

        # set the values to profile
        if(curProf != None):
            curProf.KanjiDeckName     = gui.cboCustomDeckName.  currentText()
            curProf.KanjiExpression   = gui.cboCustomExpression.currentText()
            curProf.KanjiKeyword      = gui.cboCustomKeyword.   currentText()

            curProf.KanjiUseCustomDeck          = gui.chkUseCustomDeck.isChecked()
            curProf.KanjiDisplayWithFuriganaMod = gui.chkDisplayWithFuriganaMod.isChecked()
            curProf.KanjiLoadDefaultValuesForNonExistingValues = gui.chkAlsoLoadDefaultDB.isChecked()
            curProf.KanjiShowColorsForKnownKanji    = gui.chkColorizeKanjis.isChecked()
            curProf.KanjiUseLink = gui.chkKanjiLink.isChecked()
            curProf.KanjiUseLinkUrl = gui.editKanjiLink.text()
            #print('DEBUG: update from gui ok - updated profile: ' + curProf.ProfileName)
            return True
        else:
            return False

        pass

    def anotherProfileChosen(self, strCurrentText):
        # we need the 'if' to prevent infinite loops
        if(not self.__guiUpdatingInProcess):
            print("DEBUG: anotherProfileChosen")
            # first we need to save the last input
            self.updateConfigFromGui(True)
            # then we can load the new profile
            self.updateGuiFromConfig(strCurrentText)
            self.__PreviousChosenProfileIndex = self.__gui.cboProfiles.currentIndex()
        pass

    def closeDlg(self):
        self.close()
        pass


#-------------------------------------------------------------------------------
#-----------------------------   main     -------------------------------------
#-------------------------------------------------------------------------------

# starting GUI from Anki
def startUi(ankiConnection, configFilename, parentWindow = None):
    """
    @param ankiConnection: type = ankiConnection
    @param configFilename: type = string
    @param parentWindow: type = QDialog
    """
    ui = KolConfigGui.Ui_Dialog()
    window = KolConfigDlg(ui, ankiConnection, configFilename, parentWindow)

    ui.setupUi(window)

    window.exec_()

# starting GUI independend
def main():
    app = QApplication(sys.argv)
    ui = KolConfigGui.Ui_Dialog()
    window = KolConfigDlg(ui,ankiConnectionMOCK(),CONFIGFILENAME)

    ui.setupUi(window)
    window.show()

    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
