from PyQt5 import QtGui, QtWidgets
from PyQt5.QtWidgets import qApp, QWidget, QDialog
from login_slots import LoginWindowSlots

class LoginWindow(QDialog):
	def __init__(self):
		super(LoginWindow, self).__init__()
		self.ui = LoginWindowSlots()
		self.ui.setupUi(self)
		self.ui.OK_Button.clicked.connect(self.login_press)
		self.ui.Cancel_Button.clicked.connect(self.cancel_press)

	def login_press(self):
		self.ui.Login()
		self.close()

	def cancel_press(self):
		self.close()

class RightClickMenu(QtWidgets.QMenu):

	def lw(self):
		self.dialog = LoginWindow()
		self.dialog.show()

	def __init__(self, parent=None):

		QtWidgets.QMenu.__init__(self, "File", parent)

		icon = QtGui.QIcon.fromTheme("view-split-left-right")
		loginAction = QtWidgets.QAction(icon, "&Login", self)

		loginAction.triggered.connect(self.lw)
		self.addAction(loginAction)

		self.addSeparator()

		icon = QtGui.QIcon.fromTheme("application-exit")
		exitAction = QtWidgets.QAction(icon, "&Exit", self)
		exitAction.triggered.connect(qApp.quit)
		self.addAction(exitAction)


class SystemTray(QtWidgets.QSystemTrayIcon):
	def __init__(self, parent=None):
		QtWidgets.QSystemTrayIcon.__init__(self, parent)
		self.setIcon(QtGui.QIcon('./picts/shg_icon.png'))

		self.menu = RightClickMenu()
		self.setContextMenu(self.menu)
