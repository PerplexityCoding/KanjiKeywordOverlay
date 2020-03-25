# -------------------------------------------------------------------------------
# -----------------------------   Dialog    -------------------------------------
# -------------------------------------------------------------------------------
import sys
from aqt.qt import QDialog, QApplication, QComboBox

from .utils import log
from . import KolConfigGui
from .AnkiHelper import AnkiHelper
from .KolConfigsManager import KolConfigsManager

class KolConfigDlg(QDialog):
    __gui = None
    __firstTimeShow = True
    __PreviousChosenProfileIndex = -1
    __ankiConnection = None

    def __init__(self, gui, ankiConnection, parent=None):
        super(self.__class__, self).__init__(parent)
        self.__gui = gui
        self.__ankiConnection = ankiConnection

    def showEvent(self, event):
        # print("DEBUG: showEvent")
        QDialog.showEvent(self, event)
        if (self.__firstTimeShow):
            self.onLoad()

    def closeEvent(self, event):
        # print("DEBUG: closeEvent")
        self._updateConfigFromGui()
        self.__saveConfigsToFs()
        QDialog.closeEvent(self, event)

    def onLoad(self):
        # print("DEBUG: onLoad")
        # log("on load")
        if not self.__firstTimeShow:
            return
        self.__firstTimeShow = False

        # we don't want to be disturbed by GUI-Events during the load
        #   (they will appear as we fill the checkbox)
        # self.__guiUpdatingInProcess = True

        self.__kolConfigsManager = KolConfigsManager.getInstance()

        # fill ComboBoxes
        currentSelectedProfile = self.__fillCboProfileFromAnki(self.__ankiConnection)        

        # now (at the end) we can load the current
        self.__updateGuiFromConfig(currentSelectedProfile)
        self.__addEventListeners()

    def __addEventListeners(self):
        gui = self.__gui
        gui.cboCustomDeckName.currentIndexChanged.connect(self.__fillDeckRelatedCbos)

    def __saveConfigsToFs(self):
        # print("DEBUG: safeConfigsToFs")
        self.__kolConfigsManager.save()

    def __fillCboProfileFromAnki(self, anki):
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
        if (currentProfile < 0):
            currentProfile = 0
        self.__gui.cboProfiles.setCurrentIndex(currentProfile)
        # we MUST set this index here as initial data
        self.__PreviousChosenProfileIndex = currentProfile

        # str will fail, if the profile is unicoded (damn python non-unicode-support!)
        #   short workarround: just return the QString. Is works fine with the rest code
        tmp1 = self.__gui.cboProfiles.currentText()
        tmp2 = tmp1  # str(tmp1)

        return tmp2

    def __fillDeckNameCbo(self, anki, profilename):
        # print("DEBUG: fillProfileDependedCbos")
        gui = self.__gui

        # clear
        gui.cboCustomDeckName.clear()
        gui.cboCustomDeckName.addItems(anki.getDeckNames(profilename))

    def __fillDeckRelatedCbos(self):
        log("selects");
        anki = self.__ankiConnection
        gui = self.__gui

        deckName = gui.cboCustomDeckName.currentText()
        log(deckName)
        fieldNames = anki.getFieldnames(deckName)
        log(fieldNames)

        gui.cboCustomExpression.clear()
        gui.cboCustomExpression.addItems(fieldNames)

        gui.cboCustomKeyword.clear()
        gui.cboCustomKeyword.addItems(fieldNames)

        gui.cboOnYomi.clear()
        gui.cboOnYomi.addItems(fieldNames)

        gui.cboKunYomi.clear()
        gui.cboKunYomi.addItems(fieldNames)

        gui.cboMemoStory.clear()
        gui.cboMemoStory.addItems(fieldNames)

    def __updateGuiFromConfig(self, ProfileName):
        print("DEBUG: updateGuiFromConfig")
        gui = self.__gui

        curProf = self.__kolConfigsManager.getProfileByName(ProfileName)

        if (curProf != None):
            self.__fillDeckNameCbo(self.__ankiConnection, curProf)           
            gui.cboCustomDeckName.setEditText(curProf.kanjiDeckName)
            
            self.__fillDeckRelatedCbos()
            
            # set all the other variables
            gui.cboCustomExpression.setEditText(curProf.kanjiExpression)
            gui.cboCustomKeyword.setEditText(curProf.kanjiKeyword)
            gui.cboOnYomi.setEditText(curProf.kanjiOnYomi)
            gui.cboKunYomi.setEditText(curProf.kanjiKunYomi)
            gui.cboMemoStory.setEditText(curProf.kanjiMemoStory)

            gui.chkUseCustomDeck.setChecked(curProf.kanjiCustomProfileEnabled)
            gui.chkAlsoLoadDefaultDB.setChecked(curProf.kanjiLoadDefaultValuesForNonExistingValues)
            gui.chkColorizeKanjis.setChecked(curProf.kanjiShowColorsForKnownKanji)
            gui.chkKanjiLink.setChecked(curProf.kanjiUseLink)
            gui.chkOnYomi.setChecked(curProf.kanjiOnYomiEnabled)
            gui.chkKunYomi.setChecked(curProf.kanjiKunYomiEnabled)
            gui.chkMemoStory.setChecked(curProf.kanjiMemoStoryEnabled)

            gui.editKanjiLink.setText(curProf.kanjiUseLinkUrl)
            gui.editKanjiLink.setEnabled(gui.chkKanjiLink.isChecked())

            gui.gpbKanjiData.setEnabled(gui.chkUseCustomDeck.isChecked())
            gui.gpbAdvanced.setEnabled(gui.chkUseCustomDeck.isChecked())

            gui.cboOnYomi.setEnabled(gui.chkOnYomi.isChecked())
            gui.cboKunYomi.setEnabled(gui.chkKunYomi.isChecked())
            gui.cboMemoStory.setEnabled(gui.chkMemoStory.isChecked())

        else:
            print("current profile could not be found")

    def _updateConfigFromGui(self, bProfilesChanged=False):
        # print("DEBUG: updateConfigFromGui")
        """bProfileChanged: if the Profile was changed, the previous chosen profile is used"""
        gui = self.__gui

        # find the profile
        curProf = None
        if bProfilesChanged:
            curProf = self.__kolConfigsManager.getProfileByName(
                gui.cboProfiles.itemText(self.__PreviousChosenProfileIndex))
        else:
            curProf = self.__kolConfigsManager.getProfileByName(
                gui.cboProfiles.currentText())

        # set the values to profile
        if (curProf != None):
            curProf.kanjiDeckName = gui.cboCustomDeckName.currentText()
            curProf.kanjiExpression = gui.cboCustomExpression.currentText()
            curProf.kanjiKeyword = gui.cboCustomKeyword.currentText()
            curProf.kanjiOnYomi = gui.cboOnYomi.currentText()
            curProf.kanjiKunYomi = gui.cboKunYomi.currentText()
            curProf.kanjiMemoStory = gui.cboMemoStory.currentText()

            curProf.kanjiCustomProfileEnabled = gui.chkUseCustomDeck.isChecked()
            curProf.kanjiLoadDefaultValuesForNonExistingValues = gui.chkAlsoLoadDefaultDB.isChecked()
            curProf.kanjiShowColorsForKnownKanji = gui.chkColorizeKanjis.isChecked()
            curProf.kanjiUseLink = gui.chkKanjiLink.isChecked()
            curProf.kanjiOnYomiEnabled = gui.chkOnYomi.isChecked()
            curProf.kanjiKunYomiEnabled = gui.chkKunYomi.isChecked()
            curProf.kanjiMemoStoryEnabled = gui.chkMemoStory.isChecked()

            curProf.kanjiUseLinkUrl = gui.editKanjiLink.text()
            # print("DEBUG: update from gui ok - updated profile: " + curProf.ProfileName)
            return True
        else:
            return False

    # -------------------------------------------------------------------------------
    # -------------------------  Handlers  ------------------------------------------
    # -------------------------------------------------------------------------------

    def chkKanjiLinkHandler(self):
        self.__gui.editKanjiLink.setEnabled(self.__gui.chkKanjiLink.isChecked())

    def chkOnYomiHandler(self):
        self.__gui.cboOnYomi.setEnabled(self.__gui.chkOnYomi.isChecked())

    def chkKunYomiHandler(self):
        self.__gui.cboKunYomi.setEnabled(self.__gui.chkKunYomi.isChecked())

    def chkMemoStoryHandler(self):
        self.__gui.cboMemoStory.setEnabled(self.__gui.chkMemoStory.isChecked())

    def chkUserCustomDeckHandler(self):
        gui = self.__gui
        gui.gpbKanjiData.setEnabled(gui.chkUseCustomDeck.isChecked())
        gui.gpbAdvanced.setEnabled(gui.chkUseCustomDeck.isChecked())

    def anotherProfileChosen(self, strCurrentText):
        # first we need to save the last input
        self._updateConfigFromGui(True)
        # then we can load the new profile
        self.__updateGuiFromConfig(strCurrentText)
        self.__PreviousChosenProfileIndex = self.__gui.cboProfiles.currentIndex()

    def closeDlg(self):
        self.close()

