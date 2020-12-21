# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Ui_MemberWindow.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MemberWindow(object):
    def setupUi(self, MemberWindow):
        MemberWindow.setObjectName("MemberWindow")
        MemberWindow.resize(668, 380)
        self.verticalLayout = QtWidgets.QVBoxLayout(MemberWindow)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(MemberWindow)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.search_type = QtWidgets.QComboBox(MemberWindow)
        self.search_type.setObjectName("search_type")
        self.search_type.addItem("")
        self.search_type.addItem("")
        self.search_type.addItem("")
        self.search_type.addItem("")
        self.horizontalLayout.addWidget(self.search_type)
        self.search_content = QtWidgets.QLineEdit(MemberWindow)
        self.search_content.setObjectName("search_content")
        self.horizontalLayout.addWidget(self.search_content)
        self.btn_search = QtWidgets.QPushButton(MemberWindow)
        self.btn_search.setMinimumSize(QtCore.QSize(56, 17))
        self.btn_search.setMaximumSize(QtCore.QSize(56, 17))
        self.btn_search.setObjectName("btn_search")
        self.horizontalLayout.addWidget(self.btn_search)
        self.line = QtWidgets.QFrame(MemberWindow)
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.horizontalLayout.addWidget(self.line)
        self.btn_add = QtWidgets.QPushButton(MemberWindow)
        self.btn_add.setMinimumSize(QtCore.QSize(56, 17))
        self.btn_add.setMaximumSize(QtCore.QSize(56, 17))
        self.btn_add.setObjectName("btn_add")
        self.horizontalLayout.addWidget(self.btn_add)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.tableView = QtWidgets.QTableView(MemberWindow)
        self.tableView.setObjectName("tableView")
        self.verticalLayout.addWidget(self.tableView)

        self.retranslateUi(MemberWindow)
        self.btn_search.clicked.connect(MemberWindow.search)
        self.btn_add.clicked.connect(MemberWindow.add)
        self.search_content.returnPressed.connect(self.btn_search.click)
        QtCore.QMetaObject.connectSlotsByName(MemberWindow)

    def retranslateUi(self, MemberWindow):
        _translate = QtCore.QCoreApplication.translate
        MemberWindow.setWindowTitle(_translate("MemberWindow", "会员管理"))
        self.label.setText(_translate("MemberWindow", "会员管理"))
        self.search_type.setItemText(0, _translate("MemberWindow", "会员号"))
        self.search_type.setItemText(1, _translate("MemberWindow", "姓名"))
        self.search_type.setItemText(2, _translate("MemberWindow", "身份证号"))
        self.search_type.setItemText(3, _translate("MemberWindow", "手机号"))
        self.btn_search.setText(_translate("MemberWindow", "查询"))
        self.btn_add.setText(_translate("MemberWindow", "登记"))

