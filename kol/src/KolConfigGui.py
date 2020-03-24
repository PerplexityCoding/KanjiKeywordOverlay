# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'kol/src/KolConfigGui.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(455, 479)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.tabWidget = QtWidgets.QTabWidget(Dialog)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.tab)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSpacing(7)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label = QtWidgets.QLabel(self.tab)
        self.label.setObjectName("label")
        self.verticalLayout_4.addWidget(self.label)
        self.label_3 = QtWidgets.QLabel(self.tab)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_4.addWidget(self.label_3)
        self.horizontalLayout.addLayout(self.verticalLayout_4)
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.cboProfiles = QtWidgets.QComboBox(self.tab)
        self.cboProfiles.setToolTip("")
        self.cboProfiles.setStatusTip("")
        self.cboProfiles.setWhatsThis("")
        self.cboProfiles.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.cboProfiles.setEditable(False)
        self.cboProfiles.setObjectName("cboProfiles")
        self.verticalLayout_6.addWidget(self.cboProfiles)
        self.chkUseCustomDeck = QtWidgets.QCheckBox(self.tab)
        self.chkUseCustomDeck.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.chkUseCustomDeck.setText("")
        self.chkUseCustomDeck.setObjectName("chkUseCustomDeck")
        self.verticalLayout_6.addWidget(self.chkUseCustomDeck)
        self.horizontalLayout.addLayout(self.verticalLayout_6)
        self.verticalLayout_5.addLayout(self.horizontalLayout)
        self.line = QtWidgets.QFrame(self.tab)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout_5.addWidget(self.line)
        self.gpbKanjiData = QtWidgets.QGroupBox(self.tab)
        self.gpbKanjiData.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.gpbKanjiData.sizePolicy().hasHeightForWidth())
        self.gpbKanjiData.setSizePolicy(sizePolicy)
        self.gpbKanjiData.setFlat(False)
        self.gpbKanjiData.setObjectName("gpbKanjiData")
        self.verticalLayout_11 = QtWidgets.QVBoxLayout(self.gpbKanjiData)
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.verticalLayout_12 = QtWidgets.QVBoxLayout()
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.label_4 = QtWidgets.QLabel(self.gpbKanjiData)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_12.addWidget(self.label_4)
        self.label_5 = QtWidgets.QLabel(self.gpbKanjiData)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_12.addWidget(self.label_5)
        self.label_2 = QtWidgets.QLabel(self.gpbKanjiData)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_12.addWidget(self.label_2)
        self.chkOnYomi = QtWidgets.QCheckBox(self.gpbKanjiData)
        self.chkOnYomi.setObjectName("chkOnYomi")
        self.verticalLayout_12.addWidget(self.chkOnYomi)
        self.chkKunYomi = QtWidgets.QCheckBox(self.gpbKanjiData)
        self.chkKunYomi.setObjectName("chkKunYomi")
        self.verticalLayout_12.addWidget(self.chkKunYomi)
        self.chkMemoStory = QtWidgets.QCheckBox(self.gpbKanjiData)
        self.chkMemoStory.setObjectName("chkMemoStory")
        self.verticalLayout_12.addWidget(self.chkMemoStory)
        self.horizontalLayout_6.addLayout(self.verticalLayout_12)
        self.verticalLayout_13 = QtWidgets.QVBoxLayout()
        self.verticalLayout_13.setObjectName("verticalLayout_13")
        self.cboCustomDeckName = QtWidgets.QComboBox(self.gpbKanjiData)
        self.cboCustomDeckName.setEditable(True)
        self.cboCustomDeckName.setObjectName("cboCustomDeckName")
        self.verticalLayout_13.addWidget(self.cboCustomDeckName)
        self.cboCustomExpression = QtWidgets.QComboBox(self.gpbKanjiData)
        self.cboCustomExpression.setEditable(True)
        self.cboCustomExpression.setObjectName("cboCustomExpression")
        self.verticalLayout_13.addWidget(self.cboCustomExpression)
        self.cboCustomKeyword = QtWidgets.QComboBox(self.gpbKanjiData)
        self.cboCustomKeyword.setEditable(True)
        self.cboCustomKeyword.setObjectName("cboCustomKeyword")
        self.verticalLayout_13.addWidget(self.cboCustomKeyword)
        self.cboOnYomi = QtWidgets.QComboBox(self.gpbKanjiData)
        self.cboOnYomi.setEnabled(False)
        self.cboOnYomi.setEditable(True)
        self.cboOnYomi.setObjectName("cboOnYomi")
        self.verticalLayout_13.addWidget(self.cboOnYomi)
        self.cboKunYomi = QtWidgets.QComboBox(self.gpbKanjiData)
        self.cboKunYomi.setEditable(True)
        self.cboKunYomi.setObjectName("cboKunYomi")
        self.verticalLayout_13.addWidget(self.cboKunYomi)
        self.cboMemoStory = QtWidgets.QComboBox(self.gpbKanjiData)
        self.cboMemoStory.setEnabled(False)
        self.cboMemoStory.setEditable(True)
        self.cboMemoStory.setObjectName("cboMemoStory")
        self.verticalLayout_13.addWidget(self.cboMemoStory)
        self.horizontalLayout_6.addLayout(self.verticalLayout_13)
        self.verticalLayout_11.addLayout(self.horizontalLayout_6)
        self.verticalLayout_5.addWidget(self.gpbKanjiData)
        self.gpbAdvanced = QtWidgets.QGroupBox(self.tab)
        self.gpbAdvanced.setEnabled(False)
        self.gpbAdvanced.setObjectName("gpbAdvanced")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout(self.gpbAdvanced)
        self.verticalLayout_10.setContentsMargins(2, 2, 2, 2)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setContentsMargins(5, -1, 5, -1)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.chkAlsoLoadDefaultDB = QtWidgets.QCheckBox(self.gpbAdvanced)
        self.chkAlsoLoadDefaultDB.setObjectName("chkAlsoLoadDefaultDB")
        self.verticalLayout_7.addWidget(self.chkAlsoLoadDefaultDB)
        self.chkColorizeKanjis = QtWidgets.QCheckBox(self.gpbAdvanced)
        self.chkColorizeKanjis.setToolTip("")
        self.chkColorizeKanjis.setObjectName("chkColorizeKanjis")
        self.verticalLayout_7.addWidget(self.chkColorizeKanjis)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.chkKanjiLink = QtWidgets.QCheckBox(self.gpbAdvanced)
        self.chkKanjiLink.setMinimumSize(QtCore.QSize(150, 0))
        self.chkKanjiLink.setObjectName("chkKanjiLink")
        self.horizontalLayout_2.addWidget(self.chkKanjiLink)
        self.editKanjiLink = QtWidgets.QLineEdit(self.gpbAdvanced)
        self.editKanjiLink.setEnabled(False)
        self.editKanjiLink.setObjectName("editKanjiLink")
        self.horizontalLayout_2.addWidget(self.editKanjiLink)
        self.verticalLayout_7.addLayout(self.horizontalLayout_2)
        self.verticalLayout_10.addLayout(self.verticalLayout_7)
        self.verticalLayout_5.addWidget(self.gpbAdvanced)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.tab_2)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout()
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.textEdit = QtWidgets.QTextEdit(self.tab_2)
        self.textEdit.setObjectName("textEdit")
        self.verticalLayout_8.addWidget(self.textEdit)
        self.verticalLayout_9.addLayout(self.verticalLayout_8)
        self.tabWidget.addTab(self.tab_2, "")
        self.verticalLayout.addWidget(self.tabWidget)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Close)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)
        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.retranslateUi(Dialog)
        self.tabWidget.setCurrentIndex(0)
        self.cboProfiles.setCurrentIndex(-1)
        self.buttonBox.clicked['QAbstractButton*'].connect(Dialog.closeDlg)
        self.cboProfiles.currentIndexChanged['QString'].connect(Dialog.anotherProfileChosen)
        self.chkUseCustomDeck.stateChanged['int'].connect(Dialog.chkUserCustomDeckHandler)
        self.chkKanjiLink.stateChanged['int'].connect(Dialog.chkKanjiLinkHandler)
        self.chkOnYomi.stateChanged['int'].connect(Dialog.chkOnYomiHandler)
        self.chkKunYomi.stateChanged['int'].connect(Dialog.chkKunYomiHandler)
        self.chkMemoStory.stateChanged['int'].connect(Dialog.chkMemoStoryHandler)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Anki Profile"))
        self.label_3.setText(_translate("Dialog", "Enable custom settings on this profile"))
        self.gpbKanjiData.setTitle(_translate("Dialog", "Kanji Data"))
        self.label_4.setText(_translate("Dialog", "Deck Name"))
        self.label_5.setText(_translate("Dialog", "Field with Kanji"))
        self.label_2.setText(_translate("Dialog", "Field with Meaning"))
        self.chkOnYomi.setText(_translate("Dialog", "Field with on yomi"))
        self.chkKunYomi.setText(_translate("Dialog", "Field with kun yomi"))
        self.chkMemoStory.setText(_translate("Dialog", "Field with memo story"))
        self.gpbAdvanced.setTitle(_translate("Dialog", "Advanced"))
        self.chkAlsoLoadDefaultDB.setText(_translate("Dialog", "show default values for not existing values \n"
"(no differnent stlyes will be available then)"))
        self.chkColorizeKanjis.setText(_translate("Dialog", "change style for Kanji knowledge level"))
        self.chkKanjiLink.setText(_translate("Dialog", "add link for kanji"))
        self.editKanjiLink.setPlaceholderText(_translate("Dialog", "eg: http://tangorin.com/kanji/%s"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("Dialog", "Config"))
        self.textEdit.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.15094pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt; font-weight:600; text-decoration: underline;\">Table of Content</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">- Whats this? What can I do with this?</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">- How do I use it?</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">- Option Explanations</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">- How do I change the color-settings for the Kanji?</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt; font-weight:600; text-decoration: underline;\">Whats this? What can I do with this?</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">Kanji Overlay uses a default Database for showing the meaning of the Kanjis. </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">With this, you can simply use a Deck from Anki as that Database.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt; font-weight:600; text-decoration: underline;\">How do I use it?</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">You need a Deck in the form of:</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">FrontSide: [Kanji]</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">BackSide: Meaning</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">(you don\'t need to name the fields as &quot;FrontSide&quot; and &quot;BackSide&quot;)</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8pt;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt; font-weight:600; text-decoration: underline;\">Option Explanation</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt; text-decoration: underline;\">Anki Profile</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">The Kanji overlay options you set are made for this Anki Profile. </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">If you don\'t know, what a profile is, then you probably only have one and therefore don\'t need to care about this</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt; text-decoration: underline;\">show default values for not existing values</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">If enabled, It will not only use your own deck as Kanji reference, but also the default database (if you enable this option, you don\'t have any color-overlay for unknown kanji)</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt; text-decoration: underline;\">Change style for Kanji knowledge level</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">With this option the colors of Kanjis will have three different styles for:</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">- already reviewed Kanjis</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">- Kanjis, that need to be reviewed</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">- Kanjis, that are not in the deck</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">Note: if you\'re only using the Kanji-deck as a database for kanji overlay, then you should deactivate this option. However you can change the style of the kanji</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt; font-weight:600; text-decoration: underline;\">How do I change the color-settings for the Kanji?</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">Simply via css.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">- class: </span><span style=\" font-size:8pt; font-style:italic;\">unknown </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">will change the style of values found in your deck and not yet reviewed</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">- class: </span><span style=\" font-size:8pt; font-style:italic;\">kol-missing</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">will change the style of values not found in your deck</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">- class: kol</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">will change the general style of kol and kanjis found in your deck and already reviewed</span></p></body></html>"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("Dialog", "Help - whats this?"))
