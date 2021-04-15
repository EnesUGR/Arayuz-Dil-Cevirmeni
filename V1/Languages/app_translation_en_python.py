# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'app_translation_en.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import source_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(680, 580)
        MainWindow.setMinimumSize(QSize(680, 580))
        MainWindow.setMaximumSize(QSize(680, 580))
        icon = QIcon()
        icon.addFile(u":/icons/img/ui-translator.ico", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.action_selectTR = QAction(MainWindow)
        self.action_selectTR.setObjectName(u"action_selectTR")
        icon1 = QIcon()
        icon1.addFile(u":/icons/img/turkey.png", QSize(), QIcon.Normal, QIcon.Off)
        self.action_selectTR.setIcon(icon1)
        self.action_selectEN = QAction(MainWindow)
        self.action_selectEN.setObjectName(u"action_selectEN")
        self.action_selectEN.setEnabled(True)
        icon2 = QIcon()
        icon2.addFile(u":/icons/img/english.png", QSize(), QIcon.Normal, QIcon.Off)
        self.action_selectEN.setIcon(icon2)
        self.action_about = QAction(MainWindow)
        self.action_about.setObjectName(u"action_about")
        icon3 = QIcon()
        icon3.addFile(u":/icons/img/information.ico", QSize(), QIcon.Normal, QIcon.Off)
        self.action_about.setIcon(icon3)
        self.action_exit = QAction(MainWindow)
        self.action_exit.setObjectName(u"action_exit")
        icon4 = QIcon()
        icon4.addFile(u":/icons/img/exit3.ico", QSize(), QIcon.Normal, QIcon.Off)
        self.action_exit.setIcon(icon4)
        self.action_newTranslate = QAction(MainWindow)
        self.action_newTranslate.setObjectName(u"action_newTranslate")
        self.action_newTranslate.setEnabled(True)
        icon5 = QIcon()
        icon5.addFile(u":/icons/img/google-translate-icon.png", QSize(), QIcon.Normal, QIcon.Off)
        self.action_newTranslate.setIcon(icon5)
        self.action_guide = QAction(MainWindow)
        self.action_guide.setObjectName(u"action_guide")
        icon6 = QIcon()
        icon6.addFile(u":/icons/img/book-guide-icon.png", QSize(), QIcon.Normal, QIcon.Off)
        self.action_guide.setIcon(icon6)
        self.action_enableAutoTranslate = QAction(MainWindow)
        self.action_enableAutoTranslate.setObjectName(u"action_enableAutoTranslate")
        self.action_enableAutoTranslate.setCheckable(True)
        self.action_enableAutoTranslate.setChecked(False)
        self.action_enableAutoTranslate.setEnabled(False)
        self.action_page = QAction(MainWindow)
        self.action_page.setObjectName(u"action_page")
        icon7 = QIcon()
        icon7.addFile(u":/icons/img/icons8_manual_page_rotation_64px.png", QSize(), QIcon.Normal, QIcon.Off)
        self.action_page.setIcon(icon7)
        self.actionVersiyon_Kontrol = QAction(MainWindow)
        self.actionVersiyon_Kontrol.setObjectName(u"actionVersiyon_Kontrol")
        self.actionVersiyon_Kontrol.setCheckable(True)
        self.actionVersiyon_Kontrol.setChecked(True)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidgetPage1 = QWidget()
        self.stackedWidgetPage1.setObjectName(u"stackedWidgetPage1")
        self.label_statusColor = QLabel(self.stackedWidgetPage1)
        self.label_statusColor.setObjectName(u"label_statusColor")
        self.label_statusColor.setGeometry(QRect(630, 119, 16, 16))
        self.label_statusColor.setStyleSheet(u"border-radius: 8px;\n"
"color: white;\n"
"\n"
"background-color: rgb(0, 255, 0);\n"
"background-color: rgb(255, 255, 0);\n"
"background-color: rgb(255, 0, 0);\n"
"")
        self.layoutWidget = QWidget(self.stackedWidgetPage1)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(9, 19, 641, 91))
        self.verticalLayout_2 = QVBoxLayout(self.layoutWidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.lineEdit_fromUI_path = QLineEdit(self.layoutWidget)
        self.lineEdit_fromUI_path.setObjectName(u"lineEdit_fromUI_path")
        self.lineEdit_fromUI_path.setReadOnly(True)

        self.horizontalLayout.addWidget(self.lineEdit_fromUI_path)

        self.toolButton_select_fromUIpath = QToolButton(self.layoutWidget)
        self.toolButton_select_fromUIpath.setObjectName(u"toolButton_select_fromUIpath")
        self.toolButton_select_fromUIpath.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout.addWidget(self.toolButton_select_fromUIpath)


        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.lineEdit_fromLangCode = QLineEdit(self.layoutWidget)
        self.lineEdit_fromLangCode.setObjectName(u"lineEdit_fromLangCode")
        self.lineEdit_fromLangCode.setEnabled(False)
        font = QFont()
        font.setFamily(u"MS Shell Dlg 2")
        font.setPointSize(10)
        font.setItalic(False)
        self.lineEdit_fromLangCode.setFont(font)
        self.lineEdit_fromLangCode.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_4.addWidget(self.lineEdit_fromLangCode)

        self.lineEdit_toLangCode = QLineEdit(self.layoutWidget)
        self.lineEdit_toLangCode.setObjectName(u"lineEdit_toLangCode")
        self.lineEdit_toLangCode.setEnabled(False)
        self.lineEdit_toLangCode.setFont(font)
        self.lineEdit_toLangCode.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_4.addWidget(self.lineEdit_toLangCode)

        self.toolButton_showLanguages = QToolButton(self.layoutWidget)
        self.toolButton_showLanguages.setObjectName(u"toolButton_showLanguages")
        self.toolButton_showLanguages.setEnabled(False)
        self.toolButton_showLanguages.setCursor(QCursor(Qt.PointingHandCursor))
        self.toolButton_showLanguages.setStyleSheet(u"")
        icon8 = QIcon()
        icon8.addFile(u":/icons/img/languages.png", QSize(), QIcon.Normal, QIcon.Off)
        self.toolButton_showLanguages.setIcon(icon8)

        self.horizontalLayout_4.addWidget(self.toolButton_showLanguages)

        self.toolButton_confirmLangCodes = QToolButton(self.layoutWidget)
        self.toolButton_confirmLangCodes.setObjectName(u"toolButton_confirmLangCodes")
        self.toolButton_confirmLangCodes.setEnabled(False)
        self.toolButton_confirmLangCodes.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout_4.addWidget(self.toolButton_confirmLangCodes)


        self.verticalLayout_2.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.lineEdit_toUIpath = QLineEdit(self.layoutWidget)
        self.lineEdit_toUIpath.setObjectName(u"lineEdit_toUIpath")
        self.lineEdit_toUIpath.setEnabled(False)
        self.lineEdit_toUIpath.setReadOnly(True)

        self.horizontalLayout_2.addWidget(self.lineEdit_toUIpath)

        self.toolButton_select_toUIpath = QToolButton(self.layoutWidget)
        self.toolButton_select_toUIpath.setObjectName(u"toolButton_select_toUIpath")
        self.toolButton_select_toUIpath.setEnabled(False)
        self.toolButton_select_toUIpath.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout_2.addWidget(self.toolButton_select_toUIpath)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        self.line = QFrame(self.stackedWidgetPage1)
        self.line.setObjectName(u"line")
        self.line.setGeometry(QRect(9, 119, 581, 16))
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)
        self.groupBox = QGroupBox(self.stackedWidgetPage1)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(9, 132, 644, 392))
        self.verticalLayout_5 = QVBoxLayout(self.groupBox)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.plainTextEdit_fromLangText = QPlainTextEdit(self.groupBox)
        self.plainTextEdit_fromLangText.setObjectName(u"plainTextEdit_fromLangText")
        self.plainTextEdit_fromLangText.setEnabled(False)
        self.plainTextEdit_fromLangText.setFrameShape(QFrame.Box)
        self.plainTextEdit_fromLangText.setFrameShadow(QFrame.Plain)
        self.plainTextEdit_fromLangText.setReadOnly(True)

        self.verticalLayout_4.addWidget(self.plainTextEdit_fromLangText)

        self.line_2 = QFrame(self.groupBox)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.HLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_4.addWidget(self.line_2)

        self.plainTextEdit_toLangText = QPlainTextEdit(self.groupBox)
        self.plainTextEdit_toLangText.setObjectName(u"plainTextEdit_toLangText")
        self.plainTextEdit_toLangText.setEnabled(False)
        self.plainTextEdit_toLangText.setFrameShape(QFrame.Box)
        self.plainTextEdit_toLangText.setFrameShadow(QFrame.Plain)

        self.verticalLayout_4.addWidget(self.plainTextEdit_toLangText)


        self.verticalLayout_3.addLayout(self.verticalLayout_4)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.pushButton_backText = QPushButton(self.groupBox)
        self.pushButton_backText.setObjectName(u"pushButton_backText")
        self.pushButton_backText.setEnabled(False)

        self.horizontalLayout_3.addWidget(self.pushButton_backText)

        self.toolButton_sendTranslator = QToolButton(self.groupBox)
        self.toolButton_sendTranslator.setObjectName(u"toolButton_sendTranslator")
        self.toolButton_sendTranslator.setEnabled(False)

        self.horizontalLayout_3.addWidget(self.toolButton_sendTranslator)

        self.spinBox_nowTextOrder = QSpinBox(self.groupBox)
        self.spinBox_nowTextOrder.setObjectName(u"spinBox_nowTextOrder")
        self.spinBox_nowTextOrder.setEnabled(False)
        self.spinBox_nowTextOrder.setStyleSheet(u"background-color: rgba(0, 0, 0, 0);\n"
"border: none;")
        self.spinBox_nowTextOrder.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_nowTextOrder.setReadOnly(True)
        self.spinBox_nowTextOrder.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.spinBox_nowTextOrder.setCorrectionMode(QAbstractSpinBox.CorrectToPreviousValue)
        self.spinBox_nowTextOrder.setMinimum(1)

        self.horizontalLayout_3.addWidget(self.spinBox_nowTextOrder)

        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")
        self.label.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_3.addWidget(self.label)

        self.spinBox_totaTextNumber = QSpinBox(self.groupBox)
        self.spinBox_totaTextNumber.setObjectName(u"spinBox_totaTextNumber")
        self.spinBox_totaTextNumber.setEnabled(False)
        self.spinBox_totaTextNumber.setStyleSheet(u"background-color: rgba(0, 0, 0, 0);\n"
"border: none;")
        self.spinBox_totaTextNumber.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.spinBox_totaTextNumber.setReadOnly(True)
        self.spinBox_totaTextNumber.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.spinBox_totaTextNumber.setCorrectionMode(QAbstractSpinBox.CorrectToPreviousValue)
        self.spinBox_totaTextNumber.setMinimum(1)

        self.horizontalLayout_3.addWidget(self.spinBox_totaTextNumber)

        self.pushButton_nextText = QPushButton(self.groupBox)
        self.pushButton_nextText.setObjectName(u"pushButton_nextText")
        self.pushButton_nextText.setEnabled(False)
        self.pushButton_nextText.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout_3.addWidget(self.pushButton_nextText)


        self.verticalLayout_3.addLayout(self.horizontalLayout_3)


        self.horizontalLayout_6.addLayout(self.verticalLayout_3)

        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.textEdit_fromLangTexts = QTextEdit(self.groupBox)
        self.textEdit_fromLangTexts.setObjectName(u"textEdit_fromLangTexts")
        self.textEdit_fromLangTexts.setEnabled(False)
        self.textEdit_fromLangTexts.setFrameShape(QFrame.WinPanel)
        self.textEdit_fromLangTexts.setReadOnly(True)

        self.horizontalLayout_5.addWidget(self.textEdit_fromLangTexts)

        self.textEdit_toLangTexts = QTextEdit(self.groupBox)
        self.textEdit_toLangTexts.setObjectName(u"textEdit_toLangTexts")
        self.textEdit_toLangTexts.setEnabled(False)
        self.textEdit_toLangTexts.setFrameShape(QFrame.WinPanel)
        self.textEdit_toLangTexts.setReadOnly(True)

        self.horizontalLayout_5.addWidget(self.textEdit_toLangTexts)


        self.verticalLayout_6.addLayout(self.horizontalLayout_5)

        self.pushButton_TRANSLATE = QPushButton(self.groupBox)
        self.pushButton_TRANSLATE.setObjectName(u"pushButton_TRANSLATE")
        self.pushButton_TRANSLATE.setEnabled(False)
        font1 = QFont()
        font1.setFamily(u"MS Shell Dlg 2")
        font1.setPointSize(10)
        font1.setBold(True)
        font1.setWeight(75)
        self.pushButton_TRANSLATE.setFont(font1)
        self.pushButton_TRANSLATE.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_6.addWidget(self.pushButton_TRANSLATE)


        self.horizontalLayout_6.addLayout(self.verticalLayout_6)


        self.verticalLayout_5.addLayout(self.horizontalLayout_6)

        self.toolButton_nextPage2 = QToolButton(self.stackedWidgetPage1)
        self.toolButton_nextPage2.setObjectName(u"toolButton_nextPage2")
        self.toolButton_nextPage2.setGeometry(QRect(600, 117, 25, 20))
        font2 = QFont()
        font2.setPointSize(9)
        font2.setBold(True)
        font2.setWeight(75)
        self.toolButton_nextPage2.setFont(font2)
        self.toolButton_nextPage2.setCursor(QCursor(Qt.PointingHandCursor))
        self.toolButton_nextPage2.setStyleSheet(u"")
        self.stackedWidget.addWidget(self.stackedWidgetPage1)
        self.stackedWidgetPage2 = QWidget()
        self.stackedWidgetPage2.setObjectName(u"stackedWidgetPage2")
        self.verticalLayout_9 = QVBoxLayout(self.stackedWidgetPage2)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_8 = QVBoxLayout()
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.lineEdit_page2_fromCode = QLineEdit(self.stackedWidgetPage2)
        self.lineEdit_page2_fromCode.setObjectName(u"lineEdit_page2_fromCode")
        self.lineEdit_page2_fromCode.setEnabled(True)
        self.lineEdit_page2_fromCode.setFont(font)
        self.lineEdit_page2_fromCode.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_7.addWidget(self.lineEdit_page2_fromCode)

        self.lineEdit_page2_toCode = QLineEdit(self.stackedWidgetPage2)
        self.lineEdit_page2_toCode.setObjectName(u"lineEdit_page2_toCode")
        self.lineEdit_page2_toCode.setEnabled(True)
        self.lineEdit_page2_toCode.setFont(font)
        self.lineEdit_page2_toCode.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_7.addWidget(self.lineEdit_page2_toCode)

        self.toolButton_page2_showLanguages = QToolButton(self.stackedWidgetPage2)
        self.toolButton_page2_showLanguages.setObjectName(u"toolButton_page2_showLanguages")
        self.toolButton_page2_showLanguages.setEnabled(True)
        self.toolButton_page2_showLanguages.setCursor(QCursor(Qt.PointingHandCursor))
        self.toolButton_page2_showLanguages.setStyleSheet(u"")
        self.toolButton_page2_showLanguages.setIcon(icon8)

        self.horizontalLayout_7.addWidget(self.toolButton_page2_showLanguages)


        self.verticalLayout_8.addLayout(self.horizontalLayout_7)

        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.textEdit_page2_fromText = QTextEdit(self.stackedWidgetPage2)
        self.textEdit_page2_fromText.setObjectName(u"textEdit_page2_fromText")
        self.textEdit_page2_fromText.setStyleSheet(u"font: 12pt \"MS Shell Dlg 2\";")

        self.verticalLayout_7.addWidget(self.textEdit_page2_fromText)

        self.textEdit_page2_toText = QTextEdit(self.stackedWidgetPage2)
        self.textEdit_page2_toText.setObjectName(u"textEdit_page2_toText")
        self.textEdit_page2_toText.setStyleSheet(u"font: 12pt \"MS Shell Dlg 2\";")

        self.verticalLayout_7.addWidget(self.textEdit_page2_toText)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.toolButton_nextPage1 = QToolButton(self.stackedWidgetPage2)
        self.toolButton_nextPage1.setObjectName(u"toolButton_nextPage1")
        self.toolButton_nextPage1.setFont(font2)
        self.toolButton_nextPage1.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout_8.addWidget(self.toolButton_nextPage1)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_2)

        self.pushButton_page2_translate = QPushButton(self.stackedWidgetPage2)
        self.pushButton_page2_translate.setObjectName(u"pushButton_page2_translate")
        font3 = QFont()
        font3.setPointSize(11)
        self.pushButton_page2_translate.setFont(font3)
        self.pushButton_page2_translate.setCursor(QCursor(Qt.PointingHandCursor))
        icon9 = QIcon()
        icon9.addFile(u":/icons/img/google_translate_96px.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_page2_translate.setIcon(icon9)
        self.pushButton_page2_translate.setIconSize(QSize(21, 21))

        self.horizontalLayout_8.addWidget(self.pushButton_page2_translate)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer)


        self.verticalLayout_7.addLayout(self.horizontalLayout_8)


        self.verticalLayout_8.addLayout(self.verticalLayout_7)


        self.verticalLayout_9.addLayout(self.verticalLayout_8)

        self.stackedWidget.addWidget(self.stackedWidgetPage2)

        self.verticalLayout.addWidget(self.stackedWidget)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 680, 21))
        self.menuMen = QMenu(self.menubar)
        self.menuMen.setObjectName(u"menuMen")
        self.menuDili_De_i_tir = QMenu(self.menuMen)
        self.menuDili_De_i_tir.setObjectName(u"menuDili_De_i_tir")
        self.menuDili_De_i_tir.setEnabled(True)
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        font4 = QFont()
        font4.setFamily(u"MS Shell Dlg 2")
        font4.setPointSize(8)
        font4.setBold(True)
        font4.setWeight(75)
        self.statusbar.setFont(font4)
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuMen.menuAction())
        self.menuMen.addAction(self.action_newTranslate)
        self.menuMen.addAction(self.menuDili_De_i_tir.menuAction())
        self.menuMen.addAction(self.action_enableAutoTranslate)
        self.menuMen.addAction(self.action_page)
        self.menuMen.addSeparator()
        self.menuMen.addAction(self.action_guide)
        self.menuMen.addAction(self.action_about)
        self.menuMen.addAction(self.action_exit)
        self.menuDili_De_i_tir.addAction(self.action_selectTR)
        self.menuDili_De_i_tir.addAction(self.action_selectEN)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle("")
        self.action_selectTR.setText(QCoreApplication.translate("MainWindow", u"Turkish", None))
        self.action_selectEN.setText(QCoreApplication.translate("MainWindow", u"English", None))
        self.action_about.setText(QCoreApplication.translate("MainWindow", u"About", None))
        self.action_exit.setText(QCoreApplication.translate("MainWindow", u"Exit", None))
        self.action_newTranslate.setText(QCoreApplication.translate("MainWindow", u"Start a New Translation", None))
