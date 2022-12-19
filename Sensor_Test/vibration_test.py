import RPi.GPIO as GPIO
import signal
import sys
import time

def signal_handler(signal, frame):
    print('process stop')
    PWM_RC.stop()
    GPIO.cleanup()
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)
GPIO.setmode(GPIO.BCM) #BCM mode

VIBE = 27

GPIO.setup(VIBE, GPIO.OUT)
PWM_RC = GPIO.PWM(VIBE, 200)
PWM_RC.start(7.5)

while True:
    print("here - RCMOTOR on")
    PWM_RC.ChangeDutyCycle(5)
    time.sleep(1)
    PWM_RC.ChangeDutyCycle(95)
    time.sleep(1)