# -------------------------------------------------------------------------------
# -------------------------  Anki-connection  -----------------------------------
# -------------------------------------------------------------------------------

class AnkiConnection:
    """class calls methods in anki. It's encapsulated to keep the whole dialog independend"""
    __mw = None

    def __init__(self, xmw):
        self.__mw = xmw

    def getProfileNames(self):
        return self.__mw.pm.profiles()

    def getCurrentProfileName(self):
        return self.__mw.pm.name

    def getDeckNames(self, profilename):
        deckNames = self.__mw.col.decks.allNames()
        return deckNames

    def getFieldnames(self, deckName):
        did = self.__mw.col.decks.id(deckName, False)
        notes = AnkiHelper.getNotes(did)

        allFieldNames = []
        for note in notes:
            for fieldName in note.keys():
                if fieldName not in allFieldNames:
                    allFieldNames.append(fieldName)

        return allFieldNames

    def getAllFieldnames(self):
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

class AnkiConnectionMOCK():
    """can be used for testing, or if the dialog is not called from anki"""

    def __init__(self):
        # just overwrite the parents method
        pass

    def getProfileNames(self):
        return ["prof1", "testprof2"]

    def getDeckNames(self, profilename):
        if (profilename == "prof1"):
            return ["deck1", "deck2"]
        else:
            return ["test deck name1", "test deck name2"]

    def getAllFieldnames(self, profilename):
        if (profilename == "prof1"):
            return ["field1", "field2"]
        else:
            return ["test field name1", "test field name2"]

    def getCurrentProfileName(self):
        return "testprof2"

# -------------------------------------------------------------------------------
# -----------------------------   main     -------------------------------------
# -------------------------------------------------------------------------------

# starting GUI from Anki
def startUi(parentWindow=None):
    """
    @param ankiConnection: type = ankiConnection
    @param configFilename: type = string
    @param parentWindow: type = QDialog
    """
    ui = KolConfigGui.Ui_Dialog()
    window = KolConfigDlg(ui, AnkiConnection(parentWindow), parentWindow)

    ui.setupUi(window)

    window.exec_()


# starting GUI independend
def main():
    app = QApplication(sys.argv)
    ui = KolConfigGui.Ui_Dialog()
    window = KolConfigDlg(ui, AnkiConnectionMOCK())

    ui.setupUi(window)
    window.show()

    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
