import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO_RP = 16
GPIO_LP = 26

GPIO.setup(GPIO_RP, GPIO.OUT)
GPIO.setup(GPIO_LP, GPIO.OUT)

try:
    while True:
        print("forward")
        GPIO.output(GPIO_RP, False)
        GPIO.output(GPIO_LP, True)
        time.sleep(1)
        print("stop")
        GPIO.output(GPIO_RP, True)
        GPIO.output(GPIO_LP, True)
        time.sleep(5)
except KeyboardInterrupt:
    print("Motor activation is terminated....!!!")
finally:
    GPIO.cleanup()
