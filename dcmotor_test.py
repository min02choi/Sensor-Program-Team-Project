# from gpiozero import Robot
# import time
#
# dc_motor = Robot(left=(12, 16), right=(20, 21))
#
# for num in range(4):
#     print(num, "Forward 회전")
#     dc_motor.forward(speed=1)
#     time.sleep(3)
#
#     print("모터 정지")
#     dc_motor.stop()
#     time.sleep(0.5)
#
#     print(num, "Backward 회전")
#     dc_motor.backward(speed=0.5)
#     time.sleep(3)
#
# dc_motor.stop()

###################################################################

# import RPi.GPIO as GPIO
# import time
#
# GPIO.setmode(GPIO.BCM)
# GPIO_RP = 6
# GPIO.setup(GPIO_RP, GPIO.OUT)
#
# try:
#     while True:
#         print("forward")
#         GPIO.output(GPIO_RP, True)
#         time.sleep(1)
#         print("stop")
#         GPIO.output(GPIO_RP, False)
#         time.sleep(5)
# except KeyboardInterrupt:
#     print("Motor activation is terminated....!!!")
# finally:
#     GPIO.cleanup()

################################################################

# from gpiozero import Motor
# import time
#
# motor = Motor(forward=5, backward=6)
# while True:
#     print("Motor dir : Forward")
#     motor.forward()
#     time.sleep(5)
#
#     print("Motor dir : Backward")
#     motor.backward()
#     time. sleep(5)

###################################################################

# import RPi.GPIO as GPIO
# import sys
# import time
#
# GPIO.setmode(GPIO.BCM)
# pin1 = 16
# pin2 = 26
#
# GPIO.setup(pin1, GPIO.OUT)
# GPIO.setup(pin2, GPIO.OUT)
#
#
# try:
#    while True:
#       GPIO.output(pin1, True)
#       GPIO.output(pin2, False)
#       print('Motor1')
#       time.sleep(2)
#
# except KeyboardInterrupt:
#    GPIO.cleanup()
#    sys.exit()

###################################################################

# import RPi.GPIO as GPIO
# import time
#
# GPIO.setmode(GPIO.BCM)
#
# GPIO_RP = 4
# GPIO_RN = 25
# GPIO_EN = 12
#
# GPIO.setup(GPIO_RP, GPIO.OUT)
# GPIO.setup(GPIO_RN, GPIO.OUT)
# GPIO.setup(GPIO_EN, GPIO.OUT)

# try:
#     while True:
#         print("forward")
#         GPIO.output(GPIO_RP, True)
#         GPIO.output(GPIO_RN, False)
#         GPIO.output(GPIO_EN, True)
#         time.sleep(2)
#
#         print("stop")
#         GPIO.output(GPIO_RP, False)
#         GPIO.output(GPIO_RN, False)
#         GPIO.output(GPIO_EN, True)
#         time.sleep(2)
#
#         print("backward")
#         GPIO.output(GPIO_RP, True)
#         GPIO.output(GPIO_RN, False)
#         GPIO.output(GPIO_EN, True)
#         time.sleep(2)
#
#         print("break")
#         GPIO.output(GPIO_EN, False)
#         time.sleep(2)
#
# finally:
#     GPIO.cleanup()

###################################################################

# import RPi.GPIO as GPIO
# import time
#
# GPIO.setmode(GPIO.BCM)
#
# GPIO_RP = 16
#
# GPIO.setup(GPIO_RP, GPIO.OUT)
#
# try:
#     while True:
#         print('forword')
#         GPIO.output(GPIO_RP, True)
#         time.sleep(1)
#
#         print('stop')
#         GPIO.output(GPIO_RP, False)
#         time.sleep(5)
# except KeyboardInterrupt:
#     print("Motor activation is terminated..!!!")
#
# finally:
#     GPIO.cleanup()

##############################################################

from gpiozero import Motor
import time

motor = Motor(forward=26, backward=16)

while True:
    motor.forward(speed=0.3)
    time.sleep(5)

    motor.backward(speed=0.5)
    time.sleep(5)
