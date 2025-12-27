from RegisterUi import *
from PyQt5 import QtWidgets
from Login import *
from pymongo import MongoClient
import sys
import time
class Register(QtWidgets.QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.ui = Ui_register()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.reg)
        self.center()
        self.client = MongoClient('mongodb://127.0.0.1:27017/?directConnection=true&serverSelectionTimeoutMS=2000&appName=mongosh+2.2.12')
        self.coll = self.client.Test
        self.db = self.coll.users
    def center(self):
        qr = self.frameGeometry()
        cr = QtWidgets.QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cr)
        self.move(qr.topLeft())
    def reg(self):
        self.newlogin = self.ui.lineEdit.text()
        self.newpass = self.ui.lineEdit_2.text()
        if self.newlogin and self.newpass:
            self.db.insert_one({"login":self.newlogin,"password":self.newpass})
            self.message = QtWidgets.QMessageBox()
            self.message.setWindowTitle('Login and Password')
            self.message.setText('Everything is OK')
            self.message.exec()
            time.sleep(4)
            self.close()
            self.log = login()
            self.log.show()

        else:
            self.erorr = QtWidgets.QMessageBox()
            self.erorr.setText('Enter the new login or the new pass')
            self.erorr.exec()

        
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    win = Register()
    win.show()
    sys.exit(app.exec_())