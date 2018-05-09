# coding:utf-8
from PyQt5 import QtCore,QtGui
import time
import os
import semantic
from aip import AipSpeech
APP_ID = '9851518'
API_KEY = 'uGkUqKbu0R6U9eXEyzEWvNZm'
SECRET_KEY = 'FdQmbyndt3teFfLdDRM44E0d6Fq3X6SR'
import globallob.alllib as alllib
recognitionpath = "snowboydecoder/resources/rec.wav"



#发送wav文件到Dueros云识别系统进行识别
class AipSpeedrecognition_Tread(QtCore.QThread):

    def __init__(self,parent=None):
        super(AipSpeedrecognition_Tread,self).__init__(parent)

    client = AipSpeech(APP_ID, API_KEY, SECRET_KEY)
    # 读取文件
    def get_file_content(self,filePath):
        with open(filePath, 'rb') as fp:
            return fp.read()



    sinout = QtCore.pyqtSignal(str)
    def run(self):
        # 识别本地文件
        result = self.client.asr(self.get_file_content(recognitionpath), 'pcm', 16000, {'lan': 'zh',})
        alllib.result = result['result']
        alllib.msglist.append(result['result'])
        print(result['result'])
        alllib.showmsg = alllib.showmsg + str(alllib.result)+str("\n")
        r = semantic.getsemantic(result['result'])
        alllib.aipspeedflag = 1
        #self.sinout.emit(result)
        pass

#接受中文信息进行翻译与播放
class AipSpeedsynthesis_Tread(QtCore.QThread):

    def __init__(self,parent=None):
        super(AipSpeedsynthesis_Tread,self).__init__(parent)
    client = AipSpeech(APP_ID, API_KEY, SECRET_KEY)
    def playtomp3(self,input_chinese):
        result  = self.client.synthesis(input_chinese, 'zh', 1, {
			'vol': 5,
    })
        # 识别正确返回语音二进制 错误则返回dict 参照下面错误码
        if not isinstance(result, dict):
            with open('audio.mp3', 'wb') as f:
                f.write(result)
            os.system("play audio.mp3")
    sinout = QtCore.pyqtSignal(str)
    def run(self):
        if len(alllib.dh11date) == 0:
            alllib.showmsg = alllib.showmsg + '对不起，本次读取失败！'+"\n"
            self.playtomp3('对不起，本次读取失败！')
        else:
            alllib.dh11show = "温度："+str(alllib.dh11date[0])+"C"+"湿度："+str(alllib.dh11date[1])
            alllib.showmsg = alllib.showmsg + "读取成功，温度："+str(alllib.dh11date[0])+"摄氏度。"+"湿度："+str(alllib.dh11date[1]) + "\n"
            self.playtomp3("读取成功，温度："+str(alllib.dh11date[0])+"摄氏度。"+"湿度："+str(alllib.dh11date[1]))
        pass
