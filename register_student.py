from PyQt5.QtWidgets import QApplication, QDialog, QErrorMessage
from PyQt5.QtCore import pyqtSlot
from PyQt5.uic import loadUi

from models import Camera
# from views import StartWindow

import sys

from datetime import datetime
from pytz import timezone

import mysql.connector
connn = mysql.connector.connect(user='root',password='root',host='localhost',port='3306',database='attendence_system')


class RegisterStudent(QDialog):
	
	def __init__(self, start_window):
		super().__init__()
		self.main_window = start_window
		loadUi('views/student_register.ui', self)
		self.accepted.connect(self.accept)
		self.rejected.connect(self.reject)

	def accept(self):
		name = self.textEdit.toPlainText()
		print(str(name))

		try:

			format = "%Y-%m-%d %H:%M:%S"
			# Current time in UTC
			abcdef = datetime.now()
			now_utc = datetime.now(timezone('UTC'))
			now_asia = now_utc.astimezone(timezone('Asia/Kolkata'))
			add_time = now_asia.strftime(format)

			abcdef = datetime.strptime(add_time, format)



			cur = connn.cursor()
			cur.execute("INSERT into user_details(USERNAME, FIRST_NAME) values('%s', '%s', '%s')"%(name, name))
			print("Inserted")

			cur.close()
			connn.commit()
			
		except Exception as r:
			print(str(r))

		if name:
			self.main_window.take_photo_sample(name)
			self.hide()
			self.main_window.show()

		else:
			error_dialog = QErrorMessage(self)
			error_dialog.showMessage('Please enter student name')


	def reject(self):
		camera = Camera(0)
		self.hide()
		self.main_window.show()
		
if __name__ == "__main__":
	app = QApplication([])
	dialog = RegisterStudent()
	dialog.show()
	app.exit(dialog.exec_())