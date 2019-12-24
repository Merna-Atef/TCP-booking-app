import sys
from PyQt5 import QtCore, QtGui, QtWidgets, QtQuick
from PyQt5.QtCore import QUrl
from PyQt5.QtMultimedia import QMediaContent, QMediaPlayer
from PyQt5.QtMultimediaWidgets import QVideoWidget
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtMultimedia import *
from PyQt5.QtMultimediaWidgets import *
from sahar import Ui_MainWindow
import easySocket as s
import os

flag = False
# HOST = '192.168.43.218'
HOST = '172.28.130.39'

class ViewerWindow(QMainWindow):
    state = pyqtSignal(bool)

    def closeEvent(self, e):
        # Emit the window state, to update the viewer toggle button.
        self.state.emit(True)
        global flag
        flag = True

    def toggle_viewer(self, state):
        if state:
            self.viewer.show()
        else:
            self.viewer.hide()



class window(QtWidgets.QMainWindow):
    def __init__(self):
        super(window, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        #Code for the video player
        self.error_dialog = None
        self.error_dialog1 = None
        self.book_message = None
        self.player = QMediaPlayer()
        self.viewer = ViewerWindow(self)
        self.viewer.setWindowFlags(self.viewer.windowFlags() | Qt.WindowStaysOnTopHint)
        self.viewer.setMinimumSize(QSize(480,360))
        videoWidget = QVideoWidget()
        self.viewer.setCentralWidget(videoWidget)
        self.player.setVideoOutput(videoWidget)
        #code for the video player
        self.ui.tabWidget.setTabEnabled(1, False)
        self.ui.tabWidget.setTabEnabled(2, False)
        self.ui.tabWidget.setTabEnabled(3, False)
        self.ui.pushButton_3.clicked.connect(self.getHotel1)
        self.ui.pushButton_4.clicked.connect(self.getHotel2)
        self.ui.pushButton.clicked.connect(self.goToCountry)
        self.ui.pushButton_6.clicked.connect(self.goToBooking)
        self.ui.pushButton_5.clicked.connect(self.playVideo)
        self.ui.pushButton_7.clicked.connect(self.Book)
        #self.viewer.closeEvent()

    def paintEvent(self, event):
        global flag
        if flag :
            self.player.stop()
            flag = False
            self.player = QMediaPlayer()
            self.viewer = ViewerWindow(self)
            self.viewer.setWindowFlags(self.viewer.windowFlags() | Qt.WindowStaysOnTopHint)
            self.viewer.setMinimumSize(QSize(480,360))
            videoWidget = QVideoWidget()
            self.viewer.setCentralWidget(videoWidget)
            self.player.setVideoOutput(videoWidget)


    def Book(self):
        # HOST = '192.168.43.217'
        PORT = 6666
        data = []
        data.append(self.ui.lineEdit_3.text())
        data.append(self.ui.lineEdit_2.text())
        data.append(self.ui.lineEdit_4.text())
        data.append(self.ui.lineEdit_5.text())
        data.append("save")

        for x in data:
            c = s.connect_tcp(HOST,PORT)
                #print("client connected on socket ", c)
            s.send_text(x, c)

        self.bookedMessage()
        self.ui.tabWidget.setCurrentIndex(0)
        self.ui.tabWidget.setTabEnabled(1, False)
        self.ui.tabWidget.setTabEnabled(2, False)
        self.ui.tabWidget.setTabEnabled(3, False)

    def playVideo(self):
        path ="C:\Users\merna\Merna\Biomedical\4th year\Term 1\Network\Final Project\Final code\network-socket-TCP\Client\recievedVideo.mp4"
        print(path)
        self.content= QMediaContent(QUrl.fromLocalFile(path))
        self.player.setMedia(self.content)
        self.viewer.show()
        self.player.play()


    def goToBooking(self):
        self.ui.tabWidget.setTabEnabled(3, True)
        self.ui.tabWidget.setCurrentIndex(3)
        
    def goToCountry(self):
        hotel = self.ui.lineEdit.text()
        if hotel == "norway":
            self.ui.tabWidget.setTabEnabled(1, True)
            self.ui.tabWidget.setCurrentIndex(1)
        else:
            self.errorMessage()

    def setImage1(self):
        try:
            # HOST = '192.168.43.217'
            PORT = 6666
            c = s.connect_tcp(HOST,PORT)
            print("client connected on socket ", c)
            s.send_text("hotel1", c)
            data1 = s.rcv_data(c)
            myfile1 = open("recievedPic.jpg", 'wb')
            myfile1.write(data1)
            pixmap = QPixmap("recievedPic.jpg")
            self.ui.label_8.setPixmap(pixmap)
        except:
            self.errorMessage1()

    def setImage2(self):
            try:
                # HOST = '192.168.43.217'

                PORT = 6666
                c = s.connect_tcp(HOST,PORT)
                    #print("client connected on socket ", c)
                s.send_text("hotel2", c)
                data1 = s.rcv_data(c)
                myfile1 = open("recievedPic.jpg", 'wb')
                myfile1.write(data1)
                pixmap = QPixmap("recievedPic.jpg")
                self.ui.label_8.setPixmap(pixmap)
            except:
                self.errorMessage1()


    def setVideo1(self):
        try:
            # HOST = '192.168.43.217'

            PORT = 6666
            c = s.connect_tcp(HOST,PORT)
                #print("client connected on socket ", c)
            s.send_text("hotel1video", c)
            data1 = s.rcv_data(c)
            myfile1 = open("recievedVideo.mp4", 'wb')
            myfile1.write(data1)
            #print(url)
            
            print("I'm here")
            self.ui.tabWidget.setTabEnabled(2, True)
            self.ui.tabWidget.setCurrentIndex(2)
            #self.errorMessage()
        except:
            self.errorMessage1()

    def setVideo2(self):
        try:
            # HOST = '192.168.43.217'

            PORT = 6666
            c = s.connect_tcp(HOST,PORT)
                #print("client connected on socket ", c)
            s.send_text("hotel2video", c)
            data1 = s.rcv_data(c)
            myfile1 = open("recievedVideo.mp4", 'wb')
            myfile1.write(data1)
            #print(url)
            
            print("I'm here")
            self.ui.tabWidget.setTabEnabled(2, True)
            self.ui.tabWidget.setCurrentIndex(2)
            #self.errorMessage()
        except:
            self.errorMessage1()


    def getHotel2(self):
        self.setImage2()
        self.setVideo2()
        self.ui.tabWidget.setTabEnabled(2, True)
        self.ui.tabWidget.setCurrentIndex(2)


    def getHotel1(self):
        self.setImage1()
        self.setVideo1()
        self.ui.tabWidget.setTabEnabled(2, True)
        self.ui.tabWidget.setCurrentIndex(2)

    def errorMessage1(self):
        self.error_dialog1 = QtWidgets.QErrorMessage()
        self.error_dialog1.showMessage("We couldn't connect the server")

    def errorMessage(self):
        self.error_dialog = QtWidgets.QErrorMessage()
        self.error_dialog.showMessage('We dont have hotels for this country :(')

    def bookedMessage(self):
        self.book_message = QtWidgets.QErrorMessage()
        self.book_message.showMessage("We'll reach you really soon")
        

def main():
    app = QtWidgets.QApplication(sys.argv)
    application = window()
    application.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    print("hiii")
    main()