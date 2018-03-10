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
from aqt.qt import QAction, QMenu

from kol.src.KolOverlay import KanjiOverlay
from kol.src.utils import log

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

    menuTools = mw.form.menuTools

    menuTools.addMenu(addMenuItems(menuTools))

    #for child in mw.form.menuTools.children():
    #    try:
    #        log(child.title())
    #        if(child.title() == "Add-ons"):
    #            addMenuItems(child)
    #            return True
    #    except:
    #        continue

def addMenuItems(child):
    kanjiOverlayMenu = QMenu("Kanji Overlay", child)
    addMenuItem(kanjiOverlayMenu, "Config Dialog", kanjiOverlay.openConfigDialog)
    addMenuItem(kanjiOverlayMenu, "Reload", kanjiOverlay.reload)
    return kanjiOverlayMenu

def addMenuItem(child, menuLabel, action = None):
    menuItem = QAction(menuLabel, mw)
    if action != None:
        menuItem.triggered.connect(action)
    child.addAction(menuItem)
    return menuItem

# ------------------------------------------------------------------------------
# -------------------------   hooks  -------------------------------------------
# ------------------------------------------------------------------------------

kanjiOverlay = KanjiOverlay()
addHook("profileLoaded", addToMenuBar)
addHook("profileLoaded", kanjiOverlay.load)
addHook("unloadProfile", kanjiOverlay.unload)
