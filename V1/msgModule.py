from PySide2.QtWidgets import QMessageBox
from PySide2.QtGui import QIcon

class SpecialMessageBox:
	"""
		type -> int => OK , YES|NO , YES|NO|CANCEL (1-2-3)
		iconType -> int => 1-Information 2-Warning 3-Critical 4-Question 0-NoIcon
		winIcon -> str => "icon path"
		winTitle -> str => "title"
		text -> str => "message"
		bText -> str => "Evet,Hayır"

		buttons;
		type 1 = QMessageBox.Ok
		type 2 = QMessageBox.Yes | QMessageBox.No
		type 3 = QMessageBox.Yes | QMessageBox.No | QMessageBox.Cancel

		return self.result

	"""


	def __init__(self, type:int, iconType:int, winIcon:str, winTitle:str, text:str, bText:str):
		
		self.type = type

		if iconType == 1:
			self.iconType = QMessageBox.Information
		elif iconType == 2:
			self.iconType = QMessageBox.Warning
		elif iconType == 3:
			self.iconType = QMessageBox.Critical
		elif iconType == 4:
			self.iconType = QMessageBox.Question
		else:
			self.iconType = QMessageBox.NoIcon

		self.winIcon = QIcon(f"{winIcon}")

		self.winTitle = winTitle

		self.text = text

		self.stButtons1 = QMessageBox.Ok
		self.stButtons2 = QMessageBox.Yes | QMessageBox.No
		self.stButtons3 = QMessageBox.Yes | QMessageBox.No | QMessageBox.Cancel

		self.bText = bText.split(",")

		if self.type == 1: #Ok
			self.create1()
		elif self.type == 2: #Yes|No
			self.create2()
		elif self.type == 3: #Yes|No|Cancel
			self.create3()


	def create3(self):
		specialMessageBox = QMessageBox()
		specialMessageBox.setIcon(self.iconType)
		specialMessageBox.setWindowIcon(self.winIcon)
		specialMessageBox.setWindowTitle(self.winTitle)
		specialMessageBox.setText(self.text)
		specialMessageBox.setStandardButtons(self.stButtons3)

		b1 = specialMessageBox.button(QMessageBox.Yes)
		b1.setText(f"{self.bText[0]}")
		b2 = specialMessageBox.button(QMessageBox.No)
		b2.setText(f"{self.bText[1]}")
		b3 = specialMessageBox.button(QMessageBox.Cancel)
		b3.setText(f"{self.bText[2]}")

		self.result = specialMessageBox.exec_()

		return self.result


	def create2(self):
		specialMessageBox = QMessageBox()
		specialMessageBox.setIcon(self.iconType)
		specialMessageBox.setWindowIcon(self.winIcon)
		specialMessageBox.setWindowTitle(self.winTitle)
		specialMessageBox.setText(self.text)
		specialMessageBox.setStandardButtons(self.stButtons2)

		b1 = specialMessageBox.button(QMessageBox.Yes)
		b1.setText(f"{self.bText[0]}")
		b2 = specialMessageBox.button(QMessageBox.No)
		b2.setText(f"{self.bText[1]}")

		self.result = specialMessageBox.exec_()

		return self.result


	def create1(self):
		specialMessageBox = QMessageBox()
		specialMessageBox.setIcon(self.iconType)
		specialMessageBox.setWindowIcon(self.winIcon)
		specialMessageBox.setWindowTitle(self.winTitle)
		specialMessageBox.setText(self.text)
		specialMessageBox.setStandardButtons(self.stButtons1)

		b1 = specialMessageBox.button(QMessageBox.Ok)
		b1.setText(f"{self.bText[0]}")

		self.result = specialMessageBox.exec_()

		return self.result




#ÖRNEK KULLANIM#################################################################################
# import sys
# from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMessageBox
# from msgModule import SpecialMessageBox


# def buttonClick():
# 	msg = SpecialMessageBox(type=3,iconType=4,winIcon="@.ico",winTitle="My Window",text="Kaydetmediniz. Sonlandırmayı Onaylıyor Musunuz",
# 	bText="Kaydet,Kaydetme,İptal")

# 	if msg.result == QMessageBox.Yes:
# 		print("Kaydedildi.  [Çık]")
# 		quit()
# 	elif msg.result == QMessageBox.No:
# 		print("Kaydedilmedi.  [Çık]")
# 		quit()
# 	elif msg.result == QMessageBox.Cancel: #~escape button
# 		print("Kaydedilmedi.  [Çıkma]")


# app = QApplication(sys.argv)
# win = QWidget()
# win.setWindowTitle("msgModule Örnek Kullanım!")

# btn = QPushButton("Tıkla!",win)
# btn.move(200,100)
# btn.clicked.connect(buttonClick)

# win.show()
# sys.exit(app.exec_())
#ÖRNEK KULLANIM#################################################################################
