# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Ui_BookCheckOutWindow.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_BookCheckOutWindow(object):
    def setupUi(self, BookCheckOutWindow):
        BookCheckOutWindow.setObjectName("BookCheckOutWindow")
        BookCheckOutWindow.setWindowModality(QtCore.Qt.ApplicationModal)
        BookCheckOutWindow.resize(288, 162)
        self.submit = QtWidgets.QPushButton(BookCheckOutWindow)
        self.submit.setGeometry(QtCore.QRect(120, 102, 56, 17))
        self.submit.setObjectName("submit")
        self.msg = QtWidgets.QLabel(BookCheckOutWindow)
        self.msg.setGeometry(QtCore.QRect(0, 122, 291, 20))
        self.msg.setText("")
        self.msg.setAlignment(QtCore.Qt.AlignCenter)
        self.msg.setObjectName("msg")
        self.Bs_id = QtWidgets.QLineEdit(BookCheckOutWindow)
        self.Bs_id.setGeometry(QtCore.QRect(90, 61, 151, 20))
        self.Bs_id.setObjectName("Bs_id")
        self.label_4 = QtWidgets.QLabel(BookCheckOutWindow)
        self.label_4.setGeometry(QtCore.QRect(20, 60, 61, 20))
        self.label_4.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_4.setObjectName("label_4")
        self.label = QtWidgets.QLabel(BookCheckOutWindow)
        self.label.setGeometry(QtCore.QRect(90, 10, 121, 21))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")

        self.retranslateUi(BookCheckOutWindow)
        self.submit.clicked.connect(BookCheckOutWindow.do_submit)
        QtCore.QMetaObject.connectSlotsByName(BookCheckOutWindow)
        BookCheckOutWindow.setTabOrder(self.Bs_id, self.submit)

    def retranslateUi(self, BookCheckOutWindow):
        _translate = QtCore.QCoreApplication.translate
        BookCheckOutWindow.setWindowTitle(_translate("BookCheckOutWindow", "图书出库"))
        self.submit.setText(_translate("BookCheckOutWindow", "提交"))
        self.label_4.setText(_translate("BookCheckOutWindow", "图书编号："))
        self.label.setText(_translate("BookCheckOutWindow", "图书出库"))

