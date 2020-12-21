from PyQt5 import QtCore, QtGui, QtWidgets
from ui.Ui_BorrowWindow import Ui_BorrowWindow
from Database import Database
import datetime
import Global


class BorrowWindow(QtWidgets.QMainWindow, Ui_BorrowWindow):

    def __init__(self, *args, **kwargs):
        super(BorrowWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)
        self.init_ui()

    def init_ui(self):
        # 不允许拉伸、最大化
        self.setFixedSize(self.width(), self.height())

    def clear(self):
        self.B_ISBN.setText("")
        self.Bname.setText("")
        self.Bs_id.setText("")
        self.M_id.setText("")
        self.msg.setText("")

    def do_submit(self):

        B_ISBN = self.B_ISBN.text()
        Bname = self.Bname.text()
        Bs_id = self.Bs_id.text()
        M_id = self.M_id.text()

        if len(Bs_id.strip()) < 1:
            self.msg.setText("图书编号不能为空！")
            return

        if len(M_id.strip()) < 1:
            self.msg.setText("会员号不能为空！")
            return

        # 查询是否有该图书
        sql_str = "select * from bookstock where Bs_id = '%s';" % Bs_id
        db = Database()
        book = db.query(sql_str).fetchone()
        if book is None:
            QtWidgets.QMessageBox.information(self, "提示", "不存在该编号的图书！", QtWidgets.QMessageBox.Yes)
            return

        # 查询是否有该会员
        sql_str = "select * from member where M_id = '%s';" % M_id
        db = Database()
        member = db.query(sql_str).fetchone()
        if member is None:
            QtWidgets.QMessageBox.information(self, "提示", "不存在该会员！", QtWidgets.QMessageBox.Yes)
            return

        # 准备登记库存信息SQL
        now_time = datetime.datetime.now()
        borrow_date = now_time.strftime('%Y-%m-%d')
        sql_str1 = "update bookstock set Bstate = '借出', M_id = '%s', borrow_date = '%s' where Bs_id = '%s';"\
                   % (M_id, borrow_date, Bs_id)

        # 准备登记租借登记表SQL
        bR_id = now_time.strftime('%Y%m%d%H%M%S%f')  # 流水编号
        C_id = Global.C_ID  # 员工号
        B_action = "租借"  # 动作
        Bdate = now_time.strftime('%Y-%m-%d')

        sql_str2 = "insert into borrow_regist (bR_id, M_id, Bs_id, C_id, B_action, Bdate) " \
                   "values ('%s', '%s', '%s', '%s', '%s', '%s');" % (bR_id, M_id, Bs_id, C_id, B_action, Bdate)

        # 执行SQL
        try:
            db.update(sql_str1)
            db.update(sql_str2)
        except Exception as e:
            self.msg.setText("借阅失败！{}".format(str(e)))
            return

        # SQL执行成功
        self.hide()
        self.clear()
        QtWidgets.QMessageBox.information(self, "提示", "借阅成功！", QtWidgets.QMessageBox.Yes)
