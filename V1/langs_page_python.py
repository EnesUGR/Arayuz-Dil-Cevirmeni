# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'langs_page.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import source_rc

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(380, 320)
        Dialog.setMinimumSize(QSize(380, 320))
        icon = QIcon()
        icon.addFile(u":/icons/img/ui-translator.png", QSize(), QIcon.Normal, QIcon.Off)
        Dialog.setWindowIcon(icon)
        self.verticalLayout_3 = QVBoxLayout(Dialog)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.listWidget_langs = QListWidget(Dialog)
        self.listWidget_langs.setObjectName(u"listWidget_langs")

        self.verticalLayout.addWidget(self.listWidget_langs)

        self.label_langCode = QLabel(Dialog)
        self.label_langCode.setObjectName(u"label_langCode")
        font = QFont()
        font.setFamily(u"MS Shell Dlg 2")
        font.setPointSize(15)
        self.label_langCode.setFont(font)
        self.label_langCode.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label_langCode)

        self.pushButton_closeDialog = QPushButton(Dialog)
        self.pushButton_closeDialog.setObjectName(u"pushButton_closeDialog")

        self.verticalLayout.addWidget(self.pushButton_closeDialog)


        self.verticalLayout_2.addLayout(self.verticalLayout)


        self.verticalLayout_3.addLayout(self.verticalLayout_2)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Diller", None))
        self.label_langCode.setText("")
        self.pushButton_closeDialog.setText(QCoreApplication.translate("Dialog", u"Tamam", None))
    # retranslateUi