#if QT_CONFIG(shortcut)
        self.action_newTranslate.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+R", None))
#endif // QT_CONFIG(shortcut)
        self.action_guide.setText(QCoreApplication.translate("MainWindow", u"Guide", None))
        self.action_enableAutoTranslate.setText(QCoreApplication.translate("MainWindow", u"Automatic Translate (BETA)", None))
#if QT_CONFIG(shortcut)
        self.action_enableAutoTranslate.setShortcut(QCoreApplication.translate("MainWindow", u"Shift+A", None))
#endif // QT_CONFIG(shortcut)
        self.action_page.setText(QCoreApplication.translate("MainWindow", u"Switch to Translate Page", None))
#if QT_CONFIG(shortcut)
        self.action_page.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+Up", None))
#endif // QT_CONFIG(shortcut)
        self.actionVersiyon_Kontrol.setText(QCoreApplication.translate("MainWindow", u"Check Version", None))
        self.label_statusColor.setText("")
#if QT_CONFIG(tooltip)
        self.lineEdit_fromUI_path.setToolTip(QCoreApplication.translate("MainWindow", u"Choose your .ui file", None))
#endif // QT_CONFIG(tooltip)
        self.lineEdit_fromUI_path.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Choose Your Design File", None))
#if QT_CONFIG(tooltip)
        self.toolButton_select_fromUIpath.setToolTip(QCoreApplication.translate("MainWindow", u"Choose your .ui file", None))
