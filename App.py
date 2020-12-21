import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from form.MainWindow import MainWindow
from form.LoginWindow import LoginWindow

if __name__ == "__main__":
    # 设置支持高分辨率屏幕自适应
    QCoreApplication.setAttribute(Qt.AA_EnableHighDpiScaling)
    app = QApplication(sys.argv)
    app.setStyle("Fusion")

    dialog = LoginWindow()
    if dialog.exec_() == QDialog.Accepted:
        the_window = MainWindow()  # 主窗口
        the_window.show()
        sys.exit(app.exec_())
