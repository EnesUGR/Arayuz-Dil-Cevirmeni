# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'app.ui'
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
        MainWindow.resize(540, 520)
        MainWindow.setMinimumSize(QSize(540, 520))
        MainWindow.setMaximumSize(QSize(540, 520))
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
        icon5 = QIcon()
        icon5.addFile(u":/icons/img/google-translate-icon.png", QSize(), QIcon.Normal, QIcon.Off)
        self.action_newTranslate.setIcon(icon5)
        self.action_guide = QAction(MainWindow)
        self.action_guide.setObjectName(u"action_guide")
        icon6 = QIcon()
        icon6.addFile(u":/icons/img/book-guide-icon.png", QSize(), QIcon.Normal, QIcon.Off)
        self.action_guide.setIcon(icon6)
        self.actionOtomatik_eviriyi_Etkinle_tir = QAction(MainWindow)
        self.actionOtomatik_eviriyi_Etkinle_tir.setObjectName(u"actionOtomatik_eviriyi_Etkinle_tir")
        self.actionOtomatik_eviriyi_Etkinle_tir.setCheckable(True)
        self.actionOtomatik_eviriyi_Etkinle_tir.setEnabled(False)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.line = QFrame(self.centralwidget)
        self.line.setObjectName(u"line")
        self.line.setGeometry(QRect(10, 120, 471, 16))
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)
        self.groupBox = QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(10, 140, 521, 331))
        self.layoutWidget = QWidget(self.groupBox)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(10, 20, 291, 291))
        self.verticalLayout_3 = QVBoxLayout(self.layoutWidget)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.plainTextEdit_fromLangText = QPlainTextEdit(self.layoutWidget)
        self.plainTextEdit_fromLangText.setObjectName(u"plainTextEdit_fromLangText")
        self.plainTextEdit_fromLangText.setEnabled(False)
        self.plainTextEdit_fromLangText.setFrameShape(QFrame.Box)
        self.plainTextEdit_fromLangText.setFrameShadow(QFrame.Plain)
        self.plainTextEdit_fromLangText.setReadOnly(True)

        self.verticalLayout_2.addWidget(self.plainTextEdit_fromLangText)

        self.line_2 = QFrame(self.layoutWidget)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.HLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_2.addWidget(self.line_2)

        self.plainTextEdit_toLangText = QPlainTextEdit(self.layoutWidget)
        self.plainTextEdit_toLangText.setObjectName(u"plainTextEdit_toLangText")
        self.plainTextEdit_toLangText.setEnabled(False)
        self.plainTextEdit_toLangText.setFrameShape(QFrame.Box)
        self.plainTextEdit_toLangText.setFrameShadow(QFrame.Plain)

        self.verticalLayout_2.addWidget(self.plainTextEdit_toLangText)


        self.verticalLayout_3.addLayout(self.verticalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.pushButton_backText = QPushButton(self.layoutWidget)
        self.pushButton_backText.setObjectName(u"pushButton_backText")
        self.pushButton_backText.setEnabled(False)

        self.horizontalLayout_3.addWidget(self.pushButton_backText)

        self.spinBox_nowTextOrder = QSpinBox(self.layoutWidget)
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

        self.label = QLabel(self.layoutWidget)
        self.label.setObjectName(u"label")
        self.label.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_3.addWidget(self.label)

        self.spinBox_totaTextNumber = QSpinBox(self.layoutWidget)
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

        self.pushButton_nextText = QPushButton(self.layoutWidget)
        self.pushButton_nextText.setObjectName(u"pushButton_nextText")
        self.pushButton_nextText.setEnabled(False)

        self.horizontalLayout_3.addWidget(self.pushButton_nextText)


        self.verticalLayout_3.addLayout(self.horizontalLayout_3)

        self.layoutWidget1 = QWidget(self.groupBox)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.layoutWidget1.setGeometry(QRect(310, 20, 201, 291))
        self.verticalLayout_4 = QVBoxLayout(self.layoutWidget1)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.textEdit_fromLangTexts = QTextEdit(self.layoutWidget1)
        self.textEdit_fromLangTexts.setObjectName(u"textEdit_fromLangTexts")
        self.textEdit_fromLangTexts.setEnabled(False)
        self.textEdit_fromLangTexts.setFrameShape(QFrame.WinPanel)
        self.textEdit_fromLangTexts.setReadOnly(True)

        self.horizontalLayout_5.addWidget(self.textEdit_fromLangTexts)

        self.textEdit_toLangTexts = QTextEdit(self.layoutWidget1)
        self.textEdit_toLangTexts.setObjectName(u"textEdit_toLangTexts")
        self.textEdit_toLangTexts.setEnabled(False)
        self.textEdit_toLangTexts.setFrameShape(QFrame.WinPanel)
        self.textEdit_toLangTexts.setReadOnly(True)

        self.horizontalLayout_5.addWidget(self.textEdit_toLangTexts)


        self.verticalLayout_4.addLayout(self.horizontalLayout_5)

        self.pushButton_TRANSLATE = QPushButton(self.layoutWidget1)
        self.pushButton_TRANSLATE.setObjectName(u"pushButton_TRANSLATE")
        self.pushButton_TRANSLATE.setEnabled(False)
        font = QFont()
        font.setFamily(u"MS Shell Dlg 2")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_TRANSLATE.setFont(font)

        self.verticalLayout_4.addWidget(self.pushButton_TRANSLATE)

        self.label_statusColor = QLabel(self.centralwidget)
        self.label_statusColor.setObjectName(u"label_statusColor")
        self.label_statusColor.setGeometry(QRect(494, 120, 16, 16))
        self.label_statusColor.setStyleSheet(u"border-radius: 8px;\n"
"color: white;\n"
"\n"
"background-color: rgb(0, 255, 0);\n"
"background-color: rgb(255, 255, 0);\n"
"background-color: rgb(255, 0, 0);")
        self.layoutWidget2 = QWidget(self.centralwidget)
        self.layoutWidget2.setObjectName(u"layoutWidget2")
        self.layoutWidget2.setGeometry(QRect(10, 10, 511, 86))
        self.verticalLayout = QVBoxLayout(self.layoutWidget2)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.lineEdit_fromUI_path = QLineEdit(self.layoutWidget2)
        self.lineEdit_fromUI_path.setObjectName(u"lineEdit_fromUI_path")
        self.lineEdit_fromUI_path.setReadOnly(True)

        self.horizontalLayout.addWidget(self.lineEdit_fromUI_path)

        self.toolButton_select_fromUIpath = QToolButton(self.layoutWidget2)
        self.toolButton_select_fromUIpath.setObjectName(u"toolButton_select_fromUIpath")

        self.horizontalLayout.addWidget(self.toolButton_select_fromUIpath)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.lineEdit_fromLangCode = QLineEdit(self.layoutWidget2)
        self.lineEdit_fromLangCode.setObjectName(u"lineEdit_fromLangCode")
        self.lineEdit_fromLangCode.setEnabled(False)
        font1 = QFont()
        font1.setFamily(u"MS Shell Dlg 2")
        font1.setPointSize(10)
        font1.setItalic(True)
        self.lineEdit_fromLangCode.setFont(font1)
        self.lineEdit_fromLangCode.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_4.addWidget(self.lineEdit_fromLangCode)

        self.lineEdit_toLangCode = QLineEdit(self.layoutWidget2)
        self.lineEdit_toLangCode.setObjectName(u"lineEdit_toLangCode")
        self.lineEdit_toLangCode.setEnabled(False)
        self.lineEdit_toLangCode.setFont(font1)
        self.lineEdit_toLangCode.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_4.addWidget(self.lineEdit_toLangCode)

        self.toolButton_confirmLangCodes = QToolButton(self.layoutWidget2)
        self.toolButton_confirmLangCodes.setObjectName(u"toolButton_confirmLangCodes")
        self.toolButton_confirmLangCodes.setEnabled(False)

        self.horizontalLayout_4.addWidget(self.toolButton_confirmLangCodes)


        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.lineEdit_toUIpath = QLineEdit(self.layoutWidget2)
        self.lineEdit_toUIpath.setObjectName(u"lineEdit_toUIpath")
        self.lineEdit_toUIpath.setEnabled(False)
        self.lineEdit_toUIpath.setReadOnly(True)

        self.horizontalLayout_2.addWidget(self.lineEdit_toUIpath)

        self.toolButton_select_toUIpath = QToolButton(self.layoutWidget2)
        self.toolButton_select_toUIpath.setObjectName(u"toolButton_select_toUIpath")
        self.toolButton_select_toUIpath.setEnabled(False)

        self.horizontalLayout_2.addWidget(self.toolButton_select_toUIpath)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 540, 21))
        self.menuMen = QMenu(self.menubar)
        self.menuMen.setObjectName(u"menuMen")
        self.menuDili_De_i_tir = QMenu(self.menuMen)
        self.menuDili_De_i_tir.setObjectName(u"menuDili_De_i_tir")
        self.menuDili_De_i_tir.setEnabled(False)
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        font2 = QFont()
        font2.setFamily(u"MS Shell Dlg 2")
        font2.setPointSize(8)
        font2.setBold(True)
        font2.setWeight(75)
        self.statusbar.setFont(font2)
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuMen.menuAction())
        self.menuMen.addAction(self.action_newTranslate)
        self.menuMen.addAction(self.menuDili_De_i_tir.menuAction())
        self.menuMen.addAction(self.actionOtomatik_eviriyi_Etkinle_tir)
        self.menuMen.addSeparator()
        self.menuMen.addAction(self.action_guide)
        self.menuMen.addAction(self.action_about)
        self.menuMen.addAction(self.action_exit)
        self.menuDili_De_i_tir.addAction(self.action_selectTR)
        self.menuDili_De_i_tir.addAction(self.action_selectEN)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Aray\u00fcz Dil \u00c7evirmeni", None))
        self.action_selectTR.setText(QCoreApplication.translate("MainWindow", u"T\u00fcrk\u00e7e", None))
        self.action_selectEN.setText(QCoreApplication.translate("MainWindow", u"\u0130ngilizce", None))
        self.action_about.setText(QCoreApplication.translate("MainWindow", u"Hakk\u0131nda", None))
        self.action_exit.setText(QCoreApplication.translate("MainWindow", u"\u00c7\u0131k\u0131\u015f", None))
        self.action_newTranslate.setText(QCoreApplication.translate("MainWindow", u"Yeni \u00c7eviri Ba\u015flat\u0131n", None))