#endif // QT_CONFIG(tooltip)
        self.toolButton_select_fromUIpath.setText(QCoreApplication.translate("MainWindow", u"...", None))
#if QT_CONFIG(tooltip)
        self.lineEdit_fromLangCode.setToolTip(QCoreApplication.translate("MainWindow", u"Enter Your Current Language Code / Long Version of Your Interface", None))
#endif // QT_CONFIG(tooltip)
        self.lineEdit_fromLangCode.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Source Language Code", None))
#if QT_CONFIG(tooltip)
        self.lineEdit_toLangCode.setToolTip(QCoreApplication.translate("MainWindow", u"Enter New Language Code / Long Version of Your Interface to Translate", None))
#endif // QT_CONFIG(tooltip)
        self.lineEdit_toLangCode.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Target Language Code", None))
#if QT_CONFIG(tooltip)
        self.toolButton_showLanguages.setToolTip(QCoreApplication.translate("MainWindow", u"Show Language Codes", None))
#endif // QT_CONFIG(tooltip)
        self.toolButton_showLanguages.setText("")
#if QT_CONFIG(tooltip)
        self.toolButton_confirmLangCodes.setToolTip(QCoreApplication.translate("MainWindow", u"Confirm Languages \u200b\u200bWritten.", None))
#endif // QT_CONFIG(tooltip)
        self.toolButton_confirmLangCodes.setText(QCoreApplication.translate("MainWindow", u"\u2713", None))
