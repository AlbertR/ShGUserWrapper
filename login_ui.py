# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Login(object):
    def setupUi(self, Login):
        Login.setObjectName("Login")
        Login.resize(220, 119)
        Login.setMinimumSize(QtCore.QSize(220, 100))
        self.layoutWidget = QtWidgets.QWidget(Login)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 10, 196, 104))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.login = QtWidgets.QLabel(self.layoutWidget)
        self.login.setObjectName("login")
        self.horizontalLayout.addWidget(self.login)
        self.LoginEdit = QtWidgets.QLineEdit(self.layoutWidget)
        self.LoginEdit.setEnabled(True)
        self.LoginEdit.setMinimumSize(QtCore.QSize(0, 30))
        self.LoginEdit.setObjectName("LoginEdit")
        self.horizontalLayout.addWidget(self.LoginEdit)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.password = QtWidgets.QLabel(self.layoutWidget)
        self.password.setObjectName("password")
        self.horizontalLayout_2.addWidget(self.password)
        self.PasswordEdit = QtWidgets.QLineEdit(self.layoutWidget)
        self.PasswordEdit.setMinimumSize(QtCore.QSize(0, 30))
        self.PasswordEdit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.PasswordEdit.setObjectName("PasswordEdit")
        self.horizontalLayout_2.addWidget(self.PasswordEdit)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.OK_Button = QtWidgets.QPushButton(self.layoutWidget)
        self.OK_Button.setObjectName("OK_Button")
        self.horizontalLayout_3.addWidget(self.OK_Button)
        self.Cancel_Button = QtWidgets.QPushButton(self.layoutWidget)
        self.Cancel_Button.setObjectName("Cancel_Button")
        self.horizontalLayout_3.addWidget(self.Cancel_Button)
        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.retranslateUi(Login)
        QtCore.QMetaObject.connectSlotsByName(Login)

    def retranslateUi(self, Login):
        _translate = QtCore.QCoreApplication.translate
        Login.setWindowTitle(_translate("Login", "Login Window"))
        self.login.setText(_translate("Login", "Login"))
        self.password.setText(_translate("Login", "Password"))
        self.OK_Button.setText(_translate("Login", "OK"))
        self.Cancel_Button.setText(_translate("Login", "Cancel"))

