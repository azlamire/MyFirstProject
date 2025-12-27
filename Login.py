from LoginAndPass import *
from MainApp import *
from Register import *
from PyQt5 import QtWidgets
from pymongo import MongoClient
import sys

class login(QtWidgets.QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setFixedSize(320,320)
        self.setWindowTitle('Login')
        self.center()
        self.ui.pushButton.clicked.connect(self.SignIn)
        self.ui.pushButton_2.clicked.connect(self.SignUp)
        self.client = MongoClient('mongodb://127.0.0.1:27017/?directConnection=true&serverSelectionTimeoutMS=2000&appName=mongosh+2.2.12')
        self.col = self.client.Test #collection
        self.db = self.col.users
    def SignIn(self):
        self.password = self.ui.lineEdit.text()
        self.login = self.ui.lineEdit_2.text()
        if self.db.find_one({"login":self.login,"password":self.password}):
            self.OpenMain()
        else:
            self.mes = QtWidgets.QMessageBox()
            self.mes.setText('Uncorrect login or password.Try again')
            self.mes.exec()
    def SignUp(self):
        self.reg = Register()
        self.reg.show()
        
    def center(self):
        qr = self.frameGeometry()
        cr = QtWidgets.QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cr)
        self.move(qr.topLeft())
    
    def OpenMain(self):
        self.pas = MainApp()
        self.pas.show()

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    win = login()
    win.show()
    sys.exit(app.exec_())