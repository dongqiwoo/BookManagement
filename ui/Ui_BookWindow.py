# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Ui_BookWindow.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_BookWindow(object):
    def setupUi(self, BookWindow):
        BookWindow.setObjectName("BookWindow")
        BookWindow.resize(668, 379)
        self.centralwidget = QtWidgets.QWidget(BookWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.search_type = QtWidgets.QComboBox(self.centralwidget)
        self.search_type.setObjectName("search_type")
        self.search_type.addItem("")
        self.search_type.addItem("")
        self.search_type.addItem("")
        self.search_type.addItem("")
        self.horizontalLayout.addWidget(self.search_type)
        self.search_content = QtWidgets.QLineEdit(self.centralwidget)
        self.search_content.setMinimumSize(QtCore.QSize(100, 0))
        self.search_content.setObjectName("search_content")
        self.horizontalLayout.addWidget(self.search_content)
        self.btn_search = QtWidgets.QPushButton(self.centralwidget)
        self.btn_search.setMinimumSize(QtCore.QSize(16, 17))
        self.btn_search.setMaximumSize(QtCore.QSize(56, 17))
        self.btn_search.setObjectName("btn_search")
        self.horizontalLayout.addWidget(self.btn_search)
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.horizontalLayout.addWidget(self.line_2)
        self.btn_add = QtWidgets.QPushButton(self.centralwidget)
        self.btn_add.setMinimumSize(QtCore.QSize(56, 17))
        self.btn_add.setMaximumSize(QtCore.QSize(56, 17))
        self.btn_add.setObjectName("btn_add")
        self.horizontalLayout.addWidget(self.btn_add)
        self.btn_in_2 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_in_2.setMinimumSize(QtCore.QSize(56, 17))
        self.btn_in_2.setMaximumSize(QtCore.QSize(56, 17))
        self.btn_in_2.setObjectName("btn_in_2")
        self.horizontalLayout.addWidget(self.btn_in_2)
        self.line_3 = QtWidgets.QFrame(self.centralwidget)
        self.line_3.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.horizontalLayout.addWidget(self.line_3)
        self.btn_in = QtWidgets.QPushButton(self.centralwidget)
        self.btn_in.setMinimumSize(QtCore.QSize(56, 17))
        self.btn_in.setMaximumSize(QtCore.QSize(56, 17))
        self.btn_in.setObjectName("btn_in")
        self.horizontalLayout.addWidget(self.btn_in)
        self.btn_out = QtWidgets.QPushButton(self.centralwidget)
        self.btn_out.setMinimumSize(QtCore.QSize(56, 17))
        self.btn_out.setMaximumSize(QtCore.QSize(56, 17))
        self.btn_out.setObjectName("btn_out")
        self.horizontalLayout.addWidget(self.btn_out)
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.horizontalLayout.addWidget(self.line)
        self.btn_borrow = QtWidgets.QPushButton(self.centralwidget)
        self.btn_borrow.setMinimumSize(QtCore.QSize(56, 17))
        self.btn_borrow.setMaximumSize(QtCore.QSize(56, 17))
        self.btn_borrow.setObjectName("btn_borrow")
        self.horizontalLayout.addWidget(self.btn_borrow)
        self.btn_giveback = QtWidgets.QPushButton(self.centralwidget)
        self.btn_giveback.setMinimumSize(QtCore.QSize(56, 17))
        self.btn_giveback.setMaximumSize(QtCore.QSize(56, 17))
        self.btn_giveback.setObjectName("btn_giveback")
        self.horizontalLayout.addWidget(self.btn_giveback)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.tableView = QtWidgets.QTableView(self.centralwidget)
        self.tableView.setObjectName("tableView")
        self.verticalLayout.addWidget(self.tableView)
        BookWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(BookWindow)
        self.btn_search.clicked.connect(BookWindow.search)
        self.btn_add.clicked.connect(BookWindow.add)
        self.btn_in.clicked.connect(BookWindow.check_in)
        self.btn_out.clicked.connect(BookWindow.check_out)
        self.btn_borrow.clicked.connect(BookWindow.borrow)
        self.btn_giveback.clicked.connect(BookWindow.giveback)
        self.btn_in_2.clicked.connect(BookWindow.check_stock)
        self.search_content.returnPressed.connect(self.btn_search.click)
        QtCore.QMetaObject.connectSlotsByName(BookWindow)

    def retranslateUi(self, BookWindow):
        _translate = QtCore.QCoreApplication.translate
        BookWindow.setWindowTitle(_translate("BookWindow", "图书管理"))
        self.label.setText(_translate("BookWindow", "图书管理"))
        self.search_type.setItemText(0, _translate("BookWindow", "书名"))
        self.search_type.setItemText(1, _translate("BookWindow", "作者"))
        self.search_type.setItemText(2, _translate("BookWindow", "出版社"))
        self.search_type.setItemText(3, _translate("BookWindow", "所属类别"))
        self.btn_search.setText(_translate("BookWindow", "查询"))
        self.btn_add.setText(_translate("BookWindow", "图书登记"))
        self.btn_in_2.setText(_translate("BookWindow", "查询库存"))
        self.btn_in.setText(_translate("BookWindow", "入库"))
        self.btn_out.setText(_translate("BookWindow", "出库"))
        self.btn_borrow.setText(_translate("BookWindow", "借阅"))
        self.btn_giveback.setText(_translate("BookWindow", "归还"))

