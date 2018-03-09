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
from kol.src.utils import log

class KanjiOverlay:
    DEFAULT_PROFILE = KolConfig()

    # usually data is only loaded, if modiefiet. if (True): always load data in the load-method
    __alwaysLoadNewDictData = False
    __DEBUG__ShowExceptions = False
    __saveCustomDict = False
    __CssClassOfNotReviewedKanji = " unknown"
    __CssClassOfUnknownKanji = "kol-missing"

    profile = None

    @staticmethod
    def injectCss(card):
        return "<style>%s</style>" % KanjiOverlay.css + KanjiOverlay.oldCss(card)

    def load(self):
        log("Load Plugin")

        self.__defaultKanjiDict = None
        self.__kolConfigsManager = KolConfigsManager.getInstance()

        profileName = mw.pm.name
        self.profile = self.__kolConfigsManager.getProfileByName(profileName)

        if not self.profile.kanjiCustomProfileEnabled:
            self.profile = KanjiOverlay.DEFAULT_PROFILE

        if (not (self.profile.kanjiShowColorsForKnownKanji)):
            self.__CssClassOfNotReviewedKanji = ""
            self.__CssClassOfUnknownKanji = ""

        self.__setupObjectData(self.profile)
        self.__loadKanjiDict()
        self.__addCSS()
        self.__loadTemplate()
        self.__addHooks()

        log("End Load Plugin")

    def openConfigDialog(self):
        # for testing:
        # AnkiConnection = KolConfig.ankiConnectionMOCK()
        KolConfigDialog.startUi(mw)

        self.reload()

    def __setupObjectData(self, profileVar):
        self.kanjiCustomDictPath = os.path.join(mw.pm.profileFolder(), "custom-kol.db")
        self.kanjiDefaultDictPath = os.path.join(mw.pm.addonFolder(), "kol", "data", "english-kol.db")

        self.cssFileInPlugin = os.path.join(mw.pm.addonFolder(), "kol", "data", "styles-kol.css")
        self.cssFileInProfile = os.path.join(mw.pm.profileFolder(), "styles-kol.css")

        self.templateInPlugin = os.path.join(mw.pm.addonFolder(), "kol", "data", "template-kol.hbs")

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

    def __loadCustomKanjiDB(self):
        if os.path.exists(self.kanjiCustomDictPath):
            kanjiFile = open(self.kanjiCustomDictPath, "rb")
            self.dlmod, self.nlmod, self.clmod, kanjiDict = pickle.load(kanjiFile)
            deck = mw.col.decks.byName(self.profile.kanjiDeckName)
            if (AnkiHelper.isDeckModified(self.dlmod, self.nlmod, self.clmod, deck)
                or self.__alwaysLoadNewDictData):
                kanjiDict = self.__createCustomDeck()
        else:
             kanjiDict = self.__createCustomDeck()

        return kanjiDict

    def __createCustomDeck(self, save=False):
        log("__createCustomDeck")

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

    def __addCSS(self):
        KanjiOverlay.css = self.loadCss()
        KanjiOverlay.oldCss = Card.css
        Card.css = KanjiOverlay.injectCss

    def __addHooks(self):
        addHook("fmod_kol", self.injectKanjiOverlay)
        if self.profile.kanjiDisplayWithFuriganaMod:
            addHook("fmod_furigana", self.injectKanjiOverlay)
            addHook("fmod_kanji", self.injectKanjiOverlay)

    def reload(self):
        #self.unload()
        #oldValue = self.__alwaysLoadNewDictData
        #self.__alwaysLoadNewDictData = True
        #self.load()
        # restore old value
        #self.__alwaysLoadNewDictData = oldValue
        log("reload start")
        self.kanjiDict = self.__createCustomDeck()
        log("reload stop")

    def loadCss(self):
        try:
            f = open(self.cssFileInPlugin, "r")
            css = unicode(f.read(), "utf-8")
            f.close()

            if os.path.exists(self.cssFileInProfile):
                f = open(self.cssFileInProfile, "r")
                cssInProfile = unicode(f.read(), "utf-8")
                css += cssInProfile
                f.close()

        except:
            css = u""
        return css

    def __loadTemplate(self):
        try:
            f = open(self.templateInPlugin, "r")
            self.template = unicode(f.read(), "utf-8")
            f.close()
        except:
            self.template = u""

    def unload(self):
        Card.css = KanjiOverlay.oldCss

    def injectKanjiOverlay(self, txt, *args):
        # TODO: seems to crash Anki when using the browser :/
        # if self.kanjiUseCustomDeck and os.path.exists(self.kanjiCustomDictPath): # reload if deck modified,
        #    deck = mw.col.decks.byName(self.kanjiDeckName)
        #    log("test deck modified")
        #    if AnkiHelper.isDeckModified(self.dlmod, self.nlmod, self.clmod, deck): # seems to crash Anki when search
        #        self.kanjiDict = self.__loadFromCustomDeck()
        def remap():
            for c in txt:
                if c >= u"\u4E00" and c <= u"\u9FBF":  # Kanji
                    if c in self.kanjiDict:
                        note, ivl = self.kanjiDict.get(c)
                        unkown = self.__CssClassOfNotReviewedKanji if ivl <= 0 and self.profile.kanjiCustomProfileEnabled else ""
                        overlay = self.__createOverlayHtml(note)

                        res = "<span class='kol%s'>%s<span class='overlay'>%s</span></span>" % (unkown, c, overlay)
                        if self.profile.kanjiUseLink:
                            url = self.profile.kanjiUseLinkUrl
                            url = url % c if "%s" in url else url + c
                            res = "<a style='text-decoration:none;' href='%s'>%s</a>" % (url, res)
                        yield res
                    else:
                        yield "<span class='" + self.__CssClassOfUnknownKanji + "'>%s</span>" % (c)
                else:
                    yield c

        return "".join([x for x in remap()])

    def __createOverlayHtml(self, ankiNote):
        context = dict(ankiNote)
        context["keyword"] = self.__getValue(context, self.profile.kanjiKeyword) or self.__getValue(context, "keyword")

        if self.profile.kanjiOnYomiEnabled:
            context["kol-onYomi"] = self.__getValue(context, self.profile.kanjiOnYomi) or self.__getValue(context, "onYomi")

        if self.profile.kanjiKunYomiEnabled:
            context["kol-kunYomi"] = self.__getValue(context, self.profile.kanjiKunYomi) or self.__getValue(context, "kunYomi")

        if self.profile.kanjiMemoStoryEnabled:
            context["kol-memoStory"] = self.__getValue(context, self.profile.kanjiMemoStory) or self.__getValue(context, "heisigStory")

        return Template(self.template, context).render()

    def __getValue(self, note, attr):
        if attr in note:
            return note[attr]
        return None

