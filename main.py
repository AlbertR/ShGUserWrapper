import sys
from PyQt5 import QtGui, QtWidgets
from tray import SystemTray

def main():
	app = QtWidgets.QApplication([])
	app.setQuitOnLastWindowClosed(False)
	trayIcon = SystemTray()
	trayIcon.show()

	app.exec_()

if __name__ == "__main__":
	main()