#-*- coding: utf-8 -*-
#
# Kanji Keyword Overlay
#
# Insperated from the Work of Brian Bush on Anki v1 plugin, thank you very much
#

import os, pickle, datetime, codecs

from aqt import mw

from anki.hooks import addHook
from anki.utils import ids2str

from kol.AnkiHelper import *

class KanjiOverlay:
    
    ################# CUSTOMIZE ###################
    Profiles = {
        "DEFAULT" : { #Profile by default
            "KanjiUseCustomDeck" : True,
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
        self.kanjiDict = None
        
        if self.KanjiUseCustomDeck:            
            if os.path.exists(kanjiCustomDictPath):
                kanjiFile = open(kanjiCustomDictPath, "rb")
                mod, self.kanjiDict = pickle.load(kanjiFile)
                
                deck = mw.col.decks.byName(self.KanjiDeckName)
                if deck["mod"] != mod:
                    self.kanjiDict = self.loadFromCustomDeck()
            else:
                self.kanjiDict = self.loadFromCustomDeck()
        else:
            if os.path.exists(kanjiDefaultDictPath) == False:
                raise Exception('Missing Default Dict')
            kanjiFile = open(kanjiDefaultDictPath, "rb")
            mod, self.kanjiDict = pickle.load(kanjiFile)

        addHook('fmod_kol', self.injectKanjiOverlay)
        if self.KanjiDisplayWithFuriganaMod:
            addHook('fmod_furigana', self.injectKanjiOverlay)
            addHook('fmod_kanji', self.injectKanjiOverlay)
        
        log("End Load Plugin")
        
    def injectKanjiOverlay(self, txt, *args):
        def remap():
            for c in txt:
                if c >= u'\u4E00' and c <= u'\u9FBF': #Kanji
                    if c in self.kanjiDict:
                        kw, ivl = self.kanjiDict.get(c)
                        unkown = " unknown" if ivl <= 0 and self.KanjiUseCustomDeck else ""
                        yield '<span class="kol%s" title="%s">%s</span>' % (unkown, kw, c)
                    else: yield '<span class="kol missing">%s</span>' % (c)
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

        kanjiFile = open(self.kanjiCustomDictPath, "wb")
        pickle.dump((deck["mod"], kanjiDict), kanjiFile, 2)
        
        return kanjiDict
    
def log(msg):
    logPath = os.path.join(mw.pm.addonFolder(), 'kol', 'main.log')
    txt = '%s: %s' % (datetime.datetime.now(), msg)
    f = codecs.open(logPath, 'a', 'utf-8')
    f.write(txt + '\n')
    f.close()
    print txt

kanji = KanjiOverlay()
addHook("profileLoaded", kanji.load)

