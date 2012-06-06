##############################################################################################

                        Kanji OverLay v0.1 - Anki Plugin
						--------------------------------

Git: https://github.com/fanatic84/KanjiKeywordOverlay.git
Contact: fanatic84@gmail.com

#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#- WHAT IS IT ? #-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-

Kanji OverLay is a anki-plugin used to display Keywords on Kanji (from Heisig or other)
When you move your cursor on a kanji, it display a pop-in with the corresponding keyword.

See screenshots:
http://anki.plugins.s3.amazonaws.com/KanjiOverlay/screens/screen1.jpg

---
Kanji OverLay can also change the color a kanji depending of your knowledge of them.
This needs a custom deck to be specified. See "How to use ?" for more informations.

See screenshots:
http://anki.plugins.s3.amazonaws.com/KanjiOverlay/screens/screen2.jpg

Red : kanji not seen
Blue : kanji not referenced at all (3007 kanji referenced by default so it is fairly rare)


#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#- HOW TO USE ? #-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-

A. Do nothing :) 

(If you have japanese plugin installed)

By default, Kanji OverLay plugin use a predefined English Keywords set using Heisig.
By default, When you specified the special tag : {{furigana:}} or {{kanji:}} in your template,
Kanji Overlay plugin will display information for kanji on kanjis of thoses expression.

----------------------------------------------------------------------------------------------
B.1 Configure by modifing "Kanji Overlay.py"

Localise the "Profiles" Variable in the top of the file, which would look like that:

----

Profiles = {
	"DEFAULT" : { #Profile by default
	    "KanjiUseCustomDeck" : False,
	    "KanjiCustomDeckName" : u'日本語::漢字::RTK13',
	    "KanjiCustomExpression" : "Kanji",
	    "KanjiCustomKeyword" : "Keyword",
	    "KanjiDisplayWithFuriganaMod" : True
	},
	"Other Profile Name" : { #Optional
		...
	}
}
----

* "KanjiUseCustomDeck" : True or False; Activate Custom Decks
* "KanjiCustomDeckName" : The full name of your kanji deck
* "KanjiCustomExpression" : the name of the field containing the kanji
* "KanjiCustomKeyword" : the name of the field containing the keyword
* "KanjiDisplayWithFuriganaMod" : True or False; Activate Kanji OverLay for 
   {{furigana:}} or {{kanji:}} tags in your templates. True by default.

If the profile name of your account is not found, then Default is used.

B.2 Add special tags in your template {{kol:}} tag (Kanji OverLay)

You can activate Kanji OverLay on all fields using special {{kol:}} tag.
For instance, {{kol:Expression}}

----------------------------------------------------------------------------------------------
C. Change the style of the pop-in

You can change the style of the pop-in by editing the custom-kol.css,
that the plugin placed in your profile folder.


#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#- CHANGES -#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-

v0.1:
  - Display Keyword popup
  - Use custom Kanji Deck or predefined English Keyword (Heisig)
  - Reload kanji keyword dictionnary only if modified
  - Change color of the kanji if seen, missing
  
  
#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#- THANKS #-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-
- Insperated from the anki v1 plugin of Brian Bush, Thanks !
- The plugin "Local css" for Anki 2 of Roland Sieker, Thanks !
- Of corse, Damien Elmes for Anki & Anki 2, Thanks !!

