from PyQt5 import QtGui, QtWidgets
from Database import Database
from ui.Ui_BookWindow import Ui_BookWindow
from form.BookAddWindow import BookAddWindow
from form.CheckStockWindow import CheckStockWindow
from form.BookCheckInWindow import BookCheckInWindow
from form.BookCheckOutWindow import BookCheckOutWindow
from form.BorrowWindow import BorrowWindow
from form.GivebackWindow import GivebackWindow


class BookWindow(QtWidgets.QMainWindow, Ui_BookWindow):

    def __init__(self, *args, **kwargs):
        super(BookWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)
        self.model = None
        self.book_add_window = BookAddWindow()
        self.check_stock_window = CheckStockWindow()
        self.book_check_in_window = BookCheckInWindow()
        self.book_check_out_window = BookCheckOutWindow()
        self.borrow_window = BorrowWindow()
        self.giveback_window = GivebackWindow()

    def search(self):
        """
        图书搜索
        :return:
        """
        sql_str = "select * from book"

        # 获取界面上输入的值
        search_type = self.search_type.currentText()
        search_content = self.search_content.text()

        # 根据输入情况，组查询条件语句
        # 当输入查询内容为空时，不设查询条件，查询全部数据
        if search_content is not None and len(search_content) > 0:
            if search_type == "书名":
                condition_str = "Bname like '%{}%'".format(search_content)
            elif search_type == "出版社":
                condition_str = "Bpress like '%{}%'".format(search_content)
            elif search_type == "作者":
                condition_str = "Bauthor like '%{}%'".format(search_content)
            elif search_type == "所属类别":
                condition_str = "Btype = '{}'".format(search_content)

            sql_str = sql_str + " where " + condition_str

        # 实例化数据库类对象
        db = Database()
        # 执行查询语句，并返回全部结果，保存到数组中
        book_list = db.query(sql_str).fetchall()

        # 设置model和表头
        self.model = QtGui.QStandardItemModel(0, 8)
        self.model.setHorizontalHeaderLabels(['ISBN', '书名', '出版社', '作者', '所属类别', '位置', '总数量', '在馆数量'])
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

            # 查询总数量，在馆数量
            # 这不是一种好的实现方式，要学习一下SQL关联查询来实现
            db = Database()
            sql_str = "select count(*) from bookstock where B_ISBN = '%s'" % bk[0]
            cnt1 = db.query(sql_str).fetchone()

            sql_str = "select count(*) from bookstock where B_ISBN = '%s' and Bstate = '在馆'" % bk[0]
            cnt2 = db.query(sql_str).fetchone()

            # cnt1、cnt2从数据库取出来是个元祖，值是int，显示时要取出第1个值，并转成字符型
            self.model.setItem(idx, 6, QtGui.QStandardItem(str(cnt1[0])))
            self.model.setItem(idx, 7, QtGui.QStandardItem(str(cnt2[0])))

            idx += 1

    def add(self):
        """
        图书登记
        :return:
        """
        self.book_add_window.show()  # 显示图书登记窗口

    def check_in(self):
        """
        图书入库
        :return:
        """
        # 获取当前选中的图书，如果没有选中任何图书，那么弹出提示框，否则，显示图书入库窗口
        row = self.tableView.currentIndex().row()  # 当前选中的行数（从0开始）
        if self.model is not None and row >= 0:  # 未查询或查询无数据时，无法选中某一行
            index = self.model.index(row, 0)  # 选中行第一列的索引号，第1列为isbn
            book_isbn = self.model.data(index)  # 获取isbn的值

            # 将ISBN填到入库窗口的字段中
            self.book_check_in_window.B_ISBN.setText(book_isbn)
            # 显示入库窗口
            self.book_check_in_window.show()
        else:
            QtWidgets.QMessageBox.information(self, "提示", "请先选中图书，再进行操作！", QtWidgets.QMessageBox.Yes)

    def check_stock(self):
        """
        查询库存
        :return:
        """
        # 获取当前选中的图书，如果没有选中任何图书，那么弹出提示框，否则，显示图书入库窗口
        row = self.tableView.currentIndex().row()  # 当前选中的行数（从0开始）
        if self.model is not None and row >= 0:  # 未查询或查询无数据时，无法选中某一行
            index = self.model.index(row, 0)  # 选中行第一列的索引号，第1列为isbn
            book_isbn = self.model.data(index)  # 获取isbn的值

            # 如果选中了某一行，则查询该书的库存，否则显示全部库存记录
            self.check_stock_window.B_ISBN = book_isbn

        self.check_stock_window.search()
        self.check_stock_window.show()

    def check_out(self):
        """
        图书出库
        :return:
        """
        self.book_check_out_window.show()  # 显示出库窗口

    def borrow(self):
        """
        借阅
        :return:
        """

        # 获取当前选中的图书，如果没有选中任何图书，那么弹出提示框，否则，显示图书入库窗口
        row = self.tableView.currentIndex().row()  # 当前选中的行数（从0开始）
        if self.model is not None and row >= 0:  # 未查询或查询无数据时，无法选中某一行
            index = self.model.index(row, 0)  # 选中行第一列的索引号，第1列为isbn
            book_isbn = self.model.data(index)  # 获取isbn的值

            index = self.model.index(row, 1)
            book_name = self.model.data(index)

            # 将ISBN填到入库窗口的字段中
            self.borrow_window.B_ISBN.setText(book_isbn)
            self.borrow_window.Bname.setText(book_name)
            self.borrow_window.show()
        else:
            QtWidgets.QMessageBox.information(self, "提示", "请先选中图书，再进行操作！", QtWidgets.QMessageBox.Yes)

    def giveback(self):
        """
        归还
        :return:
        """
        self.giveback_window.show()  # 显示出库窗口
