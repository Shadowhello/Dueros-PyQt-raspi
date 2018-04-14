from PyQt5 import QtCore,QtGui
import time
import os
import sys
import numpy as np 
import globallob.alllib as alllib
try:
    import RPi.GPIO as GPIO
except RuntimeError:
    print("Error importting Rpi.GPIO")
#这个线程是为了独立控制GPIO口而设计，根据接受到的信息来判断控制哪一个GPIO
class gpio_Thread(QtCore.QThread):

    def __init__(self,parent=None):
        super(gpio_Thread,self).__init__(parent)

    sinout = QtCore.pyqtSignal(str)
    def run(self):

        enable = alllib.cmdflag
        if enable==1:
            channel = 26
            GPIO.setmode(GPIO.BCM)
            GPIO.setup(channel,GPIO.OUT,initial=GPIO.LOW)
            GPIO.output(channel,GPIO.HIGH)
            alllib.showmsg = alllib.showmsg+'灯已开启'+"\n"
            print('灯已开启')
            alllib.cmdflag = 0
	#        playtomp3('灯已开启')
            #time.sleep(10)
        if enable==2:
            channel = 26
            GPIO.setmode(GPIO.BCM)
            GPIO.setup(channel,GPIO.OUT,initial=GPIO.LOW)
            GPIO.output(channel,GPIO.LOW)
            alllib.showmsg = alllib.showmsg+"灯已关闭"+"\n"
            print("灯已关闭")
            alllib.cmdflag = 0
        if enable==3:
            print("dh11 --")
            import gpiocontrol.dh11
            gpiocontrol.dh11.dh11func()
            alllib.aipspeedflag = 2
            print("end...")
            alllib.cmdflag = 0
            pass
        if enable ==4:
            alllib.showmsg = alllib.showmsg + "做梦吧，没有关机功能" +"\n"
