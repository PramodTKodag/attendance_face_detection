from PyQt5.QtWidgets import QApplication, QDialog, QErrorMessage
from PyQt5.QtCore import pyqtSlot
from PyQt5.uic import loadUi

from models import Camera
# from views import StartWindow

import sys


class RegisterStudent(QDialog):
	
	def __init__(self, start_window):
		super().__init__()
		self.main_window = start_window
		loadUi('views/student_register.ui', self)
		self.accepted.connect(self.accept)
		self.rejected.connect(self.reject)

	def accept(self):
		name = self.textEdit.toPlainText()
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