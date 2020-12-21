from PyQt5 import QtCore, QtGui, QtWidgets
from Database import Database
from ui.Ui_CheckStockWindow import Ui_CheckStockWindow


class CheckStockWindow(QtWidgets.QWidget, Ui_CheckStockWindow):

    def __init__(self, *args, **kwargs):
        super(CheckStockWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)
        self.B_ISBN = None

    def search(self):
        """
        图书搜索
        :return:
        """
        if self.B_ISBN is None:
            sql_str = "select * from bookstock"
        else:
            sql_str = "select * from bookstock where B_ISBN = '%s'" % self.B_ISBN

        # 实例化数据库类对象
        db = Database()
        # 执行查询语句，并返回全部结果，保存到数组中
        book_list = db.query(sql_str).fetchall()

        # 设置model和表头
        self.model = QtGui.QStandardItemModel(0, 6)
        self.model.setHorizontalHeaderLabels(['图书编号', 'ISBN', '入库日期', '图书状态', '借阅会员号', '借阅日期'])
        self.tableView.setModel(self.model)
        self.tableView.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)  # 设置表格不允许编辑
        self.tableView.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)   # 设置选中模式为选中整行
        self.tableView.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)  # 设置选中模式为单选
        self.tableView.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
        # 显示表格内容
        idx = 0
        for bk in book_list:
            self.model.setItem(idx, 0, QtGui.QStandardItem(bk[0]))
            self.model.setItem(idx, 1, QtGui.QStandardItem(bk[1]))
            self.model.setItem(idx, 2, QtGui.QStandardItem(bk[2]))
            self.model.setItem(idx, 3, QtGui.QStandardItem(bk[3]))
            self.model.setItem(idx, 4, QtGui.QStandardItem(bk[4]))
            self.model.setItem(idx, 5, QtGui.QStandardItem(bk[5]))

            idx += 1
