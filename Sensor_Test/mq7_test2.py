import time

import serial
import time

# 코드 분석해보시게나

port = '/dev/ttyACM0'
brate = 9600    # boudrate, 아두이노는 9600
cmd = 'temp'

a = 1

while (True):

    seri = serial.Serial(port, baudrate=brate, timeout=None)
    print(seri.name)
    seri.write(cmd.encode())

    if seri.in_waiting != 0:
        content = seri.readline()
        print(content[:-2].decode())
        time.sleep(1)
        # a = 0

