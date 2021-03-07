import sys, webbrowser
from PySide2.QtWidgets import QMainWindow, QApplication, QFileDialog, QMessageBox
from app_python import Ui_MainWindow


class UI_TranslatorApp(QMainWindow):
    def __init__(self):
        super(UI_TranslatorApp, self).__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.fileoption = QFileDialog.Option()

        self.ui.toolButton_select_fromUIpath.clicked.connect(lambda: self.toolButtons('fromui'))
        self.ui.toolButton_confirmLangCodes.clicked.connect(lambda: self.toolButtons('confirmLangCodes'))
        self.ui.toolButton_select_toUIpath.clicked.connect(lambda: self.toolButtons('toui'))

        self.no = 0
        self.new_stringList = []
        self.ui.pushButton_nextText.clicked.connect(self.read_xml)
        self.ui.pushButton_TRANSLATE.clicked.connect(self.confirmed_translate)

        self.ui.action_newTranslate.triggered.connect(self.reset_for_newTranslate)
        self.ui.action_guide.triggered.connect(lambda: webbrowser.open("https://www.enesugur.ml"))
        self.ui.action_about.triggered.connect(self.aboutPage)
        self.ui.action_exit.triggered.connect(lambda: quit(print("Enes")))


    def toolButtons(self, command:str):
        if command == "fromui":
            self.xml_file, _ = QFileDialog.getOpenFileName(self, "Tasarım Dosyasını Seçin","","UI Tasarım Dosyası (*.ui)",options=self.fileoption)
            if self.xml_file:
                self.ui.lineEdit_fromUI_path.setText(self.xml_file)
                self.ui.lineEdit_fromLangCode.setEnabled(1)
                self.ui.lineEdit_toLangCode.setEnabled(1)
                self.ui.toolButton_confirmLangCodes.setEnabled(1)
        if command == "confirmLangCodes":
            if (self.ui.lineEdit_fromLangCode.text() != "") and (self.ui.lineEdit_toLangCode.text() != ""):
                self.fromLangCode = self.ui.lineEdit_fromLangCode.text().lower()
                self.toLangCode = self.ui.lineEdit_toLangCode.text().lower()
                self.ui.lineEdit_toUIpath.setEnabled(1)
                self.ui.toolButton_select_toUIpath.setEnabled(1)
                self.new_xml_file = self.xml_file.split(".ui")[0]+f"_translation_{self.toLangCode}.ui"
                self.ui.lineEdit_toUIpath.setText(self.new_xml_file)
                self.ui.plainTextEdit_fromLangText.setEnabled(1)
                self.ui.plainTextEdit_toLangText.setEnabled(1)
                self.ui.statusbar.showMessage("Çeviri Kısmında Boş Bıraktıklarınız Kaydedilmeyecektir. Boş Bırakmanız Sırayı Karıştırır.",4000)
                self.ui.spinBox_nowTextOrder.setEnabled(1)
                self.ui.spinBox_totaTextNumber.setEnabled(1)
                self.ui.pushButton_nextText.setEnabled(1)
                self.read_xml()
                self.ui.label_statusColor.setToolTip("Çevirinizi Yapabilirsiniz.")
        if command == "toui":
            self.new_xml_file, _ = QFileDialog.getSaveFileName(self, "Kayıt Yolunu Seçin","","UI Tasarım Dosyası (*.ui)",options=self.fileoption)
            if self.new_xml_file:
                self.ui.lineEdit_toUIpath.setText(self.new_xml_file)


    def read_xml(self):
        with open(self.xml_file,"r",encoding="utf-8") as f:
            data = f.readlines()
            f.seek(0)
            self.fullData = f.read()
        self.stringList = []
        for i in range(1,len(data)):
            if "<string>" in data[i]:
                data[i] = data[i].replace("\n","")
                string = data[i].split(">")[1].split("</")[0]
                self.stringList.append(string)

        new_string = self.ui.plainTextEdit_toLangText.toPlainText()
        self.new_stringList.append(new_string)

        self.ui.spinBox_nowTextOrder.setValue(self.no+1)
        self.ui.spinBox_totaTextNumber.setValue(len(self.stringList))
        self.set_plainwidgets()

        print(self.new_stringList)
        self.ui.plainTextEdit_toLangText.clear()


    def set_plainwidgets(self):
        length_list = len(self.stringList)
        if self.no == length_list:
            self.ui.plainTextEdit_fromLangText.clear()
            self.ui.spinBox_nowTextOrder.clear()
            self.ui.pushButton_nextText.setEnabled(0)
            self.set_texteditwidgets()
            return None
        print(self.no)
        self.ui.plainTextEdit_fromLangText.setPlainText(self.stringList[self.no]) #sırayla seçip yapamıyorum. istersen listwidgetta olabilir. seçtiğinin çevrisini yazıp kaydedebilir.
        self.no += 1


    def set_texteditwidgets(self):
        self.ui.textEdit_fromLangTexts.setEnabled(1)
        self.ui.textEdit_toLangTexts.setEnabled(1)
        self.ui.pushButton_TRANSLATE.setEnabled(1)
        self.ui.label_statusColor.setStyleSheet("""
            border-radius: 8px;
            background-color: rgb(255, 255, 0);
            """)
        self.ui.label_statusColor.setToolTip("Kontrolünüzü Yapın. Hata Görürseniz Ctrl+R İle Yenileyin.")
        ctx1 = "" #çevirilmemiş metinler
        for st in self.stringList:
            ctx1 += "◾" + st + "\n"
        self.ui.textEdit_fromLangTexts.setPlainText(ctx1)

        ctx2 = "" #çevirilmiş metinler
        for st in self.new_stringList:
            if st != self.new_stringList[0]:
                ctx2 += "◾" + st + "\n"
        self.ui.textEdit_toLangTexts.setPlainText(ctx2)


    def confirmed_translate(self):
        try:
            with open(self.new_xml_file,"w",encoding="utf-8") as f:
                for j in range(0,len(self.stringList)):
                    self.fullData = self.fullData.replace(self.stringList[j],self.new_stringList[j+1])

                f.write(self.fullData)
        except Exception as err:
            self.ui.statusbar.showMessage(f"[HATA]-> {err}",8000)
        else:
            self.ui.statusbar.showMessage("İşlem Başarıyla Tamamlandı.",2500)
            self.ui.label_statusColor.setStyleSheet("""
                border-radius: 8px;
                background-color: rgb(0, 255, 0);
                """)
            self.ui.label_statusColor.setToolTip("Çeviriniz Başarıyla Tamamlandı. Ctrl+R İle Yeni Yapabilirsiniz.")


    def reset_for_newTranslate(self):
        self.ui.lineEdit_fromUI_path.clear()
        self.ui.lineEdit_fromLangCode.clear()
        self.ui.lineEdit_toLangCode.clear()
        self.ui.textEdit_fromLangTexts.clear()
        self.ui.textEdit_toLangTexts.clear()
        self.ui.lineEdit_fromLangCode.setEnabled(0)
        self.ui.lineEdit_toLangCode.setEnabled(0)
        self.ui.toolButton_confirmLangCodes.setEnabled(0)
        self.ui.lineEdit_toLangCode.setEnabled(0)
        self.ui.lineEdit_toUIpath.setEnabled(0)
        self.ui.toolButton_select_toUIpath.setEnabled(0)
        self.ui.plainTextEdit_fromLangText.setEnabled(0)
        self.ui.plainTextEdit_toLangText.setEnabled(0)
        self.ui.spinBox_nowTextOrder.setEnabled(0)
        self.ui.spinBox_totaTextNumber.setEnabled(0)
        self.ui.pushButton_nextText.setEnabled(0)
        self.ui.textEdit_fromLangTexts.setEnabled(0)
        self.ui.textEdit_toLangTexts.setEnabled(0)
        self.ui.pushButton_TRANSLATE.setEnabled(0)
        self.ui.label_statusColor.setStyleSheet("""
                border-radius: 8px;
                background-color: rgb(255, 0, 0);
            """)
        self.ui.label_statusColor.setToolTip("Gerekli Bilgileri Girdikten Sonra Çeviri Yapabilirsiniz.")


    def aboutPage(self):
        html = """<p style="text-align: center;"><strong>Aray&uuml;z Dil &Ccedil;evirmeni Uygulaması Version 1.0.0</strong></p>
            <p style="text-align: center;"><em>Uygulama Hen&uuml;z Geliştirilme Aşamasındadır. Hataları l&uuml;tfen bildiriniz.&nbsp;</em></p>
            <p style="text-align: center;">Bu uygulama 1.0.0 s&uuml;r&uuml;m&uuml;nden itibaren &uuml;cretsiz sunulmaktadır.</p>
            <p style="text-align: center;">Uygulama ile Python'da yapacağınız programların aray&uuml;z&uuml;n&uuml; PySide2 ile QtDesigner ortamında hazırladığınız .ui/.xml dosyalarınızın ek bir dile terc&uuml;mesini ger&ccedil;ekleştirme işleminizde yardımcı olmaktadır. Kolay bir şekilde programınıza yeni diller ekleyebilirsiniz.</p>
            <p style="text-align: center;">Uygulamada oluşabiliecek hataları ve g&ouml;rd&uuml;ğ&uuml;n&uuml;z eksiklikleri site &uuml;zerinden ya da iletişim adresinden l&uuml;tfen bildiriniz.</p>
            <p style="text-align: center;"><em>Geliştirici: Enes Uğur&nbsp; &nbsp;&nbsp;</em><em>Version: 1.0.0</em></p>
            <p style="text-align: center;"><span style="text-decoration: underline;">İletişim Adresleri</span></p>
            <p style="text-align: center;"><span style="text-decoration: underline;"><a href="https://www.enesugur.ml">Web Site</a></span></p>
            <p style="text-align: center;"><span style="text-decoration: underline;"><a href="mailto:eugurx@gmail.com">Mail Adresim</a></span></p>
            <p style="text-align: center;">&nbsp;</p>"""
        QMessageBox.about(self,"Arayüz Dil Çevirmeni Hakkında", html)





if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setApplicationName("Arayüz Dil Çevirmeni")
    app.setOrganizationName("Enes Uğur")
    app.setOrganizationDomain("https://www.enesugur.ml/")
    app.setApplicationVersion("1.0.0")
    win = UI_TranslatorApp()
    win.show()
    sys.exit(app.exec_())