#if QT_CONFIG(tooltip)
        self.lineEdit_toUIpath.setToolTip(QCoreApplication.translate("MainWindow", u"Select the Save Path of the New Language Design File. It Is Suggested To Stay Automatically Filled.", None))
#endif // QT_CONFIG(tooltip)
        self.lineEdit_toUIpath.setPlaceholderText(QCoreApplication.translate("MainWindow", u"New Design File Path", None))
#if QT_CONFIG(tooltip)
        self.toolButton_select_toUIpath.setToolTip(QCoreApplication.translate("MainWindow", u"Choose the Path to Save Your New .ui File", None))
#endif // QT_CONFIG(tooltip)
        self.toolButton_select_toUIpath.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Translate", None))
#if QT_CONFIG(tooltip)
        self.plainTextEdit_fromLangText.setToolTip(QCoreApplication.translate("MainWindow", u"The Texts in Your Interface Come Here.", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.plainTextEdit_toLangText.setToolTip(QCoreApplication.translate("MainWindow", u"G\u00f6rd\u00fc\u011f\u00fcn\u00fcz Textin Translatesini Buraya Girin ve 'Next' Butonuna Bas\u0131n.", None))
#endif // QT_CONFIG(tooltip)
        self.pushButton_backText.setText(QCoreApplication.translate("MainWindow", u"Back", None))
#if QT_CONFIG(tooltip)
        self.toolButton_sendTranslator.setToolTip(QCoreApplication.translate("MainWindow", u"Ctrl+Shift+Return", None))
#endif // QT_CONFIG(tooltip)
        self.toolButton_sendTranslator.setText(QCoreApplication.translate("MainWindow", u">>", None))
#if QT_CONFIG(shortcut)
        self.toolButton_sendTranslator.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+Shift+Return", None))
#endif // QT_CONFIG(shortcut)
#if QT_CONFIG(tooltip)
        self.spinBox_nowTextOrder.setToolTip(QCoreApplication.translate("MainWindow", u"Order of Current Text", None))
#endif // QT_CONFIG(tooltip)
        self.spinBox_nowTextOrder.setPrefix("")
        self.label.setText(QCoreApplication.translate("MainWindow", u"/", None))
#if QT_CONFIG(tooltip)
        self.spinBox_totaTextNumber.setToolTip(QCoreApplication.translate("MainWindow", u"Toplam Translatelecek Text Say\u0131s\u0131", None))
#endif // QT_CONFIG(tooltip)
        self.spinBox_totaTextNumber.setPrefix("")
#if QT_CONFIG(tooltip)
        self.pushButton_nextText.setToolTip(QCoreApplication.translate("MainWindow", u"Switch to Next Text (Ctrl + Enter)", None))
#endif // QT_CONFIG(tooltip)
        self.pushButton_nextText.setText(QCoreApplication.translate("MainWindow", u"Next", None))
#if QT_CONFIG(shortcut)
        self.pushButton_nextText.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+Return", None))
#endif // QT_CONFIG(shortcut)
#if QT_CONFIG(tooltip)
        self.textEdit_fromLangTexts.setToolTip(QCoreApplication.translate("MainWindow", u"Texts in Source Language", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.textEdit_toLangTexts.setToolTip(QCoreApplication.translate("MainWindow", u"Texts in Target  Language", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.pushButton_TRANSLATE.setToolTip(QCoreApplication.translate("MainWindow", u"Translateme \u0130\u015flemini Ba\u015flat\u0131n. Translatelmi\u015f .ui Dosyan\u0131z Belirtilen Kay\u0131t Yolunuza Kaydedilir.", None))
#endif // QT_CONFIG(tooltip)
        self.pushButton_TRANSLATE.setText(QCoreApplication.translate("MainWindow", u"START TRANSLATION", None))
#if QT_CONFIG(tooltip)
        self.toolButton_nextPage2.setToolTip(QCoreApplication.translate("MainWindow", u"Go To Other Page", None))
#endif // QT_CONFIG(tooltip)
        self.toolButton_nextPage2.setText(QCoreApplication.translate("MainWindow", u">", None))
#if QT_CONFIG(shortcut)
        self.toolButton_nextPage2.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+Right", None))
#endif // QT_CONFIG(shortcut)
#if QT_CONFIG(tooltip)
        self.lineEdit_page2_fromCode.setToolTip(QCoreApplication.translate("MainWindow", u"Enter the Language Code of Your Text.", None))
#endif // QT_CONFIG(tooltip)
        self.lineEdit_page2_fromCode.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Source Language Code", None))
#if QT_CONFIG(tooltip)
        self.lineEdit_page2_toCode.setToolTip(QCoreApplication.translate("MainWindow", u"Select the Code of the Target Language.", None))
#endif // QT_CONFIG(tooltip)
        self.lineEdit_page2_toCode.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Target Language Code", None))
#if QT_CONFIG(tooltip)
        self.toolButton_page2_showLanguages.setToolTip(QCoreApplication.translate("MainWindow", u"Show Language Codes", None))
#endif // QT_CONFIG(tooltip)
        self.toolButton_page2_showLanguages.setText("")
        self.textEdit_page2_fromText.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Text", None))
        self.textEdit_page2_toText.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Translate", None))
#if QT_CONFIG(tooltip)
        self.toolButton_nextPage1.setToolTip(QCoreApplication.translate("MainWindow", u"Go To Other Page", None))
#endif // QT_CONFIG(tooltip)
        self.toolButton_nextPage1.setText(QCoreApplication.translate("MainWindow", u"<", None))
#if QT_CONFIG(shortcut)
        self.toolButton_nextPage1.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+Left", None))
#endif // QT_CONFIG(shortcut)
        self.pushButton_page2_translate.setText(QCoreApplication.translate("MainWindow", u"Translate", None))
        self.menuMen.setTitle(QCoreApplication.translate("MainWindow", u"Menu", None))
        self.menuDili_De_i_tir.setTitle(QCoreApplication.translate("MainWindow", u"Change Language", None))
    # retranslateUi

