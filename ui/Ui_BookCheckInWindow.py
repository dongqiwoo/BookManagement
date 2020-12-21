# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Ui_BookCheckInWindow.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_BookCheckInWindow(object):
    def setupUi(self, BookCheckInWindow):
        BookCheckInWindow.setObjectName("BookCheckInWindow")
        BookCheckInWindow.setWindowModality(QtCore.Qt.ApplicationModal)
        BookCheckInWindow.resize(288, 162)
        self.submit = QtWidgets.QPushButton(BookCheckInWindow)
        self.submit.setGeometry(QtCore.QRect(120, 120, 56, 17))
        self.submit.setObjectName("submit")
        self.msg = QtWidgets.QLabel(BookCheckInWindow)
        self.msg.setGeometry(QtCore.QRect(0, 140, 291, 20))
        self.msg.setText("")
        self.msg.setAlignment(QtCore.Qt.AlignCenter)
        self.msg.setObjectName("msg")
        self.Bs_id = QtWidgets.QLineEdit(BookCheckInWindow)
        self.Bs_id.setGeometry(QtCore.QRect(90, 79, 151, 20))
        self.Bs_id.setObjectName("Bs_id")
        self.label_4 = QtWidgets.QLabel(BookCheckInWindow)
        self.label_4.setGeometry(QtCore.QRect(20, 78, 61, 20))
        self.label_4.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(BookCheckInWindow)
        self.label_5.setGeometry(QtCore.QRect(40, 48, 41, 20))
        self.label_5.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_5.setObjectName("label_5")
        self.B_ISBN = QtWidgets.QLineEdit(BookCheckInWindow)
        self.B_ISBN.setGeometry(QtCore.QRect(90, 49, 151, 20))
        self.B_ISBN.setReadOnly(True)
        self.B_ISBN.setObjectName("B_ISBN")
        self.label = QtWidgets.QLabel(BookCheckInWindow)
        self.label.setGeometry(QtCore.QRect(90, 10, 121, 21))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")

        self.retranslateUi(BookCheckInWindow)
        self.submit.clicked.connect(BookCheckInWindow.do_submit)
        QtCore.QMetaObject.connectSlotsByName(BookCheckInWindow)
        BookCheckInWindow.setTabOrder(self.Bs_id, self.submit)
        BookCheckInWindow.setTabOrder(self.submit, self.B_ISBN)

    def retranslateUi(self, BookCheckInWindow):
        _translate = QtCore.QCoreApplication.translate
        BookCheckInWindow.setWindowTitle(_translate("BookCheckInWindow", "图书入库"))
        self.submit.setText(_translate("BookCheckInWindow", "提交"))
        self.label_4.setText(_translate("BookCheckInWindow", "图书编号："))
        self.label_5.setText(_translate("BookCheckInWindow", "ISBN："))
        self.label.setText(_translate("BookCheckInWindow", "图书入库"))

