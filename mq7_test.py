# # import RPi.GPIO as GPIO
# # import time
# #
# # GPIO.setmode(GPIO.BCM)
# # GPIO.setup(18, GPIO.IN)
# # GPIO.setup(27, GPIO.OUT)
# #
# # try:
# #     while True:
# #         if GPIO.input(18):
# #             print("detection X")
# #             time.sleep(0.2)
# #         if GPIO.input(18) != 1:
# #             print("Detection O")
# #             GPIO.output(27, False)
# #             time.sleep(0.1)
# #             GPIO.output(27, True)
# #
# # except KeyboardInterrupt:
# #     GPIO.cleanup()
#
#
# from mq import *
# import sys
# import time
#
# try:
#     print("Press CTRL+C to abort.")
#
#     mq = MQ();
#     while True:
#         perc = mq.MQPercentage()
#         sys.stdout.write("\r")
#         sys.stdout.write("\033[K")
#         sys.stdout.write("LPG: %g ppm, CO: %g ppm, Smoke: %g ppm" % (perc["GAS_LPG"], perc["CO"], perc["SMOKE"]))
#         sys.stdout.flush()
#         time.sleep(0.1)
#
# except:
#     print("\nAbort by user")


# import RPi.GPIO as GPIO
# import time
#
# GPIO.setmode(GPIO.BCM)
# is_running = True
# GPIO.setup(26, GPIO.IN)  # 센서 입력
# # GPIO.setup(25, GPIO.OUT)  # LED
#
# try:
#     while is_running:
#         if GPIO.input(26) == 1:
#             # GPIO.output(25, GPIO.HIGH)  # LED ON
#             print("on")
#             time.sleep(1)
#
#         else:
#             # GPIO.output(25, GPIO.LOW)  # LED OFF
#             print("off")
#             time.sleep(1)
#
# except KeyboardInterrupt:
#     GPIO.cleanup()
#     is_running = False
#

#
import time
import botbook_mcp3002 as mcp

smokeLevel = 0

def readSmokeLevel():
    global smokeLevel

smokeLevel = mcp.readAnalog()

def main():
    while True:
        readSmokeLevel()
        print ("Current smoke level is %i " % smokeLevel)
        if smokeLevel > 120:
            print("Smoke detected")
        time.sleep(0.5)
