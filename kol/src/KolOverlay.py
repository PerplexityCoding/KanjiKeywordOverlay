import os
import json
from json import JSONEncoder

from anki import hooks
from aqt import gui_hooks

from anki.cards import Card
from aqt import mw, reviewer, clayout
from aqt.utils import showInfo

from .lib import pystache
from . import KolConfigDialog
from .AnkiHelper import AnkiHelper
from .KolConfigsManager import KolConfig, KolConfigsManager
from .utils import log, readFile

class KanjiOverlay:
    DEFAULT_PROFILE = KolConfig()

    # usually data is only loaded, if modiefiet. if (True): always load data in the load-method
    __alwaysLoadNewDictData = False
    __DEBUG__ShowExceptions = False
    __saveCustomDict = False
    __CssClassOfNotReviewedKanji = "kol-unknown"
    __CssClassOfUnknownKanji = "kol-missing"
    __renderer = pystache.Renderer()

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
        log("open config dialog")
        KolConfigDialog.startUi(mw)

        self.reload()

    def __setupObjectData(self):
        addon_package = mw.addonManager.addonFromModule(__name__)

        self.kanjiDefaultDictPath = os.path.join(mw.pm.addonFolder(), addon_package, "data", "english.json.db")
        self.kanjiCustomDictPath = os.path.join(mw.pm.addonFolder(), addon_package, "user_files", "custom-kol.json.db")

        self.cssFileInPlugin = os.path.join(mw.pm.addonFolder(), addon_package, "data", "styles.css")
        self.cssFileUserFiles = os.path.join(mw.pm.addonFolder(), addon_package, "user_files", "styles.css")

        self.scriptsFileInPlugin = os.path.join(mw.pm.addonFolder(), addon_package, "data", "scripts.js")
        self.scriptsFileUserFiles = os.path.join(mw.pm.addonFolder(), addon_package, "user_files", "scripts.js")

        self.templateInPlugin = os.path.join(mw.pm.addonFolder(), addon_package, "data", "template.hbs")
        self.templateUserFiles = os.path.join(mw.pm.addonFolder(), addon_package, "user_files", "template.hbs")

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
                kanjiDict[note[self.profile.kanjiExpression]] = (note.items(), card.ivl)
            except:
                continue

        #self.dlmod = deck["mod"]
        #self.nlmod, self.clmod = AnkiHelper.getLastModified(deck["id"])

        if save or KanjiOverlay.__saveCustomDict:
            kanjiFile = open(self.kanjiCustomDictPath, "w")
            json.dump(kanjiDict, kanjiFile)

        return kanjiDict

    def __loadDefaultKanjiDB(self):
        if self.__defaultKanjiDict:
            return self.__defaultKanjiDict
        if os.path.exists(self.kanjiDefaultDictPath) == False:
            raise Exception("Missing Default Dict")
        kanjiFile = open(self.kanjiDefaultDictPath, "rb")
        kanjiDict = json.load(kanjiFile)

        self.__defaultKanjiDict = kanjiDict
        return kanjiDict

    def __loadTemplate(self):
        if os.path.exists(self.templateUserFiles):
            self.template = readFile(self.templateUserFiles)
        else:
            self.template = readFile(self.templateInPlugin)

        if self.template == None:
            self.template = u""
        else:
            self.parsedTemplate = pystache.parse(self.template)

    def __addFilters(self, field_text, field_name, filter_name, ctx):
        log(filter_name)
        if filter_name == "kol":
            return self.injectKanjiOverlay(field_text)
        else:
            return field_text

    def __addHooks(self):
        hooks.field_filter.append(self.__addFilters)
        gui_hooks.webview_will_set_content.append(self.__appendScripts)

    def __appendScripts(self, web_content, context):
        if isinstance(context, reviewer.Reviewer) or isinstance(context, clayout.CardLayout):
            web_content.head += self.css
            web_content.body += self.scripts

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
            context = dict()
            for i in ankiNote:
                context[i[0]] = i[1]

            unkownClass = self.__CssClassOfNotReviewedKanji if ivl <= 0 and self.profile.kanjiCustomProfileEnabled else ""
            context["kol-class"] = unkownClass

            context["kol-keyword"] = self.__getValue(context, self.profile.kanjiKeyword) or self.__getValue(context, "keyword")

            if self.profile.kanjiOnYomiEnabled:
                context["kol-onYomi"] = self.__getValue(context, self.profile.kanjiOnYomi) or self.__getValue(context, "onYomi")

            if self.profile.kanjiKunYomiEnabled:
                context["kol-kunYomi"] = self.__getValue(context, self.profile.kanjiKunYomi) or self.__getValue(context, "kunYomi")

            if self.profile.kanjiMemoStoryEnabled:
                context["kol-memoStory"] = self.__getValue(context, self.profile.kanjiMemoStory) or self.__getValue(context, "heisigStory")
        else:
            context = dict()
            context["kol-class"] = self.__CssClassOfUnknownKanji

        context["kol-kanji"] = kanji
        context["kol-kanjiLink"] = self.__getKanjiUrl(kanji)

        return self.__renderer.render(self.parsedTemplate, context)

    def __getValue(self, note, attr):
        if attr in note:
            return note[attr]
        return None
