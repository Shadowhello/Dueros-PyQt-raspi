#!/usr/bin/python3
import sys
import signal
import os
import time
import collections
import wave  
import pyaudio
import snowboydecoder.snowboydetect as snowboydetect
import globallob.alllib as alllib
#import AipSpeed as aipd


RESOURCE_FILE = "snowboydecoder/resources/common.res"
DETECT_DING = "snowboydecoder/resources/ding.wav"
DETECT_DONG = "snowboydecoder/resources/dong.wav"
#model = 'resources/smart_mirror.umdl'
model = "snowboydecoder/resources/xiaoxi.pmdl"
sensitivity = '0.5'
audiogain = 1

detector = snowboydetect.SnowboyDetect(resource_filename=RESOURCE_FILE.encode(), model_str=model.encode())
detector.SetSensitivity(sensitivity.encode())
detector.SetAudioGain(audiogain)

ring_buffer = collections.deque(maxlen=(detector.NumChannels() * detector.SampleRate()*5))

def audio_callback(in_data, frame_count, time_info, status):
    ring_buffer.extend(in_data)
    play_data = chr(0) * len(in_data)
    return play_data, pyaudio.paContinue

audio = pyaudio.PyAudio()
stream_in = audio.open(
            input=True, output=False,
            format=audio.get_format_from_width(detector.BitsPerSample()/8),
            channels=detector.NumChannels(),
            rate=detector.SampleRate(),
            frames_per_buffer=2048,
            stream_callback=audio_callback)

print(('format = %d' % audio.get_format_from_width(detector.BitsPerSample()/8)))
print(('channels = %d' %detector.NumChannels()))
print(('rate = %d' % detector.SampleRate()))


def save_wave_file(filename, data):   
    wf = wave.open(filename, 'wb')  
    wf.setnchannels(1)  
    wf.setsampwidth(2)  
    wf.setframerate(16000)  
    wf.writeframes(b"".join(data))  
    wf.close() 

def save_flag_file(filename, flag):
    wf = open(filename,"w")
    wf.write(flag)
    wf.close()

def play_audio_file(fname=DETECT_DING):
    ding_wav = wave.open(fname, 'rb')
    ding_data = ding_wav.readframes(ding_wav.getnframes())
    audio = pyaudio.PyAudio()
    stream_out = audio.open(
        format=audio.get_format_from_width(ding_wav.getsampwidth()),
        channels=ding_wav.getnchannels(),
        rate=ding_wav.getframerate(), input=False, output=True)
    stream_out.start_stream()
    stream_out.write(ding_data)
    time.sleep(0.2)
    stream_out.stop_stream()
    stream_out.close()
    audio.terminate()

def detected_callback():

    rec_count = 0
    sil_count = 0
    save_buffer = [] 

    while True:
        data = bytes(bytearray(ring_buffer))
        ring_buffer.clear()
        #data = stream_in.read(4000)
        
        if len(data) == 0:
            time.sleep(0.03)
            continue

        ans = detector.RunDetection(data)
        if ans is 1:    
            print('hotword dectect')
            play_audio_file('snowboydecoder/resources/ding.wav')
            save_buffer = []
            rec_count = 1 
            #data = stream_in.read(800)
            data = bytes(bytearray(ring_buffer))
            ring_buffer.clear()
            alllib.flag = 1
        elif ans is 0:      
            if rec_count > 0:
                print('voice')
                save_buffer.append(data)
                rec_count += 1 
                sil_count = 0
                alllib.flag = 2
        elif ans is -2:    
            if rec_count > 0:
                save_buffer.append(data)
                sil_count += 1
                alllib.flag = 3
                print('silence')
            if sil_count > 2 and rec_count > 1:
                play_audio_file('snowboydecoder/resources/dong.wav')
                filename = "snowboydecoder/resources/rec.wav"   
                save_wave_file(filename, save_buffer) 
            #    text = aipd.read_file(filename)
		#print('rec asr %s' % text)
                rec_count = 0
                sil_count = 0 
                save_buffer = [] 
                print('Listening...')
                alllib.flag = 0
        

if __name__ == "__main__":
    print('Listening...')
    detected_callback()
