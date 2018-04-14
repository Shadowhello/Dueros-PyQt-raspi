#from dh11_play import playtomp3
import os
import sys
import wave
import numpy as np 
import time
from datetime import datetime
from pyaudio import PyAudio, paInt16

import time
try:
    import RPi.GPIO as GPIO
except RuntimeError:
    print("Error importting Rpi.GPIO")


from aip import AipSpeech

APP_ID = '9851518'
API_KEY = 'uGkUqKbu0R6U9eXEyzEWvNZm'
SECRET_KEY = 'FdQmbyndt3teFfLdDRM44E0d6Fq3X6SR'

client = AipSpeech(APP_ID, API_KEY, SECRET_KEY)


# 读取文件
def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()
#判断是否开灯
def fun_panduan_yuyi(result1):
    if str(result1).find('灯')!= -1:
        if str(result1).find('开')!= -1:
            return 1
    if str(result1).find('灯')!= -1:
        if str(result1).find('关')!= -1:
            return 2
    if str(result1).find('温')!= -1:
        if str(result1).find('湿')!= -1:
            return 3
    return 0

#添加GPIO操作
def control_GPIO_show(enable):
    channel = 26    
    GPIO.setmode(GPIO.BCM)

    GPIO.setup(channel,GPIO.OUT,initial=GPIO.LOW)
    if enable==1:
        GPIO.output(channel,GPIO.HIGH)
        print('灯已开启')
#        playtomp3('灯已开启')
        time.sleep(10)
    if enable==2:
        GPIO.output(channel,GPIO.LOW)
        print("灯已关闭")
#        playtomp3('灯已关闭')




# 从URL获取文件识别
#result = client.asr('', 'pcm', 16000, {
#    'url': 'http://121.40.195.233/res/16k_test.pcm',
#    'callback': 'http://xxx.com/receive',
#})

class GenAudio(object):
    def __init__(self):
        self.num_samples = 1024     #pyaudio内置缓冲大小
        self.sampling_rate = 16000  #取样频率
        self.level = 1500          #声音保存的阈值
        self.count_num = 20        #count_num个取样之内出现COUNT_NUM个大于LEVEL的取样则记录声音
        self.save_length = 8       #声音记录的最小长度：save_length * num_samples 个取样
        self.time_count = 16        #录音时间，单位s
        self.voice_string = []

    
    #保存文件
    def save_wav(self, filename):
        wf = wave.open(filename, 'wb') 
        wf.setnchannels(1) 
        wf.setsampwidth(2) 
        wf.setframerate(self.sampling_rate) 
        wf.writeframes(np.array(self.voice_string).tostring())
        wf.close()
    
    
    def read_audio(self):
        pa = PyAudio() 
        stream = pa.open(format=paInt16, channels=1, rate=self.sampling_rate, input=True, 
                frames_per_buffer=self.num_samples) 
        
        save_count = 0
        save_buffer = [] 
        time_count = self.time_count

        while True:
            time_count -= 1
            
            # 读入num_samples个取样
            string_audio_data = stream.read(self.num_samples)     
            # 将读入的数据转换为数组
            audio_data = np.fromstring(string_audio_data, dtype = np.short)
            #计算大于 level 的取样的个数
            large_sample_count = np.sum(audio_data > self.level)
            
            print(np.max(audio_data)),  "large_sample_count=>", large_sample_count

            # 如果个数大于COUNT_NUM，则至少保存SAVE_LENGTH个块
            if large_sample_count > self.count_num:
                save_count = self.save_length
            else: 
                save_count -= 1
            if save_count < 0:
                save_count = 0
            
            if save_count > 0:
                save_buffer.append(string_audio_data)
            else:
                if len(save_buffer) > 0:
                    self.voice_string = save_buffer
                    save_buffer = [] 
                    print("Recode a piece of  voice successfully!")
                    return True
            
            if time_count == 0: 
                if len(save_buffer) > 0:
                    self.voice_string = save_buffer
                    save_buffer = []
                    print("Recode a piece of  voice successfully!")
                    return True
                else:
                    return False
        return True


def main_fun():

	#r = GenAudio()
	#r.read_audio()
	#r.save_wav("./test.wav")
 #       time.sleep(1)
        # 识别本地文件
	os.system('python3 pyaudio_recored.py')
	result = client.asr(get_file_content('test.wav'), 'pcm', 16000, {
        'lan': 'zh',
})
	print(result)
	ret = fun_panduan_yuyi(result['result'])
#ret==1:开灯,ret==2:关灯，ret==3:读取温湿度 ret==0:没有以上命令.
	if ret == 1:
              	control_GPIO_show(ret)		
	if ret == 2:
		control_GPIO_show(ret)
	if ret == 3:
		os.system('python3 dh11_play.py')
if __name__ == "__main__":
    while True:
        try:
            try:
                print('\n')
                input('单击[Enter]建，然后发起对话\n')
            except SyntaxError:
                pass
            main_fun()
        except KeyboardInterrupt:
            break

