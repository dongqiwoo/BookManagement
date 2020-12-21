# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Ui_BorrowWindow.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_BorrowWindow(object):
    def setupUi(self, BorrowWindow):
        BorrowWindow.setObjectName("BorrowWindow")
        BorrowWindow.setWindowModality(QtCore.Qt.ApplicationModal)
        BorrowWindow.resize(288, 225)
        self.Bs_id = QtWidgets.QLineEdit(BorrowWindow)
        self.Bs_id.setGeometry(QtCore.QRect(90, 109, 151, 20))
        self.Bs_id.setObjectName("Bs_id")
        self.label_2 = QtWidgets.QLabel(BorrowWindow)
        self.label_2.setGeometry(QtCore.QRect(20, 108, 61, 20))
        self.label_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.M_id = QtWidgets.QLineEdit(BorrowWindow)
        self.M_id.setGeometry(QtCore.QRect(90, 139, 151, 20))
        self.M_id.setObjectName("M_id")
        self.label_3 = QtWidgets.QLabel(BorrowWindow)
        self.label_3.setGeometry(QtCore.QRect(40, 138, 41, 20))
        self.label_3.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_3.setObjectName("label_3")
        self.submit = QtWidgets.QPushButton(BorrowWindow)
        self.submit.setGeometry(QtCore.QRect(120, 180, 56, 17))
        self.submit.setObjectName("submit")
        self.msg = QtWidgets.QLabel(BorrowWindow)
        self.msg.setGeometry(QtCore.QRect(0, 200, 291, 20))
        self.msg.setText("")
        self.msg.setAlignment(QtCore.Qt.AlignCenter)
        self.msg.setObjectName("msg")
        self.label_4 = QtWidgets.QLabel(BorrowWindow)
        self.label_4.setGeometry(QtCore.QRect(40, 78, 41, 20))
        self.label_4.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(BorrowWindow)
        self.label_5.setGeometry(QtCore.QRect(40, 48, 41, 20))
        self.label_5.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_5.setObjectName("label_5")
        self.label = QtWidgets.QLabel(BorrowWindow)
        self.label.setGeometry(QtCore.QRect(90, 10, 121, 21))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.B_ISBN = QtWidgets.QLabel(BorrowWindow)
        self.B_ISBN.setGeometry(QtCore.QRect(90, 48, 151, 20))
        self.B_ISBN.setText("")
        self.B_ISBN.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.B_ISBN.setObjectName("B_ISBN")
        self.Bname = QtWidgets.QLabel(BorrowWindow)
        self.Bname.setGeometry(QtCore.QRect(90, 78, 151, 20))
        self.Bname.setText("")
        self.Bname.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.Bname.setObjectName("Bname")

        self.retranslateUi(BorrowWindow)
        self.submit.clicked.connect(BorrowWindow.do_submit)
        QtCore.QMetaObject.connectSlotsByName(BorrowWindow)
        BorrowWindow.setTabOrder(self.Bs_id, self.M_id)
        BorrowWindow.setTabOrder(self.M_id, self.submit)

    def retranslateUi(self, BorrowWindow):
        _translate = QtCore.QCoreApplication.translate
        BorrowWindow.setWindowTitle(_translate("BorrowWindow", "图书借阅"))
        self.label_2.setText(_translate("BorrowWindow", "图书编号："))
        self.label_3.setText(_translate("BorrowWindow", "会员号："))
        self.submit.setText(_translate("BorrowWindow", "提交"))
        self.label_4.setText(_translate("BorrowWindow", "书名："))
        self.label_5.setText(_translate("BorrowWindow", "ISBN："))
        self.label.setText(_translate("BorrowWindow", "图书借阅"))

