from PyQt5 import QtCore, QtGui, QtWidgets
from ui.Ui_WelcomeWindow import Ui_WelcomeWindow


class WelcomeWindow(QtWidgets.QWidget, Ui_WelcomeWindow):

    def __init__(self):
        super(WelcomeWindow, self).__init__()
        self.setupUi(self)
        self.init_ui()

    def init_ui(self):
        pass

