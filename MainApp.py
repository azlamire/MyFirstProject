from MainAppUi import *
from Video import CVideo
from Playlist import CPlayList
from PyQt5 import QtWidgets
import sys

class MainApp(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.vid)
        self.ui.pushButton_2.clicked.connect(self.playlist)
        self.center()
    def vid(self): 
        self.ExVid = CVideo()
        self.ExVid.show()
    def playlist(self):
        self.ExPlay = CPlayList()
        self.ExPlay.show()
    def center(self):
        qreact = self.frameGeometry()
        centralPoint = QtWidgets.QDesktopWidget().availableGeometry().center()
        qreact.moveCenter(centralPoint)
        self.move(qreact.topLeft())
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    win = MainApp()
    win.show()
    sys.exit(app.exec())
