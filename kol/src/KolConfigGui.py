# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'kol/src/KolConfigGui.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(455, 479)
        self.verticalLayout_2 = QtGui.QVBoxLayout(Dialog)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.tabWidget = QtGui.QTabWidget(Dialog)
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        self.verticalLayout_5 = QtGui.QVBoxLayout(self.tab)
        self.verticalLayout_5.setObjectName(_fromUtf8("verticalLayout_5"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setSpacing(7)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.verticalLayout_4 = QtGui.QVBoxLayout()
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.label = QtGui.QLabel(self.tab)
        self.label.setObjectName(_fromUtf8("label"))
        self.verticalLayout_4.addWidget(self.label)
        self.label_3 = QtGui.QLabel(self.tab)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.verticalLayout_4.addWidget(self.label_3)
        self.horizontalLayout.addLayout(self.verticalLayout_4)
        self.verticalLayout_6 = QtGui.QVBoxLayout()
        self.verticalLayout_6.setObjectName(_fromUtf8("verticalLayout_6"))
        self.cboProfiles = QtGui.QComboBox(self.tab)
        self.cboProfiles.setToolTip(_fromUtf8(""))
        self.cboProfiles.setStatusTip(_fromUtf8(""))
        self.cboProfiles.setWhatsThis(_fromUtf8(""))
        self.cboProfiles.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.cboProfiles.setEditable(False)
        self.cboProfiles.setObjectName(_fromUtf8("cboProfiles"))
        self.verticalLayout_6.addWidget(self.cboProfiles)
        self.chkUseCustomDeck = QtGui.QCheckBox(self.tab)
        self.chkUseCustomDeck.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.chkUseCustomDeck.setText(_fromUtf8(""))
        self.chkUseCustomDeck.setObjectName(_fromUtf8("chkUseCustomDeck"))
        self.verticalLayout_6.addWidget(self.chkUseCustomDeck)
        self.horizontalLayout.addLayout(self.verticalLayout_6)
        self.verticalLayout_5.addLayout(self.horizontalLayout)
        self.line = QtGui.QFrame(self.tab)
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.verticalLayout_5.addWidget(self.line)
        self.gpbKanjiData = QtGui.QGroupBox(self.tab)
        self.gpbKanjiData.setEnabled(False)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.gpbKanjiData.sizePolicy().hasHeightForWidth())
        self.gpbKanjiData.setSizePolicy(sizePolicy)
        self.gpbKanjiData.setFlat(False)
        self.gpbKanjiData.setObjectName(_fromUtf8("gpbKanjiData"))
        self.verticalLayout_11 = QtGui.QVBoxLayout(self.gpbKanjiData)
        self.verticalLayout_11.setObjectName(_fromUtf8("verticalLayout_11"))
        self.horizontalLayout_6 = QtGui.QHBoxLayout()
        self.horizontalLayout_6.setObjectName(_fromUtf8("horizontalLayout_6"))
        self.verticalLayout_12 = QtGui.QVBoxLayout()
        self.verticalLayout_12.setObjectName(_fromUtf8("verticalLayout_12"))
        self.label_4 = QtGui.QLabel(self.gpbKanjiData)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.verticalLayout_12.addWidget(self.label_4)
        self.label_5 = QtGui.QLabel(self.gpbKanjiData)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.verticalLayout_12.addWidget(self.label_5)
        self.label_2 = QtGui.QLabel(self.gpbKanjiData)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.verticalLayout_12.addWidget(self.label_2)
        self.chkOnYomi = QtGui.QCheckBox(self.gpbKanjiData)
        self.chkOnYomi.setObjectName(_fromUtf8("chkOnYomi"))
        self.verticalLayout_12.addWidget(self.chkOnYomi)
        self.chkKunYomi = QtGui.QCheckBox(self.gpbKanjiData)
        self.chkKunYomi.setObjectName(_fromUtf8("chkKunYomi"))
        self.verticalLayout_12.addWidget(self.chkKunYomi)
        self.chkMemoStory = QtGui.QCheckBox(self.gpbKanjiData)
        self.chkMemoStory.setObjectName(_fromUtf8("chkMemoStory"))
        self.verticalLayout_12.addWidget(self.chkMemoStory)
        self.horizontalLayout_6.addLayout(self.verticalLayout_12)
        self.verticalLayout_13 = QtGui.QVBoxLayout()
        self.verticalLayout_13.setObjectName(_fromUtf8("verticalLayout_13"))
        self.cboCustomDeckName = QtGui.QComboBox(self.gpbKanjiData)
        self.cboCustomDeckName.setEditable(True)
        self.cboCustomDeckName.setObjectName(_fromUtf8("cboCustomDeckName"))
        self.verticalLayout_13.addWidget(self.cboCustomDeckName)
        self.cboCustomExpression = QtGui.QComboBox(self.gpbKanjiData)
        self.cboCustomExpression.setEditable(True)
        self.cboCustomExpression.setObjectName(_fromUtf8("cboCustomExpression"))
        self.verticalLayout_13.addWidget(self.cboCustomExpression)
        self.cboCustomKeyword = QtGui.QComboBox(self.gpbKanjiData)
        self.cboCustomKeyword.setEditable(True)
        self.cboCustomKeyword.setObjectName(_fromUtf8("cboCustomKeyword"))
        self.verticalLayout_13.addWidget(self.cboCustomKeyword)
        self.cboOnYomi = QtGui.QComboBox(self.gpbKanjiData)
        self.cboOnYomi.setEnabled(False)
        self.cboOnYomi.setEditable(True)
        self.cboOnYomi.setObjectName(_fromUtf8("cboOnYomi"))
        self.verticalLayout_13.addWidget(self.cboOnYomi)
        self.cboKunYomi = QtGui.QComboBox(self.gpbKanjiData)
        self.cboKunYomi.setEditable(True)
        self.cboKunYomi.setObjectName(_fromUtf8("cboKunYomi"))
        self.verticalLayout_13.addWidget(self.cboKunYomi)
        self.cboMemoStory = QtGui.QComboBox(self.gpbKanjiData)
        self.cboMemoStory.setEnabled(False)
        self.cboMemoStory.setEditable(True)
        self.cboMemoStory.setObjectName(_fromUtf8("cboMemoStory"))
        self.verticalLayout_13.addWidget(self.cboMemoStory)
        self.horizontalLayout_6.addLayout(self.verticalLayout_13)
        self.verticalLayout_11.addLayout(self.horizontalLayout_6)
        self.verticalLayout_5.addWidget(self.gpbKanjiData)
        self.gpbAdvanced = QtGui.QGroupBox(self.tab)
        self.gpbAdvanced.setEnabled(False)
        self.gpbAdvanced.setObjectName(_fromUtf8("gpbAdvanced"))
        self.verticalLayout_10 = QtGui.QVBoxLayout(self.gpbAdvanced)
        self.verticalLayout_10.setMargin(2)
        self.verticalLayout_10.setObjectName(_fromUtf8("verticalLayout_10"))
        self.verticalLayout_7 = QtGui.QVBoxLayout()
        self.verticalLayout_7.setContentsMargins(5, -1, 5, -1)
        self.verticalLayout_7.setObjectName(_fromUtf8("verticalLayout_7"))
        self.chkDisplayWithFuriganaMod = QtGui.QCheckBox(self.gpbAdvanced)
        self.chkDisplayWithFuriganaMod.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.chkDisplayWithFuriganaMod.setObjectName(_fromUtf8("chkDisplayWithFuriganaMod"))
        self.verticalLayout_7.addWidget(self.chkDisplayWithFuriganaMod)
        self.chkAlsoLoadDefaultDB = QtGui.QCheckBox(self.gpbAdvanced)
        self.chkAlsoLoadDefaultDB.setObjectName(_fromUtf8("chkAlsoLoadDefaultDB"))
        self.verticalLayout_7.addWidget(self.chkAlsoLoadDefaultDB)
        self.chkColorizeKanjis = QtGui.QCheckBox(self.gpbAdvanced)
        self.chkColorizeKanjis.setToolTip(_fromUtf8(""))
        self.chkColorizeKanjis.setObjectName(_fromUtf8("chkColorizeKanjis"))
        self.verticalLayout_7.addWidget(self.chkColorizeKanjis)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.chkKanjiLink = QtGui.QCheckBox(self.gpbAdvanced)
        self.chkKanjiLink.setMinimumSize(QtCore.QSize(150, 0))
        self.chkKanjiLink.setObjectName(_fromUtf8("chkKanjiLink"))
        self.horizontalLayout_2.addWidget(self.chkKanjiLink)
        self.editKanjiLink = QtGui.QLineEdit(self.gpbAdvanced)
        self.editKanjiLink.setEnabled(False)
        self.editKanjiLink.setObjectName(_fromUtf8("editKanjiLink"))
        self.horizontalLayout_2.addWidget(self.editKanjiLink)
        self.verticalLayout_7.addLayout(self.horizontalLayout_2)
        self.verticalLayout_10.addLayout(self.verticalLayout_7)
        self.verticalLayout_5.addWidget(self.gpbAdvanced)
        self.tabWidget.addTab(self.tab, _fromUtf8(""))
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName(_fromUtf8("tab_2"))
        self.verticalLayout_9 = QtGui.QVBoxLayout(self.tab_2)
        self.verticalLayout_9.setObjectName(_fromUtf8("verticalLayout_9"))
        self.verticalLayout_8 = QtGui.QVBoxLayout()
        self.verticalLayout_8.setObjectName(_fromUtf8("verticalLayout_8"))
        self.textEdit = QtGui.QTextEdit(self.tab_2)
        self.textEdit.setObjectName(_fromUtf8("textEdit"))
        self.verticalLayout_8.addWidget(self.textEdit)
        self.verticalLayout_9.addLayout(self.verticalLayout_8)
        self.tabWidget.addTab(self.tab_2, _fromUtf8(""))
        self.verticalLayout.addWidget(self.tabWidget)
        self.buttonBox = QtGui.QDialogButtonBox(Dialog)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Close)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.verticalLayout.addWidget(self.buttonBox)
        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.retranslateUi(Dialog)
        self.tabWidget.setCurrentIndex(0)
        self.cboProfiles.setCurrentIndex(-1)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("clicked(QAbstractButton*)")), Dialog.closeDlg)
        QtCore.QObject.connect(self.cboProfiles, QtCore.SIGNAL(_fromUtf8("currentIndexChanged(QString)")), Dialog.anotherProfileChosen)
        QtCore.QObject.connect(self.chkUseCustomDeck, QtCore.SIGNAL(_fromUtf8("stateChanged(int)")), Dialog.chkUserCustomDeckHandler)
        QtCore.QObject.connect(self.chkKanjiLink, QtCore.SIGNAL(_fromUtf8("stateChanged(int)")), Dialog.chkKanjiLinkHandler)
        QtCore.QObject.connect(self.chkOnYomi, QtCore.SIGNAL(_fromUtf8("stateChanged(int)")), Dialog.chkOnYomiHandler)
        QtCore.QObject.connect(self.chkKunYomi, QtCore.SIGNAL(_fromUtf8("stateChanged(int)")), Dialog.chkKunYomiHandler)
        QtCore.QObject.connect(self.chkMemoStory, QtCore.SIGNAL(_fromUtf8("stateChanged(int)")), Dialog.chkMemoStoryHandler)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))
        self.label.setText(_translate("Dialog", "Anki Profile", None))
        self.label_3.setText(_translate("Dialog", "Enable custom settings on this profile", None))
        self.gpbKanjiData.setTitle(_translate("Dialog", "Kanji Data", None))
        self.label_4.setText(_translate("Dialog", "Deck Name", None))
        self.label_5.setText(_translate("Dialog", "Field with Kanji", None))
        self.label_2.setText(_translate("Dialog", "Field with Meaning", None))
        self.chkOnYomi.setText(_translate("Dialog", "Field with on yomi", None))
        self.chkKunYomi.setText(_translate("Dialog", "Field with kun yomi", None))
        self.chkMemoStory.setText(_translate("Dialog", "Field with memo story", None))
        self.gpbAdvanced.setTitle(_translate("Dialog", "Advanced", None))
        self.chkDisplayWithFuriganaMod.setText(_translate("Dialog", "enable Kanji Overlay for the furigana Plugin", None))
        self.chkAlsoLoadDefaultDB.setText(_translate("Dialog", "show default values for not existing values \n"
"(no differnent stlyes will be available then)", None))
        self.chkColorizeKanjis.setText(_translate("Dialog", "change style for Kanji knowledge level", None))
        self.chkKanjiLink.setText(_translate("Dialog", "add link for kanji", None))
        self.editKanjiLink.setPlaceholderText(_translate("Dialog", "eg: http://tangorin.com/kanji/%s", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("Dialog", "Config", None))
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
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt; text-decoration: underline;\">enable Kanji Overlay for the furigana Plugin</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">{{furigana:FIELDNAME}} </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">Kanji Overlay will also be shown in that field.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">If you </span><span style=\" font-size:8pt; font-style:italic;\">don\'t</span><span style=\" font-size:8pt;\"> enable this option, then you need to write </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">{{</span><span style=\" font-size:8pt; font-weight:600;\">kol</span><span style=\" font-size:8pt;\">:FIELDNAME}}</span></p>\n"
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
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">will change the general style of kol and kanjis found in your deck and already reviewed</span></p></body></html>", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("Dialog", "Help - whats this?", None))

