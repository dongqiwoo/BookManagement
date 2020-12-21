from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from Database import Database
import Global

from ui.Ui_LoginWindow import Ui_LoginWindow


class LoginWindow(QDialog, Ui_LoginWindow):
    def __init__(self):
        super(LoginWindow, self).__init__()
        self.setupUi(self)
        self.init_ui()

    def init_ui(self):
        # 不允许拉伸、最大化
        self.setFixedSize(self.width(), self.height())
        # 默认有帮助问号，去掉
        self.setWindowFlags(Qt.WindowCloseButtonHint)
        self.msg.setAlignment(Qt.AlignCenter)

    def login(self):

        C_id = self.username.text()
        Cpassword = self.password.text()

        db = Database()
        sql_str = "select * from client where C_id = '{}' and Cpassword = '{}'".format(C_id, Cpassword)
        userinfo = db.query(sql_str).fetchone()

        if userinfo is not None:
            # 通过验证
            Global.C_ID = C_id  # 设置全局变量
            self.accept()
        else:
            self.msg.setText("用户名或密码错误！")
