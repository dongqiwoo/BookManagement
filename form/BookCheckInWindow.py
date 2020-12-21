from PyQt5 import QtCore, QtGui, QtWidgets
import datetime
from ui.Ui_BookCheckInWindow import Ui_BookCheckInWindow
from Database import Database
import Global


class BookCheckInWindow(QtWidgets.QMainWindow, Ui_BookCheckInWindow):

    def __init__(self, *args, **kwargs):
        super(BookCheckInWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)
        self.init_ui()

    def init_ui(self):
        # 不允许拉伸、最大化
        self.setFixedSize(self.width(), self.height())

    def clear(self):
        self.B_ISBN.setText("")
        self.Bs_id.setText("")
        self.msg.setText("")

    def do_submit(self):

        # 输入信息校验
        B_ISBN = self.B_ISBN.text()
        Bs_id = self.Bs_id.text()

        if len(B_ISBN.strip()) < 1:
            self.msg.setText("ISBN不能为空！")
            return

        if len(Bs_id.strip()) < 1:
            self.msg.setText("图书编号不能为空！")
            return

        # 准备登记库存信息SQL
        now_time = datetime.datetime.now()
        Put_in_date = now_time.strftime('%Y-%m-%d')
        Bstate = "在馆"

        sql_str1 = "insert into bookstock (B_ISBN, Bs_id, Put_in_date, Bstate) " \
                  "values ('%s', '%s', '%s', '%s');" % (B_ISBN, Bs_id, Put_in_date, Bstate)

        # 准备登记出入库信息SQL
        sR_id = now_time.strftime('%Y%m%d%H%M%S%f')  # 流水编号
        C_id = Global.C_ID  # 员工号
        S_action = "入库"  # 动作
        Sdate = Put_in_date

        sql_str2 = "insert into stock_regist (sR_id, Bs_id, C_id, S_action, Sdate) " \
                   "values ('%s', '%s', '%s', '%s', '%s');" % (sR_id, Bs_id, C_id, S_action, Sdate)

        # 执行SQL
        db = Database()
        try:
            db.update(sql_str1)
            db.update(sql_str2)
        except Exception as e:
            self.msg.setText("入库失败！{}".format(str(e)))
            return

        # SQL执行成功
        self.hide()
        self.clear()
        QtWidgets.QMessageBox.information(self, "提示", "入库成功！", QtWidgets.QMessageBox.Yes)
