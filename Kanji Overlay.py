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

from kol.AnkiHelper import *

class KanjiOverlay:
    
    ################# CUSTOMIZE ###################
    Profiles = {
        "DEFAULT" : { #Profile by default
            "KanjiUseCustomDeck" : True, #False : Use default english keyword from Heisig
            "KanjiCustomDeckName" : u'日本語::漢字::意味', 
            "KanjiCustomExpression" : "Expression",
            "KanjiCustomKeyword" : "French Keyword",
            "KanjiDisplayWithFuriganaMod" : True
        },
        "FanAtiC" : { #Other Profile Name
            "KanjiUseCustomDeck" : True,
            "KanjiCustomDeckName" : u'日本語::漢字::意味',
            "KanjiCustomExpression" : "Expression",
            "KanjiCustomKeyword" : "French Keyword",
            "KanjiDisplayWithFuriganaMod" : True
        }
        # Add other Profile name
    }
    ################################################

    def load(self):
        
        log("Load Plugin")
        
        profileName = mw.pm.name
        pf = self.Profiles
        profileVar = pf["DEFAULT"] if not profileName in pf else pf[profileName]
        self.KanjiUseCustomDeck = profileVar["KanjiUseCustomDeck"]
        if self.KanjiUseCustomDeck:
            self.KanjiDeckName = profileVar["KanjiCustomDeckName"]
            self.KanjiExpression = profileVar["KanjiCustomExpression"]
            self.KanjiKeyword = profileVar["KanjiCustomKeyword"]
        self.KanjiDisplayWithFuriganaMod = profileVar["KanjiDisplayWithFuriganaMod"]
        
        self.kanjiCustomDictPath = kanjiCustomDictPath = os.path.join(mw.pm.profileFolder(), 'custom-kol.db')
        self.kanjiDefaultDictPath = kanjiDefaultDictPath = os.path.join(mw.pm.addonFolder(), 'kol', 'english-kol.db')
        self.cssFileInPlugin = os.path.join(mw.pm.addonFolder(), 'kol', 'default-kol.css')
        self.cssFileInProfile = os.path.join(mw.pm.profileFolder(), 'custom-kol.css')
        self.kanjiDict = None
        
        if self.KanjiUseCustomDeck:            
            if os.path.exists(kanjiCustomDictPath):
                kanjiFile = open(kanjiCustomDictPath, "rb")
                self.dlmod, self.nlmod, self.clmod, self.kanjiDict = pickle.load(kanjiFile)
                
                deck = mw.col.decks.byName(self.KanjiDeckName)
                if AnkiHelper.isDeckModified(self.dlmod, self.nlmod, self.clmod, deck):
                    self.kanjiDict = self.loadFromCustomDeck()
            else:
                self.kanjiDict = self.loadFromCustomDeck()
        else:
            if os.path.exists(kanjiDefaultDictPath) == False:
                raise Exception('Missing Default Dict')
            kanjiFile = open(kanjiDefaultDictPath, "rb")
            self.dlmod, self.nlmod, self.clmod, self.kanjiDict = pickle.load(kanjiFile)

        # Add CSS
        if not os.path.exists(self.cssFileInProfile):
            shutil.copy2(self.cssFileInPlugin, self.cssFileInProfile)
            
        KanjiOverlay.css = self.loadCss()
        KanjiOverlay.oldCss = Card.css
        Card.css = injectCss

        addHook('fmod_kol', self.injectKanjiOverlay)
        if self.KanjiDisplayWithFuriganaMod:
            addHook('fmod_furigana', self.injectKanjiOverlay)
            addHook('fmod_kanji', self.injectKanjiOverlay)
        
        log("End Load Plugin")
    
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
        #seems to crash Anki when using the browser :/
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
                        unkown = " unknown" if ivl <= 0 and self.KanjiUseCustomDeck else ""
                        yield '<span class="kol%s">%s<span>%s</span></span>' % (unkown, c, kw)
                    else: yield '<span class="kol-missing">%s</span>' % (c)
                else: yield c
        return ''.join([x for x in remap()])

    def loadFromCustomDeck(self):
        log("loadFromCustomDeck")
        deck = mw.col.decks.byName(self.KanjiDeckName)
        cards = AnkiHelper.getCards(deck["id"])

        kanjiDict = dict()
        for card in cards:
            note = card.note
            try:
                kanjiDict[note[self.KanjiExpression]] = (note[self.KanjiKeyword], card.ivl)
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

kanji = KanjiOverlay()
addHook("profileLoaded", kanji.load)
addHook("unloadProfile", kanji.unload)
