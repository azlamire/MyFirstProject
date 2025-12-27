from PyQt5 import QtWidgets
from pytubefix import YouTube
import sys, os
from VideoAndPlaylistUi import *


class Download(QtCore.QThread):
    def __init__(self,path,url):
        super().__init__()
        self.path = path
        self.url = url
    def run(self):
        self.YtUrl = YouTube(self.url)
        self.audio = self.YtUrl.streams.get_audio_only().download(self.path)
        self.Truetitle = self.YtUrl.title.replace("'",'').replace('"','').replace('.','').replace(',','').replace('~','')
        if '-' in self.YtUrl.title:
            os.rename(f'{self.path}/{self.Truetitle}.mp4',f'{self.path}/{self.YtUrl.title}.mp3')
        else:
            os.rename(f'{self.path}/{self.Truetitle}.mp4',f'{self.path}/{self.YtUrl.author}-{self.YtUrl.title}.mp3')    

class CVideo(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.ui.pushButton_2.clicked.connect(self.Downloading)
        self.ui.Choosethepath.clicked.connect(self.ChooseThePath)


    def ChooseThePath(self):
        global path 
        self.path = QtWidgets.QFileDialog.getExistingDirectory()
    
    def Downloading(self):

        self.passby = Download(self.path,self.ui.Urlline.text())
        self.passby.start()

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    win = CVideo()
    win.show()
    sys.exit(app.exec())