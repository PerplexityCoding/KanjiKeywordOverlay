#-*- coding: utf-8 -*-
#
# Kanji Overlay Anki Plugin
#
# Comments & Suggestions at: fanatic84@gmail.com
#
# Use at your own Risk :)
#
# Insperated from the Work of Brian Bush on Anki v1 plugin, thank you very much
# Thanks for Roland Sieker <ospalh@gmail.com> and his plugin Local css for Anki 2
#

import os, pickle, datetime, codecs, shutil

from aqt import mw

from anki.hooks import addHook
from anki.utils import ids2str
from anki.cards import Card
import kol.KolConfig as KolConfig
from kol.AnkiHelper import *
from aqt.utils import showInfo

class KanjiOverlay:
    ################# CUSTOMIZE ###################
    # switch the next Variable to True, if you don't want to use the GUI to configure
    __useTheProfilesConfiguredInThisFile = False
    Profiles = {
        KolConfig.DEFAULTCONFIGNAME : #Profile by default
                    KolConfig.KolConfig(
                        ProfileName = KolConfig.DEFAULTCONFIGNAME,
                        KanjiUseCustomDeck = False,
                        KanjiDeckName = u'',
                        KanjiExpression = '',
                        KanjiKeyword = '',
                        KanjiDisplayWithFuriganaMod = True,
                        KanjiLoadDefaultValuesForNonExistingValues = False,
                        KanjiShowColorsForKnownKanji = True )
        ,"User 1" :  #Other Profile Name
                    KolConfig.KolConfig(
                        #ProfileName = 'User 1',
                        KanjiUseCustomDeck = True,
                        KanjiDeckName = u'dictdec2',
                        KanjiExpression = 'Front',
                        KanjiKeyword = 'Back',
                        KanjiDisplayWithFuriganaMod = True,
                        KanjiLoadDefaultValuesForNonExistingValues = False,
                        KanjiShowColorsForKnownKanji = True )

        }
        # Add other Profile name

    ################################################

    # usually data is only loaded, if modiefiet. if (True): always load data in the load-method
    __alwaysLoadNewDictData = True
    __DEBUG__ShowExceptions = False
    __CssClassOfNotReviewedKanji = " unknown"
    __CssClassOfUnknownKanji = 'kol-missing'

    Profile = None
    def load(self):

        log("Load Plugin")

        profileName = mw.pm.name

        pf = None
        if (self.__useTheProfilesConfiguredInThisFile):
            pf = self.Profiles
        else:
            pf = KolConfig.getKolConfigManager(self.getConfigFilePathName()).allProfiles

        self.Profile = pf[KolConfig.DEFAULTCONFIGNAME] if not profileName in pf else pf[profileName]

        if(not (self.Profile.KanjiShowColorsForKnownKanji)):
            self.__CssClassOfNotReviewedKanji = ""
            self.__CssClassOfUnknownKanji = ''

        self.__setupObjectData(self.Profile)
        self.__loadKanjiDict()
        self.__addCSS()
        self.__addHooks()

        log("End Load Plugin")

    def __addCSS(self):
        if not os.path.exists(self.cssFileInProfile):
            shutil.copy2(self.cssFileInPlugin, self.cssFileInProfile)

        KanjiOverlay.css = self.loadCss()
        KanjiOverlay.oldCss = Card.css
        Card.css = injectCss

    def __addHooks(self):
        addHook('fmod_kol', self.injectKanjiOverlay)
        if self.Profile.KanjiDisplayWithFuriganaMod:
            addHook('fmod_furigana', self.injectKanjiOverlay)
            addHook('fmod_kanji', self.injectKanjiOverlay)

    def __loadKanjiDict(self):

        # ------------ define an inner function for overall readiness -----------
        def __loadKanjiDB(loadCustomDB):
            kanjiDict = dict()
            if (loadCustomDB):
                if os.path.exists(self.kanjiCustomDictPath):
                    kanjiFile = open(self.kanjiCustomDictPath, "rb")
                    self.dlmod, self.nlmod, self.clmod, kanjiDict = pickle.load(kanjiFile)
                    deck = mw.col.decks.byName(self.Profile.KanjiDeckName)
                    if (AnkiHelper.isDeckModified(self.dlmod, self.nlmod, self.clmod, deck)
                        or self.__alwaysLoadNewDictData ):
                            kanjiDict = self.loadFromCustomDeck()
                else:
                    kanjiDict = self.loadFromCustomDeck()
                pass
            else:
                if os.path.exists(self.kanjiDefaultDictPath) == False:
                    raise Exception('Missing Default Dict')
                kanjiFile = open(self.kanjiDefaultDictPath, "rb")
                self.dlmod, self.nlmod, self.clmod, kanjiDict = pickle.load(kanjiFile)
                pass
            return kanjiDict

        # --------------- the actual function starts here -------------
        self.kanjiDict = dict()
        if(self.Profile.KanjiLoadDefaultValuesForNonExistingValues):
            # first load the default DB, so the Values from the custom DB
            #  overwrite/update the default values
            self.kanjiDict = __loadKanjiDB(False)

        try:
            tmpDict = __loadKanjiDB(self.Profile.KanjiUseCustomDeck)
        except Exception as e:
            showInfo('Kanji Overlay Error: User defined Database could not be loaded.' +
                     ' please check your settings. \nusing default Database instead')
            tmpDict = __loadKanjiDB(False)
            if(self.__DEBUG__ShowExceptions):
                raise(e)

        self.kanjiDict.update(tmpDict)


    def __setupObjectData(self, profileVar):
        self.kanjiCustomDictPath    = os.path.join(mw.pm.profileFolder(), 'custom-kol.db')
        self.kanjiDefaultDictPath   = os.path.join(mw.pm.addonFolder(), 'kol', 'english-kol.db')
        self.cssFileInPlugin        = os.path.join(mw.pm.addonFolder(), 'kol', 'default-kol.css')
        self.cssFileInProfile       = os.path.join(mw.pm.profileFolder(), 'custom-kol.css')

        self.kanjiDict = None

    def reload(self):
        self.unload()
        oldValue = self.__alwaysLoadNewDictData
        self.__alwaysLoadNewDictData = True
        self.load()
        # restore old value
        self.__alwaysLoadNewDictData = oldValue

    def getConfigFilePathName(self):
        return os.path.join(mw.pm.addonFolder(), 'kol', KolConfig.CONFIGFILENAME)

    def loadCss(self):
        try:
            f = open(self.cssFileInProfile, 'r')
            css = unicode(f.read(), 'utf-8')
            f.close()
        except:
            css = u''
        return css

    def unload(self):
        Card.css = KanjiOverlay.oldCss

    def injectKanjiOverlay(self, txt, *args):
        #TODO: seems to crash Anki when using the browser :/
        #if self.KanjiUseCustomDeck and os.path.exists(self.kanjiCustomDictPath): # reload if deck modified,
        #    deck = mw.col.decks.byName(self.KanjiDeckName)
        #    log("test deck modified")
        #    if AnkiHelper.isDeckModified(self.dlmod, self.nlmod, self.clmod, deck): # seems to crash Anki when search
        #        self.kanjiDict = self.loadFromCustomDeck()
        def remap():
            for c in txt:
                if c >= u'\u4E00' and c <= u'\u9FBF': #Kanji
                    if c in self.kanjiDict:
                        kw, ivl = self.kanjiDict.get(c)
                        unkown = self.__CssClassOfNotReviewedKanji if ivl <= 0 and self.Profile.KanjiUseCustomDeck else ""
                        yield '<span class="kol%s">%s<span>%s</span></span>' % (unkown, c, kw)
                    else: yield '<span class="' + self.__CssClassOfUnknownKanji + '">%s</span>' % (c)
                else: yield c

        return ''.join([x for x in remap()])

    def loadFromCustomDeck(self):
        log("loadFromCustomDeck")
        deck = mw.col.decks.byName(self.Profile.KanjiDeckName)
        cards = AnkiHelper.getCards(deck["id"])
        kanjiDict = dict()
        for card in cards:
            note = card.note
            try:
                kanjiDict[note[self.Profile.KanjiExpression]] = (note[self.Profile.KanjiKeyword], card.ivl)

            except: continue

        self.dlmod = deck["mod"]
        self.nlmod, self.clmod = AnkiHelper.getLastModified(deck["id"])

        kanjiFile = open(self.kanjiCustomDictPath, "wb")
        pickle.dump((self.dlmod, self.nlmod, self.clmod, kanjiDict), kanjiFile, 2)

        return kanjiDict

