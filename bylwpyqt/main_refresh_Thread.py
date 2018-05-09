# !/usr/bin/python3
from PyQt5 import QtCore,QtGui
import time
from snowboydecoder.snowboyrecord_Thread import snowboyThread
from AipSpeed.AipSpeed_Thread import AipSpeedrecognition_Tread
from AipSpeed.AipSpeed_Thread import AipSpeedsynthesis_Tread
import globallob.alllib as alllib
from gpiocontrol.gpio_Thread import gpio_Thread
import semantic
import  time
import gpiocontrol.publish as pub
class mainrefresh(QtCore.QThread):
	
	
    def __init__(self,parent=None):
        super(mainrefresh,self).__init__(parent)
        self.snowboythead = snowboyThread()
        self.recognizer = AipSpeedrecognition_Tread()
        self.player = AipSpeedsynthesis_Tread()
        self.gpiocontrol = gpio_Thread()
    sinout = QtCore.pyqtSignal(int)
    preflag = 0
    def run(self):
        print("start auto run")
        self.sinout.emit(1)
        num = 0
        while 1:
            self.sinout.emit(0)
            time.sleep(0.1)
            nowflag =alllib.flag
            print(self.preflag,nowflag,alllib.aipspeedflag)
            if alllib.aipspeedflag == 1:
                self.sinout.emit(3)
                alllib.aipspeedflag = 0
            if alllib.aipspeedflag == 2:
                self.sinout.emit(4)
                alllib.aipspeedflag = 0
            if self.preflag ==3 and nowflag == 0:
                print("jinruyuyinshibie---\n")
                self.sinout.emit(2)
            self.preflag = nowflag
            
            
            if alllib.flag == 1:
                self.sinout.emit(10) 
            if alllib.cmdflag == 1:
                self.sinout.emit(12) #open red
                pub.sendcontrol()
            if alllib.cmdflag == 2:
                self.sinout.emit(11) #close gray
                pub.sendcontrol()
                
            num = num +1
            if num == 100:
                import gpiocontrol.dh11
                gpiocontrol.dh11.dh11func()
                alllib.dh11show = "温度："+str(alllib.dh11date[0])+"C"+"湿度："+str(alllib.dh11date[1])
                num = 0
                
                pub.sendwenshidu()
        pass
if __name__ == "__main__":
	pass
