from PyQt5 import QtWidgets,QtCore
from mainwindow import Ui_MainWindow

from gpioshow import gpioshow
from fileoperate import fileoperate as foper
from snowboydecoder.snowboyrecord_Thread import snowboyThread
from AipSpeed.AipSpeed_Thread import AipSpeedrecognition_Tread
from AipSpeed.AipSpeed_Thread import AipSpeedsynthesis_Tread
import globallob.alllib as alllib
from gpiocontrol.gpio_Thread import gpio_Thread
import semantic
import  time
import main_refresh_Thread
class mywindow(QtWidgets.QWidget):
    def __init__(self):
        super(mywindow,self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.pushButton_1.clicked.connect(self.show1)
        self.ui.pushButton_2.clicked.connect(self.refreshfunc)
        self.ui.pushButton_3.clicked.connect(self.yuyinshibie)
        self.ui.pushButton_4.clicked.connect(self.control)
        self.ui.pushButton_5.clicked.connect(self.yuyinbofang)
        self.ui.pushButton_6.clicked.connect(self.autorun)



        #public
        self.f = foper()

        self.snowboythead = snowboyThread()
        self.recognizer = AipSpeedrecognition_Tread()
        self.player = AipSpeedsynthesis_Tread()
        self.gpiocontrol = gpio_Thread()
        
        self.autorun = main_refresh_Thread.mainrefresh()
        self.autorun.sinout.connect(self.autoslots)
        self.textshow = ""
    def autoslots(self,choice):
        if(choice ==0):
            print("0000")
            self.ui.pushButton_1.clicked.emit()
            #self.ui.pushButton_1.setStyleSheet("QPushButton:pressed{background-color:green}")
        if(choice==1):
            print("1111")
            self.ui.pushButton_2.clicked.emit()
            #self.ui.pushButton_2.setStyleSheet("QPushButton:pressed{background-color:green}")
        if(choice==2):
            print("222")
            self.ui.pushButton_3.clicked.emit()
            #self.ui.pushButton_3.setStyleSheet("QPushButton:pressed{background-color:green}")
            self.ui.pushButton_ding.setStyleSheet("QPushButton:pressed{background-color:gray}")
        if(choice==3):
            print("3333")
            self.ui.pushButton_4.clicked.emit()
            #self.ui.pushButton_4.setStyleSheet("QPushButton:pressed{background-color:green}")
        if(choice==4):
            print("444")
            self.ui.pushButton_5.clicked.emit()
            #self.ui.pushButton_5.setStyleSheet("QPushButton:pressed{background-color:green}")
            
            
        if(choice==10):
            self.ui.pushButton_ding.setStyleSheet("QPushButton{background-color:green}")
        if(choice==11):
            self.ui.pushButton_control.setStyleSheet("QPushButton{background-color:gray}")
        if(choice==12):
            self.ui.pushButton_control.setStyleSheet("QPushButton{background-color:red}")
    def yuyinshibie(self):
        self.recognizer.start()

    def control(self):
        self.gpiocontrol.start()
        pass
    def yuyinbofang(self):
        self.player.start()
        pass

    def refreshfunc(self,int):
        self.snowboythead.start()
        pass

    def autorun(self):
        self.autorun.start()
     #   self.ui.pushButton_2.clicked.emit()
      #  while 1:
       #     print("111")
       # pass
        
    def show1(self,str):
        self.ui.textEdit.setText(alllib.showmsg)
        self.ui.dh11show.setText(alllib.dh11show)
        pass


if __name__ == "__main__":
    import sys
    app=QtWidgets.QApplication(sys.argv)
    myshow = mywindow()
    myshow.show()
    sys.exit(app.exec())