def injectCss(self):
    return '<style>%s</style>' % KanjiOverlay.css + KanjiOverlay.oldCss(self)

def log(msg):
    logPath = os.path.join(mw.pm.addonFolder(), 'kol', 'main.log')
    txt = '%s: %s' % (datetime.datetime.now(), msg)
    f = codecs.open(logPath, 'a', 'utf-8')
    f.write(txt + '\n')
    f.close()

# ------------------------------------------------------------------------------
# -----------------------   For Menu in Anki -----------------------------------
# ------------------------------------------------------------------------------

def callConfigDialog():
    AnkiConnection = KolConfig.ankiConnection(mw)
    #for testing:
    #AnkiConnection = KolConfig.ankiConnectionMOCK()
    KolConfig.startUi(AnkiConnection, kanji.getConfigFilePathName(),mw)

    kanji.reload()

    pass

def reloadKol():
    kanji.reload()

def addToMenuBar():
    # The menu goes to
    # Tools -> Add-Ons -> KanjiOverlay
    for child in mw.form.menuPlugins.children():
        try:
            if(child.title() == 'KanjiOverlay'):
                child.addAction(actionKolConfigDlg)
                child.addAction(actionReloadKol)
                return True

        except:
            continue
    # in case - for whatever reason - there is no Point 'KanjiOverlay'
    mw.form.menuPlugins.addAction(actionKolConfigDlg)
    mw.form.menuPlugins.addAction(actionReloadKol)

from aqt.qt import *
actionKolConfigDlg = QAction("Kol Config Dialog", mw)
mw.connect(actionKolConfigDlg, SIGNAL("triggered()"), callConfigDialog)
actionReloadKol = QAction("Reload (in case of changes)", mw)
mw.connect(actionReloadKol, SIGNAL("triggered()"), reloadKol)
# If you want to call the config dialog directly from the Add-Ons-Menu, then enable this one
#mw.form.menuPlugins.addAction(action)


# ------------------------------------------------------------------------------
# -------------------------   hooks  -------------------------------------------
# ------------------------------------------------------------------------------

kanji = KanjiOverlay()
addHook("profileLoaded", addToMenuBar)
addHook("profileLoaded", kanji.load)
addHook("unloadProfile", kanji.unload)


