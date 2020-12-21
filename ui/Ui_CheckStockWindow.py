# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Ui_CheckStockWindow.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_CheckStockWindow(object):
    def setupUi(self, CheckStockWindow):
        CheckStockWindow.setObjectName("CheckStockWindow")
        CheckStockWindow.resize(629, 290)
        self.verticalLayout = QtWidgets.QVBoxLayout(CheckStockWindow)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(CheckStockWindow)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.tableView = QtWidgets.QTableView(CheckStockWindow)
        self.tableView.setObjectName("tableView")
        self.verticalLayout.addWidget(self.tableView)

        self.retranslateUi(CheckStockWindow)
        QtCore.QMetaObject.connectSlotsByName(CheckStockWindow)

    def retranslateUi(self, CheckStockWindow):
        _translate = QtCore.QCoreApplication.translate
        CheckStockWindow.setWindowTitle(_translate("CheckStockWindow", "查询库存"))
        self.label.setText(_translate("CheckStockWindow", "库存信息"))

