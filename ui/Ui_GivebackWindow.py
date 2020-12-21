# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Ui_GivebackWindow.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_GivebackWindow(object):
    def setupUi(self, GivebackWindow):
        GivebackWindow.setObjectName("GivebackWindow")
        GivebackWindow.setWindowModality(QtCore.Qt.ApplicationModal)
        GivebackWindow.resize(288, 160)
        self.Bs_id = QtWidgets.QLineEdit(GivebackWindow)
        self.Bs_id.setGeometry(QtCore.QRect(90, 61, 151, 20))
        self.Bs_id.setObjectName("Bs_id")
        self.label_2 = QtWidgets.QLabel(GivebackWindow)
        self.label_2.setGeometry(QtCore.QRect(20, 60, 61, 20))
        self.label_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.submit = QtWidgets.QPushButton(GivebackWindow)
        self.submit.setGeometry(QtCore.QRect(120, 100, 56, 17))
        self.submit.setObjectName("submit")
        self.msg = QtWidgets.QLabel(GivebackWindow)
        self.msg.setGeometry(QtCore.QRect(0, 120, 291, 20))
        self.msg.setText("")
        self.msg.setAlignment(QtCore.Qt.AlignCenter)
        self.msg.setObjectName("msg")
        self.label = QtWidgets.QLabel(GivebackWindow)
        self.label.setGeometry(QtCore.QRect(90, 10, 121, 21))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")

        self.retranslateUi(GivebackWindow)
        self.submit.clicked.connect(GivebackWindow.do_submit)
        QtCore.QMetaObject.connectSlotsByName(GivebackWindow)
        GivebackWindow.setTabOrder(self.Bs_id, self.submit)

    def retranslateUi(self, GivebackWindow):
        _translate = QtCore.QCoreApplication.translate
        GivebackWindow.setWindowTitle(_translate("GivebackWindow", "图书归还"))
        self.label_2.setText(_translate("GivebackWindow", "图书编号："))
        self.submit.setText(_translate("GivebackWindow", "提交"))
        self.label.setText(_translate("GivebackWindow", "图书归还"))

