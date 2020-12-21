from PyQt5 import QtCore, QtGui, QtWidgets
import datetime
from ui.Ui_BookCheckOutWindow import Ui_BookCheckOutWindow
from Database import Database
import Global


class BookCheckOutWindow(QtWidgets.QMainWindow, Ui_BookCheckOutWindow):

    def __init__(self, *args, **kwargs):
        super(BookCheckOutWindow, self).__init__(*args, **kwargs)
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

        # 准备删除登记库存信息SQL
        sql_str1 = "delete from bookstock where Bs_id = '%s';" % Bs_id

        # 准备登记出入库信息SQL
        now_time = datetime.datetime.now()
        sR_id = now_time.strftime('%Y%m%d%H%M%S%f')  # 流水编号
        C_id = Global.C_ID  # 员工号
        S_action = "出库"  # 动作
        Sdate = now_time.strftime('%Y-%m-%d')

        sql_str2 = "insert into stock_regist (sR_id, Bs_id, C_id, S_action, Sdate) " \
                   "values ('%s', '%s', '%s', '%s', '%s');" % (sR_id, Bs_id, C_id, S_action, Sdate)

        # 执行SQL
        try:
            db.update(sql_str1)
            db.update(sql_str2)
        except Exception as e:
            self.msg.setText("出库失败！{}".format(str(e)))
            return

        # SQL执行成功
        self.hide()
        self.clear()
        QtWidgets.QMessageBox.information(self, "提示", "出库成功！", QtWidgets.QMessageBox.Yes)