#if QT_CONFIG(shortcut)
        self.action_newTranslate.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+R", None))
#endif // QT_CONFIG(shortcut)
        self.action_guide.setText(QCoreApplication.translate("MainWindow", u"Klavuz", None))
        self.actionOtomatik_eviriyi_Etkinle_tir.setText(QCoreApplication.translate("MainWindow", u"Otomatik \u00c7eviriyi Etkinle\u015ftir", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"\u00c7eviri", None))
#if QT_CONFIG(tooltip)
        self.plainTextEdit_fromLangText.setToolTip(QCoreApplication.translate("MainWindow", u"Aray\u00fcz\u00fcn\u00fczdeki Metinler Buraya Gelir.", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.plainTextEdit_toLangText.setToolTip(QCoreApplication.translate("MainWindow", u"G\u00f6rd\u00fc\u011f\u00fcn\u00fcz Metinin \u00c7evirisini Buraya Girin ve 'Sonraki' Butonuna Bas\u0131n.", None))
#endif // QT_CONFIG(tooltip)
        self.pushButton_backText.setText(QCoreApplication.translate("MainWindow", u"\u00d6nceki", None))
#if QT_CONFIG(tooltip)
        self.spinBox_nowTextOrder.setToolTip(QCoreApplication.translate("MainWindow", u"\u015euanki Metinin  S\u0131ras\u0131", None))
#endif // QT_CONFIG(tooltip)
        self.spinBox_nowTextOrder.setPrefix("")
        self.label.setText(QCoreApplication.translate("MainWindow", u"/", None))
#if QT_CONFIG(tooltip)
        self.spinBox_totaTextNumber.setToolTip(QCoreApplication.translate("MainWindow", u"Toplam \u00c7evirilecek Metin Say\u0131s\u0131", None))
#endif // QT_CONFIG(tooltip)
        self.spinBox_totaTextNumber.setPrefix("")
#if QT_CONFIG(tooltip)
        self.pushButton_nextText.setToolTip(QCoreApplication.translate("MainWindow", u"S\u0131radaki Metine Ge\u00e7in (Ctrl + Enter)", None))
#endif // QT_CONFIG(tooltip)
        self.pushButton_nextText.setText(QCoreApplication.translate("MainWindow", u"Sonraki", None))
#if QT_CONFIG(shortcut)
        self.pushButton_nextText.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+Return", None))
#endif // QT_CONFIG(shortcut)
#if QT_CONFIG(tooltip)
        self.textEdit_fromLangTexts.setToolTip(QCoreApplication.translate("MainWindow", u"Kaynak Dildeki Metinler", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.textEdit_toLangTexts.setToolTip(QCoreApplication.translate("MainWindow", u"Hedef Dilinizdeki Metinler", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.pushButton_TRANSLATE.setToolTip(QCoreApplication.translate("MainWindow", u"\u00c7evirme \u0130\u015flemini Ba\u015flat\u0131n. \u00c7evirilmi\u015f .ui Dosyan\u0131z Belirtilen Kay\u0131t Yolunuza Kaydedilir.", None))
#endif // QT_CONFIG(tooltip)
        self.pushButton_TRANSLATE.setText(QCoreApplication.translate("MainWindow", u"\u00c7EV\u0130R\u0130Y\u0130 BA\u015eLAT", None))
        self.label_statusColor.setText("")
#if QT_CONFIG(tooltip)
        self.lineEdit_fromUI_path.setToolTip(QCoreApplication.translate("MainWindow", u".ui Uzant\u0131l\u0131 Dosyan\u0131z\u0131 Se\u00e7in", None))
#endif // QT_CONFIG(tooltip)
        self.lineEdit_fromUI_path.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Tasar\u0131m Dosyas\u0131n\u0131 Se\u00e7in", None))
#if QT_CONFIG(tooltip)
        self.toolButton_select_fromUIpath.setToolTip(QCoreApplication.translate("MainWindow", u".ui Uzant\u0131l\u0131 Dosyan\u0131z\u0131 Se\u00e7in", None))
#endif // QT_CONFIG(tooltip)
        self.toolButton_select_fromUIpath.setText(QCoreApplication.translate("MainWindow", u"...", None))
#if QT_CONFIG(tooltip)
        self.lineEdit_fromLangCode.setToolTip(QCoreApplication.translate("MainWindow", u"Aray\u00fcz\u00fcn\u00fcz\u00fcn \u015euanki Dil Kodunuz/Uzun Halini Girin", None))
#endif // QT_CONFIG(tooltip)
        self.lineEdit_fromLangCode.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Kaynak Dil Kodu", None))
#if QT_CONFIG(tooltip)
        self.lineEdit_toLangCode.setToolTip(QCoreApplication.translate("MainWindow", u"Aray\u00fcz\u00fcn\u00fcz\u00fcn \u00c7evirilecek Yeni Dil Kodunu/Uzun Halini Girin", None))
#endif // QT_CONFIG(tooltip)
        self.lineEdit_toLangCode.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Hedef Dil Kodu", None))
#if QT_CONFIG(tooltip)
        self.toolButton_confirmLangCodes.setToolTip(QCoreApplication.translate("MainWindow", u"Yaz\u0131lan Dilleri Onaylay\u0131n.", None))
#endif // QT_CONFIG(tooltip)
        self.toolButton_confirmLangCodes.setText(QCoreApplication.translate("MainWindow", u"\u2713", None))
#if QT_CONFIG(tooltip)
        self.lineEdit_toUIpath.setToolTip(QCoreApplication.translate("MainWindow", u"Yeni Dil Tasar\u0131m\u0131 Dosyas\u0131n\u0131n Kay\u0131t Yolunu Se\u00e7in. Otomatik Doldurulmu\u015f \u015eekilde Kalmas\u0131 \u00d6nerilir.", None))
#endif // QT_CONFIG(tooltip)
        self.lineEdit_toUIpath.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Yeni Tasar\u0131m Dosya Yolu", None))
#if QT_CONFIG(tooltip)
        self.toolButton_select_toUIpath.setToolTip(QCoreApplication.translate("MainWindow", u"Yeni .ui Uzant\u0131l\u0131 Dosyan\u0131z\u0131n Kay\u0131t Yolunu Se\u00e7in", None))
#endif // QT_CONFIG(tooltip)
        self.toolButton_select_toUIpath.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.menuMen.setTitle(QCoreApplication.translate("MainWindow", u"Men\u00fc", None))
        self.menuDili_De_i_tir.setTitle(QCoreApplication.translate("MainWindow", u"Dili De\u011fi\u015ftir", None))
    # retranslateUi

