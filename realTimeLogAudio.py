#!/usr/bin/python

import pyaudio
import numpy as np
from time import time
import os
import signal
import sys

CHANNELS = 2
RATE = 44100
FREQ = 100
NEWFREQ = 100
PHASE = 0
LOG_FILE = "probemon.log"

def signal_handler(sig, frame):
    ''' 
       Process control + C 
    '''
    stream.stop_stream()
    stream.close()
    p.terminate()
    print "Exiting program upon Control + C"
    sys.exit(0)

def callback(in_data, frame_count, time_info, status):
    '''
        Callback function refreshes frequency audio stream
    '''
    global TT,PHASE,FREQ,NEWFREQ
    if NEWFREQ != FREQ:
        PHASE = 2*np.pi*TT*(FREQ-NEWFREQ)+PHASE
        FREQ=NEWFREQ
    left = (np.sin(PHASE+2*np.pi*FREQ*(TT+np.arange(frame_count)/float(RATE))))
    data = np.zeros((left.shape[0]*2,),np.float32)
    data[0::2] = left
    data[1::2] = left
    TT+=frame_count/float(RATE)
    return (data, pyaudio.paContinue)


if __name__=="__main__":
    TT = time()
    #Handle SIGINT
    signal.signal(signal.SIGINT, signal_handler)

    #Initialize pyaudio instance
    p = pyaudio.PyAudio()

    # define and start stream
    stream = p.open(format=pyaudio.paFloat32,
                channels=CHANNELS,
                rate=RATE,
                input=True,
                output=True,
                stream_callback=callback)

    stream.start_stream()

    #Logic to refresh global NEWFREQ var by probing LOG_FILE
    tmphold = ""
    try:
        while True:
            line = os.popen('tail -n 1 {}'.format(LOG_FILE)).read()
            try:
                key, val = line.split()
            except:
                key, val = "default", 0.0

            f = abs(int(val))  
            NEWFREQ = f * 10  #update freq per log
            if NEWFREQ != tmphold:
                tmphold = NEWFREQ
                print "mac:{} , rssi:{} , freq:{} Hz".format(key,val,NEWFREQ)
    finally:
        stream.stop_stream()
        stream.close()
        p.terminate()
