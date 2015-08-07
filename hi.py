from __future__ import division
from time import sleep
from math import sin
from datetime import datetime, timedelta
from itertools import cycle
import alsaaudio, time, audioop
from numpy import mean

inp = alsaaudio.PCM(alsaaudio.PCM_CAPTURE,alsaaudio.PCM_NONBLOCK)

inp.setchannels(1)
inp.setrate(8000)
inp.setformat(alsaaudio.PCM_FORMAT_S16_LE)

inp.setperiodsize(160)
ys = [100]
y = 100
p = 100
last = datetime.now()
z = ''

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

for x in cycle(range(100000)):
    i = datetime.now()
    if i - last > timedelta(seconds=.01):
        last = datetime.now()
        p = int(mean(ys)) * 3.9
        ys = []
        if p > 32767:
            z = bcolors.WARNING
            p = 32767
        elif p > 20000:
            z = bcolors.OKBLUE
        elif p > 10000:
            z = bcolors.HEADER
        else:
            z = ''
    l,data = inp.read()
    if l:
        y = audioop.max(data, 2)
        if y == 0:
            continue
    ys.append(y)
    sleep(.015 - .9*(.015* (p/32768)))
    print(z + "o" * int(159.0+(p/32768)*(156.0*sin(x/120.0))) + bcolors.ENDC) 

