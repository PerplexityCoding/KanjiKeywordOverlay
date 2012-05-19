#
# Kanji Keyword Overlay
#
# Insperated from the Work of Brian Bush on Anki v1 plugin, thank you very much
#

import os
import pickle
import threading

from aqt import mw

from anki.hooks import addHook

class KanjiKeywordOverlay:
    
    ############################## CUSTOMIZE ###############################################
    KanjiUseCustomDeck = True
    KanjiDeckName = "日本語::漢字::意味"
    KanjiExpression = "Expression"
    KanjiKeyword = "French Keyword"
    ########################################################################################

    def load(self):

        kanjiCustomDictPath = os.path.join(mw.pm.profileFolder(), 'custom-kko.db')
        kanjiDefaultDictPath = os.path.join(mw.pm.addonFolder(), 'kko', 'english-kko.db')
        self.kanjiDict = None
        
        if self.KanjiUseCustomDeck == True:
            if os.path.exists(kanjiCustomDictPath):
                kanjiFile = open(kanjiCustomDictPath, "rb")
                self.kanjiDict = pickle.load(kanjiFile)
            else:
                self.kanjiDict = self.loadFromCustomDeck()
                kanjiFile = open(kanjiCustomDictPath, "wb")
                pickle.dump(self.kanjiDict, kanjiFile, 2)
        else:
            if os.path.exists(kanjiDefaultDictPath) == False:
                raise Exception('Missing Default Dict')
            kanjiFile = open(kanjiDefaultDictPath, "rb")
            self.kanjiDict = pickle.load(kanjiFile)

        addHook('fmod_kko', self.injectKanjiOverlay)
        
    def injectKanjiOverlay(self, txt, *args):
        def remap():
            for t in txt:
                kw = self.kanjiDict.get(t)
                if kw:
                    yield '<span class="kko" title="%s">%s</span>' % (kw, t)
                else: yield t
        return ''.join([x for x in remap()])

    def loadFromCustomDeck(self):
        cardsId = mw.col.findCards("deck:" + self.KanjiDeckName)
        kanjiDict = dict()
        for cardId in cardsId:
            card = mw.col.getCard(cardId)
            note = card.note()
            try:
                kanjiDict[note[self.KanjiExpression]] = note[self.KanjiKeyword]
            except: continue
        return kanjiDict

kanji = KanjiKeywordOverlay()
addHook("profileLoaded", kanji.load)

