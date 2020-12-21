from PyQt5 import QtWidgets, Qt
import sys

from ui.Ui_MainWindow import Ui_MainWindow
from form.WelcomeWindow import WelcomeWindow
from form.BookWindow import BookWindow
from form.MemberWindow import MemberWindow


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    """
    主界面
    """
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)

        # 给frame设定堆叠布局
        self.wins = Qt.QStackedLayout(self.frame)

        self.welcome_window = WelcomeWindow()
        self.book_window = BookWindow()
        self.member_window = MemberWindow()

        # 将各个窗口加入到堆叠布局中
        self.wins.addWidget(self.welcome_window)  # 欢迎界面窗口
        self.wins.addWidget(self.book_window)  # 图书管理窗口
        self.wins.addWidget(self.member_window)  # 会员管理窗口

        self.windowList = {"welcome_window": 0, "book_window": 1, "member_window": 2}

        self.init_ui()

    def init_ui(self):
        # 将动作事件连接到对应的处理函数
        self.action_book_manage.triggered.connect(self.book_manage)  # 图书管理
        self.action_member_manage.triggered.connect(self.member_manage)  # 会员管理
        self.action_logout.triggered.connect(self.logout)  # 退出

    def book_manage(self):
        """
        图书管理的响应处理函数
        :return:
        """
        index = self.windowList["book_window"]
        self.wins.setCurrentIndex(index)

    def member_manage(self):
        """
        会员管理
        :return:
        """
        index = self.windowList["member_window"]
        self.wins.setCurrentIndex(index)

    def logout(self):
        """
        退出登录
        :return:
        """
        sys.exit()
