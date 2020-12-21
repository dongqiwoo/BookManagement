from PyQt5 import QtCore, QtGui, QtWidgets
from ui.Ui_GivebackWindow import Ui_GivebackWindow
from Database import Database
import datetime
import Global


class GivebackWindow(QtWidgets.QMainWindow, Ui_GivebackWindow):

    def __init__(self, *args, **kwargs):
        super(GivebackWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)
        self.init_ui()

    def init_ui(self):
        # 不允许拉伸、最大化
        self.setFixedSize(self.width(), self.height())

    def clear(self):
        self.Bs_id.setText("")
        self.msg.setText("")

    def do_submit(self):

        # 输入信息校验
        Bs_id = self.Bs_id.text()
        if len(Bs_id.strip()) < 1:
            self.msg.setText("图书编号不能为空！")
            return

        # 查询是否有该图书
        sql_str = "select * from bookstock where Bs_id = '%s';" % Bs_id
        db = Database()
        book = db.query(sql_str).fetchone()
        if book is None:
            QtWidgets.QMessageBox.information(self, "提示", "不存在该编号的图书！", QtWidgets.QMessageBox.Yes)
            return

        # 检查该图书是否是被借阅状态，并取到借阅的会员号
        if book[3] != "借出":
            QtWidgets.QMessageBox.information(self, "提示", "该图书当前非借出状态！", QtWidgets.QMessageBox.Yes)
            return
        M_id = book[4]

        # 准备登记库存信息SQL
        sql_str1 = "update bookstock set Bstate = '在馆', M_id = '', borrow_date = '' where Bs_id = '%s';" % Bs_id

        # 准备登记租借登记表SQL
        now_time = datetime.datetime.now()
        bR_id = now_time.strftime('%Y%m%d%H%M%S%f')  # 流水编号
        C_id = Global.C_ID  # 员工号
        B_action = "归还"  # 动作
        Bdate = now_time.strftime('%Y-%m-%d')

        sql_str2 = "insert into borrow_regist (bR_id, M_id, Bs_id, C_id, B_action, Bdate) " \
                   "values ('%s', '%s', '%s', '%s', '%s', '%s');" % (bR_id, M_id, Bs_id, C_id, B_action, Bdate)

        # 执行SQL
        try:
            db.update(sql_str1)
            db.update(sql_str2)
        except Exception as e:
            self.msg.setText("归还失败！{}".format(str(e)))
            return

        # SQL执行成功
        self.hide()
        self.clear()
        QtWidgets.QMessageBox.information(self, "提示", "归还成功！", QtWidgets.QMessageBox.Yes)
