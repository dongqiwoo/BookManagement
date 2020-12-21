# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Ui_LoginWindow.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_LoginWindow(object):
    def setupUi(self, LoginWindow):
        LoginWindow.setObjectName("LoginWindow")
        LoginWindow.setWindowModality(QtCore.Qt.ApplicationModal)
        LoginWindow.resize(258, 182)
        self.username = QtWidgets.QLineEdit(LoginWindow)
        self.username.setGeometry(QtCore.QRect(90, 60, 113, 20))
        self.username.setObjectName("username")
        self.label = QtWidgets.QLabel(LoginWindow)
        self.label.setGeometry(QtCore.QRect(70, 20, 111, 21))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(LoginWindow)
        self.label_2.setGeometry(QtCore.QRect(50, 59, 41, 20))
        self.label_2.setObjectName("label_2")
        self.password = QtWidgets.QLineEdit(LoginWindow)
        self.password.setGeometry(QtCore.QRect(90, 90, 113, 20))
        self.password.setMaxLength(20)
        self.password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.password.setObjectName("password")
        self.label_3 = QtWidgets.QLabel(LoginWindow)
        self.label_3.setGeometry(QtCore.QRect(50, 89, 41, 20))
        self.label_3.setObjectName("label_3")
        self.submit = QtWidgets.QPushButton(LoginWindow)
        self.submit.setGeometry(QtCore.QRect(100, 140, 56, 17))
        self.submit.setObjectName("submit")
        self.msg = QtWidgets.QLabel(LoginWindow)
        self.msg.setGeometry(QtCore.QRect(50, 110, 151, 20))
        self.msg.setText("")
        self.msg.setObjectName("msg")

        self.retranslateUi(LoginWindow)
        self.submit.clicked.connect(LoginWindow.login)
        QtCore.QMetaObject.connectSlotsByName(LoginWindow)

    def retranslateUi(self, LoginWindow):
        _translate = QtCore.QCoreApplication.translate
        LoginWindow.setWindowTitle(_translate("LoginWindow", "登录"))
        self.label.setText(_translate("LoginWindow", "图书借阅管理系统"))
        self.label_2.setText(_translate("LoginWindow", "用户名："))
        self.label_3.setText(_translate("LoginWindow", "密  码："))
        self.submit.setText(_translate("LoginWindow", "登录"))

