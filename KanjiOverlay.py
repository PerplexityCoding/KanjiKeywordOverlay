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
# Big thanks for Ricky for Adding GUI for the plugin
#

from anki.hooks import addHook
from aqt import mw
from aqt.qt import QAction, SIGNAL

from kol.src.KolOverlay import KanjiOverlay

# ------------------------------------------------------------------------------
# -----------------------   For Menu in Anki -----------------------------------
# ------------------------------------------------------------------------------

menuBarAdded = False

def addToMenuBar():
    global menuBarAdded
    # The menu goes to
    # Tools -> Add-Ons -> KanjiOverlay

    if menuBarAdded:
        return

    menuBarAdded = True

    for child in mw.form.menuPlugins.children():
        try:
            if(child.title() == "KanjiOverlay"):
                addMenuItems(child)
                return True

        except:
            continue

def addMenuItems(child):
    addMenuItem(child, "Config Dialog", kanjiOverlay.openConfigDialog)
    addMenuItem(child, "Reload", kanjiOverlay.reload)
    addMenuItem(child, "Reset", kanjiOverlay.reset)

def addMenuItem(child, menuLabel, action):
    menuItem = QAction(menuLabel, mw)
    mw.connect(menuItem, SIGNAL("triggered()"), action)
    child.addAction(menuItem)

# ------------------------------------------------------------------------------
# -------------------------   hooks  -------------------------------------------
# ------------------------------------------------------------------------------

kanjiOverlay = KanjiOverlay()
addHook("profileLoaded", addToMenuBar)
addHook("profileLoaded", kanjiOverlay.load)
addHook("unloadProfile", kanjiOverlay.unload)
