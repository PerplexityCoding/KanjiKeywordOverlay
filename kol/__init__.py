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

from aqt import mw, gui_hooks

from .src.KolOverlay import KanjiOverlay

# Clear logs
from .src.utils import resetLog
resetLog()

# ------------------------------------------------------------------------------
# -------------------------   hooks  -------------------------------------------
# ------------------------------------------------------------------------------

kanjiOverlay = KanjiOverlay()
gui_hooks.profile_did_open.append(kanjiOverlay.load)
gui_hooks.profile_will_close.append(kanjiOverlay.unload)

mw.addonManager.setConfigAction(__name__, kanjiOverlay.openConfigDialog)
