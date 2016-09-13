from PyQt5 import QtGui, QtWidgets

if __name__ == "__main__":

	app = QtWidgets.QApplication([])

	icon = QtGui.QIcon('picts/shg_icon.png')
	tray = QtWidgets.QSystemTrayIcon(icon)
	tray.show()

	app.exec_()