#-*- coding: utf-8 -*-
#
# Kanji Overlay Anki Plugin
#
# Comments & Suggestions at: fanatic84@gmail.com
#
# MIT License
#
# Insperated from the Work of Brian Bush on Anki v1 plugin, thank you very much
# Thanks for Roland Sieker <ospalh@gmail.com> and his plugin Local css for Anki 2
# Big thanks for Ricky for Adding GUI for the plugin
#

from anki.hooks import addHook
from aqt import mw

from kol.src.KolOverlay import KanjiOverlay

# ------------------------------------------------------------------------------
# -------------------------   hooks  -------------------------------------------
# ------------------------------------------------------------------------------

kanjiOverlay = KanjiOverlay()
addHook("profileLoaded", kanjiOverlay.load)
addHook("unloadProfile", kanjiOverlay.unload)

mw.addonManager.setConfigAction(__name__, kanjiOverlay.openConfigDialog)
