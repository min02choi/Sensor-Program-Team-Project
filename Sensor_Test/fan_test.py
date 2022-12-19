import os
import RPi.GPIO as GPIO
from time import sleep

# pin = 21
# maxTmp = 50
#
# def setup():
#     GPIO.setmode(GPIO.BCM)
#     GPIO.setup(pin, GPIO.OUT)
#     GPIO.setwarnings(False)
#
# def getCPUTemperature():
#     temp = os.popen("vcgencmd measure_temp").readline()
#     return (temp.replace("temp=","").replace("'C\n",""))
#
# def checkTemperature():
#     CPU_temp = float(getCPUTemperature())
#     if CPU_temp > maxTmp:
#         GPIO.output(pin, True)
#     else:
#         GPIO.output(pin, False)
#
# try:
#     setup()
#     while True:
#         GPIO.output(pin, True)
#         sleep(10)
# except KeyboardInterrupt:
#     GPIO.cleanup()

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
FAN_PIN = 26
GPIO.setup(FAN_PIN, GPIO.OUT)
GPIO.output(FAN_PIN, True)
sleep(10)