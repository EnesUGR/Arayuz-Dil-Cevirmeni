from os import startfile, path
import sys, webbrowser
from PySide2.QtWidgets import QMainWindow, QApplication, QFileDialog, QMessageBox
from googletrans import Translator, LANGUAGES
from threading import Thread

from AutoUpdate_module import AutoUpdateCheck_Github
from app_python import Ui_MainWindow
from langs_page import LangsPage
from msgModule import SpecialMessageBox
from Languages import app_translation_en_python, langs_page_translation_en_python



VERSION = "1.2.2"
class UI_TranslatorApp(QMainWindow):
	def __init__(self):
		super(UI_TranslatorApp, self).__init__()

		self.setLanguage(self)
		self.ui.action_selectTR.triggered.connect(lambda: self.setLanguage(cLang="tr"))
		self.ui.action_selectEN.triggered.connect(lambda: self.setLanguage(cLang="en"))

		self.fileoption = QFileDialog.Option()

		self.languagesList = []
		for x in LANGUAGES.items():
			self.languagesList.append(x)
		self.translator = Translator()

		updateCheck = AutoUpdateCheck_Github(VERSION,"Arayuz-Dil-Cevirmeni")
		print(updateCheck.result)
		if updateCheck.result["isitUptoDate"] == False and updateCheck.result["error"] == "None":
			msg = SpecialMessageBox(1,1,":/icons/img/ui-translator.ico","Arayüz Dil Çevirmeni","Versiyonunuz Güncel Değil. Lütfen Yeni Sürüm İçin Siteyi Ziyaret Edin ya da Hakkında Bölümünden İletişime Geçin.","Tamam")

		self.ui.spinBox_nowTextOrder.clear()
		self.ui.spinBox_totaTextNumber.clear()

		self.ui.toolButton_select_fromUIpath.clicked.connect(lambda: self.toolButtons('fromui'))
		self.ui.toolButton_confirmLangCodes.clicked.connect(lambda: self.toolButtons('confirmLangCodes'))
		self.ui.toolButton_select_toUIpath.clicked.connect(lambda: self.toolButtons('toui'))
		self.ui.toolButton_showLanguages.clicked.connect(lambda: LangsPage(self.languagesList).show())
		self.ui.toolButton_page2_showLanguages.clicked.connect(lambda: LangsPage(self.languagesList).show())

		self.ui.toolButton_nextPage2.clicked.connect(lambda: self.changePage("main"))
		self.ui.toolButton_nextPage1.clicked.connect(lambda: self.changePage("second"))
		self.ui.action_page.triggered.connect(lambda: self.changePage("action"))

		self.no = 0
		self.new_stringList = []
		self.ui.pushButton_nextText.clicked.connect(self.read_xml)
		self.ui.pushButton_TRANSLATE.clicked.connect(self.confirmed_translate)
		self.ui.pushButton_page2_translate.clicked.connect(self.translator_page)
		self.ui.toolButton_sendTranslator.clicked.connect(self.sendTranslator)

		self.ui.action_newTranslate.triggered.connect(self.reset_for_newTranslate)
		self.ui.action_guide.triggered.connect(lambda: webbrowser.open("https://www.enesugur.ml")) #Sonra YouTube videosu konulabilir.
		self.ui.action_about.triggered.connect(self.aboutPage)
		self.ui.action_exit.triggered.connect(lambda: quit(print("Quit")))
		

	def setLanguage(self, cLang=""):
		if path.exists("language.json") == False:
			with open("language.json","w") as f:
				f.write("tr")
				self.language = "tr"
		else:
			with open("language.json","r") as f:
				self.language = f.read()

		if self.language == "en" :
			self.ui = app_translation_en_python.Ui_MainWindow()
			self.ui.setupUi(self)
		else:
			self.ui = Ui_MainWindow()
			self.ui.setupUi(self)

		restartInfo = {"tr":"Uygulamayı yeniden başlatın.","en":"Restart the application."}
		if (cLang == "tr") or (cLang == "en"):
			with open("language.json","w") as f:
				f.write(cLang)
			self.ui.statusbar.showMessage(restartInfo[self.language],2000)


	def changePage(self, fromPage:str):
		if fromPage == "main":
			self.ui.stackedWidget.setCurrentIndex(1)
		elif fromPage == "action":
			if self.ui.stackedWidget.currentIndex() == 0:
				self.ui.stackedWidget.setCurrentIndex(1)
				self.ui.action_page.setText("Ana Sayfaya Geç")
			else:
				self.ui.stackedWidget.setCurrentIndex(0)
				self.ui.action_page.setText("Çeviri Sayfasına Geç")
		else:
			self.ui.stackedWidget.setCurrentIndex(0)


	def toolButtons(self, command:str):
		if command == "fromui":
			self.xml_file, _ = QFileDialog.getOpenFileName(self, "Tasarım Dosyasını Seçin","","UI Tasarım Dosyası (*.ui)",options=self.fileoption)
			if self.xml_file:
				self.ui.lineEdit_fromUI_path.setText(self.xml_file)
				self.ui.lineEdit_fromLangCode.setEnabled(1)
				self.ui.lineEdit_toLangCode.setEnabled(1)
				self.ui.toolButton_showLanguages.setEnabled(1)
				self.ui.toolButton_confirmLangCodes.setEnabled(1)
		if command == "confirmLangCodes":
			if self.ui.lineEdit_toLangCode.text().lower() in LANGUAGES.keys():
				print("hedef dil kodu doğru.")
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
					self.ui.toolButton_sendTranslator.setEnabled(1)
					Thread(target=self.read_xml()).start()
					self.ui.label_statusColor.setToolTip("Çevirinizi Yapabilirsiniz.")
					self.ui.lineEdit_fromLangCode.setEnabled(0)
					self.ui.lineEdit_toLangCode.setEnabled(0)
					self.ui.toolButton_confirmLangCodes.setEnabled(0)
					self.ui.statusbar.showMessage("")
			else:
				self.ui.statusbar.showMessage("Hedef dil kodunuz hatalı. Lütfen kontrol edin.",2000)
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
		self.stringList.clear()
		for i in range(1,len(data)):
			if "<string>" in data[i]:
				data[i] = data[i].replace("\n","")
				string = data[i].split(">")[1].split("</")[0]
				self.stringList.append(string)

		new_string = self.ui.plainTextEdit_toLangText.toPlainText()
		self.new_stringList.append(new_string)

		if self.no != 0:
			if self.ui.plainTextEdit_toLangText.toPlainText() == "":
				self.ui.statusbar.showMessage("Boş Geçemezsiniz.",1000)
				return None

		self.ui.spinBox_nowTextOrder.setValue(self.no+1)
		self.ui.spinBox_totaTextNumber.setValue(len(self.stringList))
		self.ui.plainTextEdit_toLangText.clear()
		self.set_plainwidgets()

		print(self.new_stringList)


	def set_plainwidgets(self):
		length_list = len(self.stringList)
		if self.no == length_list:
			self.ui.plainTextEdit_fromLangText.clear()
			self.ui.spinBox_nowTextOrder.clear()
			self.ui.pushButton_nextText.setEnabled(0)
			self.ui.toolButton_sendTranslator.setEnabled(0)
			self.set_texteditwidgets()
			return None
		print(self.no)
		self.ui.plainTextEdit_fromLangText.setPlainText(self.stringList[self.no])
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
		ctx1, n = "", 1 #çevirilmemiş metinler
		for st in self.stringList:
			ctx1 += str(n) + "◾ " + st + "\n"
			n += 1
		self.ui.textEdit_fromLangTexts.setPlainText(ctx1)

		ctx2, n = "", 1 #çevirilmiş metinler
		for st in self.new_stringList:
			if st != self.new_stringList[0]:
				ctx2 += str(n) + "◾ " + st + "\n"
				n += 1
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
			startfile("/".join(self.ui.lineEdit_toUIpath.text().split("/")[0:-1])+"/")
	

	def sendTranslator(self):
		self.ui.stackedWidget.setCurrentIndex(1)
		src_lang = self.ui.lineEdit_fromLangCode.text()
		to_lang = self.ui.lineEdit_toLangCode.text()
		text = self.ui.plainTextEdit_fromLangText.toPlainText()
		self.ui.lineEdit_page2_fromCode.setText(src_lang)
		self.ui.lineEdit_page2_toCode.setText(to_lang)
		self.ui.textEdit_page2_fromText.setText(text)
		self.translator_page()
		self.ui.textEdit_page2_toText.copy()




	def reset_for_newTranslate(self):
		self.ui.lineEdit_fromUI_path.clear()
		self.ui.lineEdit_fromLangCode.clear()
		self.ui.lineEdit_toLangCode.clear()
		self.ui.textEdit_fromLangTexts.clear()
		self.ui.textEdit_toLangTexts.clear()
		self.ui.lineEdit_fromLangCode.setEnabled(0)
		self.ui.lineEdit_toLangCode.setEnabled(0)
		self.ui.toolButton_showLanguages.setEnabled(0)
		self.ui.toolButton_confirmLangCodes.setEnabled(0)
		self.ui.lineEdit_toLangCode.setEnabled(0)
		self.ui.lineEdit_toUIpath.setEnabled(0)
		self.ui.toolButton_select_toUIpath.setEnabled(0)
		self.ui.plainTextEdit_fromLangText.setEnabled(0)
		self.ui.plainTextEdit_toLangText.setEnabled(0)
		self.ui.spinBox_nowTextOrder.setEnabled(0)
		self.ui.spinBox_totaTextNumber.setEnabled(0)
		self.ui.pushButton_nextText.setEnabled(0)
		self.ui.toolButton_sendTranslator.setEnabled(0)
		self.ui.textEdit_fromLangTexts.setEnabled(0)
		self.ui.textEdit_toLangTexts.setEnabled(0)
		self.ui.pushButton_TRANSLATE.setEnabled(0)
		self.ui.label_statusColor.setStyleSheet("""
				border-radius: 8px;
				background-color: rgb(255, 0, 0);
			""")
		self.ui.label_statusColor.setToolTip("Gerekli Bilgileri Girdikten Sonra Çeviri Yapabilirsiniz.")

		self.stringList.clear()
		self.new_stringList.clear()
		self.no = 0
		self.ui.lineEdit_toUIpath.clear()
		self.ui.plainTextEdit_fromLangText.clear()
		self.ui.plainTextEdit_toLangText.clear()
		self.ui.spinBox_nowTextOrder.clear()
		self.ui.spinBox_totaTextNumber.clear()
		self.ui.textEdit_fromLangTexts.clear()
		self.ui.textEdit_toLangTexts.clear()
	

	def translator_page(self):
		text = self.ui.textEdit_page2_fromText.toPlainText()
		src_lang = self.ui.lineEdit_page2_fromCode.text()
		lang = self.ui.lineEdit_page2_toCode.text()
		if (src_lang in LANGUAGES.keys()) and (lang in LANGUAGES.keys()):
			try:
				translation = self.translator.translate(text=text, dest=lang, src=src_lang)
				print(translation)
			except ValueError and TypeError:
				return False
			else:
				self.ui.textEdit_page2_toText.setPlainText(translation.text)
		else:
			self.ui.statusbar.showMessage("Dil Kodlarınız Doğru Değil.",1000)


	def aboutPage(self):
		html = {
		'tr' : f"""<p style="text-align: center;"><strong>Aray&uuml;z Dil &Ccedil;evirmeni Uygulaması </strong></p>
			<p style="text-align: center;"><em>Uygulama Hen&uuml;z Geliştirilme Aşamasındadır. Hataları l&uuml;tfen bildiriniz.&nbsp;</em></p>
			<p style="text-align: center;">Bu uygulama 1.0.0 s&uuml;r&uuml;m&uuml;nden itibaren &uuml;cretsiz sunulmaktadır.</p>
			<p style="text-align: center;">Uygulama ile Python'da yapacağınız programların aray&uuml;z&uuml;n&uuml; PySide2 ile QtDesigner ortamında hazırladığınız .ui/.xml dosyalarınızın ek bir dile terc&uuml;mesini ger&ccedil;ekleştirme işleminizde yardımcı olmaktadır. Kolay bir şekilde programınıza yeni diller ekleyebilirsiniz.</p>
			<p style="text-align: center;">Uygulamada oluşabiliecek hataları ve g&ouml;rd&uuml;ğ&uuml;n&uuml;z eksiklikleri site &uuml;zerinden ya da iletişim adresinden l&uuml;tfen bildiriniz.</p>
			<p style="text-align: center;"><em>Geliştirici: Enes Uğur&nbsp; &nbsp;&nbsp;</em><em>Version: {VERSION}</em></p>
			<p style="text-align: center;"><span style="text-decoration: underline;">İletişim Adresleri</span></p>
			<p style="text-align: center;"><span style="text-decoration: underline;"><a href="https://www.enesugur.ml">Web Site</a></span></p>
			<p style="text-align: center;"><span style="text-decoration: underline;"><a href="mailto:eugurx@gmail.com">Mail Adresim</a></span></p>
			<p style="text-align: center;">&nbsp;</p>""",
		'en' : f"""<p style="text-align: center;"><strong>Interface Language Translator Application</strong></p>
				<p style="text-align: center;"><em>The application is still under development. Please report</em> <em>bugs</em>.</p>
				<p style="text-align: center;">This application is available free of charge from version 1.0.0.</p>
				<p style="text-align: center;">It helps you to perform the translation of your .ui / .xml files that you have prepared in QtDesigner environment with PySide2 for the interface of the programs you will make in Python with the application. You can easily add new languages to your program.</p>
				<p style="text-align: center;">Please report the errors that may occur in the application and the deficiencies you see on the site or at the contact address.</p>
				<p style="text-align: center;"><em>Developer: Enes Uğur&nbsp; &nbsp; </em><em>Version: {VERSION}</em></p>
				<p style="text-align: center;"><span style="text-decoration: underline;">Contact Addresses</span></p>
				<p style="text-align: center;"><span style="text-decoration: underline;"><a href="https://www.enesugur.ml">Web Site</a></span></p>
				<p style="text-align: center;"><span style="text-decoration: underline;"><a href="mailto:eugurx@gmail.com">Mail Address</a></span></p>
				<p style="text-align: center;">&nbsp;</p>"""}
		title = {'tr':'Hakkında','en':'About'}
		QMessageBox.about(self, title[self.language], html[self.language])



if __name__ == '__main__':
	app = QApplication(sys.argv)
	app.setApplicationName("Arayüz Dil Çevirmeni")
	app.setApplicationDisplayName("Arayüz Dil Çevirmeni")
	app.setOrganizationName("Enes Uğur")
	app.setOrganizationDomain("https://www.enesugur.ml/")
	app.setDesktopFileName("Arayüz Dil Çevirmeni")
	app.setApplicationVersion(VERSION)
	win = UI_TranslatorApp()
	if win.language == "en":
		app.setApplicationDisplayName("Interface Language Translator")
	win.show()
	sys.exit(app.exec_())
