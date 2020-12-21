from PyQt5 import QtCore, QtGui, QtWidgets
from ui.Ui_BookAddWindow import Ui_BookAddWindow
from Database import Database


class BookAddWindow(QtWidgets.QMainWindow, Ui_BookAddWindow):

    def __init__(self, *args, **kwargs):
        super(BookAddWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)
        self.init_ui()

    def init_ui(self):
        # 不允许拉伸、最大化
        self.setFixedSize(self.width(), self.height())

    def clear(self):
        self.B_ISBN.setText("")
        self.Bname.setText("")
        self.Bpress.setText("")
        self.Bauthor.setText("")
        self.Btype.setText("")
        self.Bposition.setText("")
        self.msg.setText("")

    def do_submit(self):

        B_ISBN = self.B_ISBN.text()
        Bname = self.Bname.text()
        Bpress = self.Bpress.text()
        Bauthor = self.Bauthor.text()
        Btype = self.Btype.text()
        Bposition = self.Bposition.text()

        if len(B_ISBN.strip()) < 1:
            self.msg.setText("ISBN不能为空！")
            return

        if len(Bname.strip()) < 1:
            self.msg.setText("书名不能为空！")
            return

        # TODO 增加校验

        record = (B_ISBN, Bname, Bpress, Bauthor, Btype, Bposition)

        sql_str = "insert into book values ('%s', '%s', '%s', '%s', '%s', '%s');" % record

        db = Database()
        try:
            rtn = db.update(sql_str)
        except Exception as e:
            self.msg.setText("登记失败！{}".format(str(e)))
            return

        if not rtn:
            self.msg.setText("登记失败！")
            return
        else:
            self.hide()
            self.clear()
            QtWidgets.QMessageBox.information(self, "提示", "登记成功！", QtWidgets.QMessageBox.Yes)
