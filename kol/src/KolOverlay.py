import os
import pickle

from anki.cards import Card
from anki.hooks import addHook
from anki.template.template import Template
from aqt import mw
from aqt.utils import showInfo

from kol.src import KolConfigDialog
from kol.src.AnkiHelper import AnkiHelper
from kol.src.KolConfigsManager import KolConfig, KolConfigsManager
from kol.src.utils import log, readFile


class KanjiOverlay:
    DEFAULT_PROFILE = KolConfig()

    # usually data is only loaded, if modiefiet. if (True): always load data in the load-method
    __alwaysLoadNewDictData = False
    __DEBUG__ShowExceptions = False
    __saveCustomDict = False
    __CssClassOfNotReviewedKanji = "kol-unknown"
    __CssClassOfUnknownKanji = "kol-missing"

    profile = None

    @staticmethod
    def injectCss(card):
        return "<style>%s</style>" % KanjiOverlay.css + KanjiOverlay.oldCss(card)

    def load(self):
        log("Load Plugin")

        self.__defaultKanjiDict = None
        self.__kolConfigsManager = KolConfigsManager.getInstance()

        self.__loadProfile()

        self.__setupObjectData()
        self.__loadKanjiDict()
        self.__loadCss()
        self.__loadScripts()
        self.__loadTemplate()
        self.__addHooks()

        log("End Load Plugin")

    def unload(self):
        pass

    def reload(self):
        #self.unload()
        #oldValue = self.__alwaysLoadNewDictData
        #self.__alwaysLoadNewDictData = True
        #self.load()
        # restore old value
        #self.__alwaysLoadNewDictData = oldValue
        log("reload start")
        self.__loadProfile()
        self.__loadKanjiDict()
        log("reload stop")

    def __loadProfile(self):
        profileName = mw.pm.name
        self.profile = self.__kolConfigsManager.getProfileByName(profileName)

        if not self.profile.kanjiCustomProfileEnabled:
            self.profile = KanjiOverlay.DEFAULT_PROFILE

        if (not (self.profile.kanjiShowColorsForKnownKanji)):
            self.__CssClassOfNotReviewedKanji = ""
            self.__CssClassOfUnknownKanji = ""

    def openConfigDialog(self):
        # for testing:
        # AnkiConnection = KolConfig.ankiConnectionMOCK()
        KolConfigDialog.startUi(mw)

        self.reload()

    def __setupObjectData(self):
        self.kanjiDefaultDictPath = os.path.join(mw.pm.addonFolder(), "kol", "data", "english.db")
        self.kanjiCustomDictPath = os.path.join(mw.pm.profileFolder(), "kol", "user_files", "custom-kol.db")

        self.cssFileInPlugin = os.path.join(mw.pm.addonFolder(), "kol", "data", "styles.css")
        self.cssFileUserFiles = os.path.join(mw.pm.addonFolder(), "kol", "user_files", "styles.css")

        self.scriptsFileInPlugin = os.path.join(mw.pm.addonFolder(), "kol", "data", "scripts.js")
        self.scriptsFileUserFiles = os.path.join(mw.pm.addonFolder(), "kol", "user_files", "scripts.js")

        self.templateInPlugin = os.path.join(mw.pm.addonFolder(), "kol", "data", "template.hbs")
        self.templateUserFiles = os.path.join(mw.pm.addonFolder(), "kol", "user_files", "template.hbs")

    def __loadKanjiDict(self):
        self.kanjiDict = dict()
        if self.profile.kanjiLoadDefaultValuesForNonExistingValues:
            # first load the default DB, so the Values from the custom DB
            #  overwrite/update the default values
            self.kanjiDict = self.__loadDefaultKanjiDB()

        if self.profile.kanjiCustomProfileEnabled:
            try:
                customKanjiDict = self.__createCustomDeck()
                self.kanjiDict.update(customKanjiDict)
            except Exception as e:
                showInfo("Kanji Overlay Error: User defined Database could not be loaded." +
                         " please check your settings. \nusing default Database instead")

                self.kanjiDict = self.__loadDefaultKanjiDB()
                if (self.__DEBUG__ShowExceptions):
                    raise (e)

                return
        else:
            self.kanjiDict = self.__loadDefaultKanjiDB()

    # def __loadCustomKanjiDB(self):
    #     if os.path.exists(self.kanjiCustomDictPath):
    #         kanjiFile = open(self.kanjiCustomDictPath, "rb")
    #         self.dlmod, self.nlmod, self.clmod, kanjiDict = pickle.load(kanjiFile)
    #         deck = mw.col.decks.byName(self.profile.kanjiDeckName)
    #         if (AnkiHelper.isDeckModified(self.dlmod, self.nlmod, self.clmod, deck)
    #             or self.__alwaysLoadNewDictData):
    #             kanjiDict = self.__createCustomDeck()
    #     else:
    #          kanjiDict = self.__createCustomDeck()
    #
    #     return kanjiDict

    def __createCustomDeck(self, save=False):
        log("__createCustomDeck")

        if self.profile and not self.profile.kanjiCustomProfileEnabled:
            return

        deck = mw.col.decks.byName(self.profile.kanjiDeckName)
        cards = AnkiHelper.getCards(deck["id"])
        kanjiDict = dict()
        for card in cards:
            note = card.note
            try:
                kanjiDict[note[self.profile.kanjiExpression]] = (note, card.ivl)
            except:
                continue

        #self.dlmod = deck["mod"]
        #self.nlmod, self.clmod = AnkiHelper.getLastModified(deck["id"])

        if save or KanjiOverlay.__saveCustomDict:
            kanjiFile = open(self.kanjiCustomDictPath, "wb")
            pickle.dump(kanjiDict, kanjiFile, 2)

        return kanjiDict

    def __loadDefaultKanjiDB(self):
        if self.__defaultKanjiDict:
            return self.__defaultKanjiDict
        if os.path.exists(self.kanjiDefaultDictPath) == False:
            raise Exception("Missing Default Dict")
        kanjiFile = open(self.kanjiDefaultDictPath, "rb")
        kanjiDict = pickle.load(kanjiFile)
        self.__defaultKanjiDict = kanjiDict
        return kanjiDict

    def __loadTemplate(self):
        if os.path.exists(self.templateUserFiles):
            self.template = readFile(self.templateUserFiles)
        else:
            self.template = readFile(self.templateInPlugin)

        if self.template == None:
            self.template = u""

    def __addHooks(self):
        addHook("fmod_kol", self.injectKanjiOverlay)
        if self.profile.kanjiDisplayWithFuriganaMod:
            addHook("fmod_furigana", self.injectKanjiOverlay)
            addHook("fmod_kanji", self.injectKanjiOverlay)
        addHook('prepareQA', self.__prepareQA)

    def __prepareQA(self, html, card, context):
        html += self.css
        html += self.scripts
        return html

    def __loadCss(self):
        try:
            css = readFile(self.cssFileInPlugin)

            if os.path.exists(self.cssFileUserFiles):
                cssInProfile = readFile(self.cssFileUserFiles)
                css += cssInProfile
        except:
            css = u""
        self.css = '<style>' + css + '</style>'

    def __loadScripts(self):
        try:
            if os.path.exists(self.scriptsFileUserFiles):
                scripts = readFile(self.scriptsFileUserFiles)
            else:
                scripts = readFile(self.scriptsFileInPlugin)
        except:
            scripts = u""
        self.scripts = '<script>' + scripts + '</script>'

    def injectKanjiOverlay(self, txt, *args):
        def remap():
            for c in txt:
                if c >= u"\u4E00" and c <= u"\u9FBF":  # Kanji
                    yield self.__createHtml(c)
                else:
                    yield c
        return "".join([x for x in remap()])
    
    def __getKanjiUrl(self, kanji):
        url = None
        if self.profile.kanjiUseLink:
            url = self.profile.kanjiUseLinkUrl
            url = url % kanji if "%s" in url else url + kanji
        return url

    def __createHtml(self, kanji):
        if kanji in self.kanjiDict:
            ankiNote, ivl = self.kanjiDict.get(kanji)
            context = dict(ankiNote)

            unkownClass = self.__CssClassOfNotReviewedKanji if ivl <= 0 and self.profile.kanjiCustomProfileEnabled else ""
            context["class"] = unkownClass

            context["keyword"] = self.__getValue(context, self.profile.kanjiKeyword) or self.__getValue(context, "keyword")

            if self.profile.kanjiOnYomiEnabled:
                context["kol-onYomi"] = self.__getValue(context, self.profile.kanjiOnYomi) or self.__getValue(context, "onYomi")

            if self.profile.kanjiKunYomiEnabled:
                context["kol-kunYomi"] = self.__getValue(context, self.profile.kanjiKunYomi) or self.__getValue(context, "kunYomi")

            if self.profile.kanjiMemoStoryEnabled:
                context["kol-memoStory"] = self.__getValue(context, self.profile.kanjiMemoStory) or self.__getValue(context, "heisigStory")
        else:
            context = dict()
            context["class"] = self.__CssClassOfUnknownKanji

        context["kanji"] = kanji
        context["kanjiLink"] = self.__getKanjiUrl(kanji)

        return Template(self.template, context).render()

    def __getValue(self, note, attr):
        if attr in note:
            return note[attr]
        return None
