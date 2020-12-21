from PyQt5 import QtCore, QtGui, QtWidgets
from Database import Database
from ui.Ui_MemberWindow import Ui_MemberWindow


class MemberWindow(QtWidgets.QWidget, Ui_MemberWindow):

    def __init__(self):
        super(MemberWindow, self).__init__()
        self.setupUi(self)
        self.model = None
        self.init_ui()

    def init_ui(self):
        self.btn_add.setVisible(False)  # 暂未实现登记功能

    def search(self):
        """
        图书搜索
        :return:
        """
        sql_str = "select M_id, Mname, Msex, M_idcard, Mtel, Mstate, M_regist_date, M_legal_date from member"

        # 获取界面上输入的值
        search_type = self.search_type.currentText()
        search_content = self.search_content.text()

        # 根据输入情况，组查询条件语句
        # 当输入查询内容为空时，不设查询条件，查询全部数据
        if search_content is not None and len(search_content) > 0:
            if search_type == "会员号":
                condition_str = "M_id = '{}'".format(search_content)
            elif search_type == "姓名":
                condition_str = "Mname like '%{}%'".format(search_content)
            elif search_type == "身份证号":
                condition_str = "M_idcard = '{}'".format(search_content)
            elif search_type == "手机号码":
                condition_str = "Mtel = '{}'".format(search_content)

            sql_str = sql_str + " where " + condition_str

        # 实例化数据库类对象
        db = Database()
        # 执行查询语句，并返回全部结果，保存到数组中
        book_list = db.query(sql_str).fetchall()

        # 设置model和表头
        self.model = QtGui.QStandardItemModel(0, 8)
        self.model.setHorizontalHeaderLabels(['会员号', '姓名', '性别', '身份证号', '手机号', '会员状态', '注册日期', '有效日期'])
        self.tableView.setModel(self.model)
        self.tableView.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)  # 设置表格不允许编辑
        self.tableView.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)   # 设置选中模式为选中整行
        self.tableView.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)  # 设置选中模式为单选
        # 显示表格内容
        idx = 0
        for bk in book_list:
            self.model.setItem(idx, 0, QtGui.QStandardItem(bk[0]))
            self.model.setItem(idx, 1, QtGui.QStandardItem(bk[1]))
            self.model.setItem(idx, 2, QtGui.QStandardItem(bk[2]))
            self.model.setItem(idx, 3, QtGui.QStandardItem(bk[3]))
            self.model.setItem(idx, 4, QtGui.QStandardItem(bk[4]))
            self.model.setItem(idx, 5, QtGui.QStandardItem(bk[5]))
            self.model.setItem(idx, 6, QtGui.QStandardItem(bk[6]))
            self.model.setItem(idx, 7, QtGui.QStandardItem(bk[7]))

            idx += 1

    def add(self):
        """
        图书登记
        :return:
        """
        pass
