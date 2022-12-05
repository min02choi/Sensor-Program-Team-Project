import RPi.GPIO as GPIO
import time
import signal
import sys
import threading
import led_code
import mq7_code
import piezo_code

GPIO.setmode(GPIO.BCM)

#### MQ7 세팅 ####

CO_STATE = 0


#### LED 세팅 ####
ledRed = 11
ledGreen = 9
ledBlue = 10

GPIO.setup(ledRed, GPIO.OUT)
GPIO.setup(ledGreen, GPIO.OUT)
GPIO.setup(ledBlue, GPIO.OUT)

PWM_RED = GPIO.PWM(ledRed, 100)
PWM_RED.start(0)

PWM_GREEN = GPIO.PWM(ledGreen, 100)
PWM_GREEN.start(0)

PWM_BLUE = GPIO.PWM(ledBlue, 100)
PWM_BLUE.start(0)

# 구체적인 RGB설정을 위함
# red_num = 0
# green_num = 0
# blue_num = 0
rgb_color = [0, 0, 0]       # RGB 색 설정

# LED 깜빡이는 속도
led_speed = 0

#### Piezo ####
piezo = 23
GPIO.setup(piezo, GPIO.OUT)
PWM_Piezo = GPIO.PWM(piezo, 100)
PWM_Piezo.start(0)


#### Vibration ####
# 이후 세팅


#### Variable ####
# 함수 안에서 global 설정
# 활성화 시킬것
LEVEL = 0


##################### 코드 시작 ##############################

print("hi")

try:
    # 쓰레드 실행
    # thread0_MQ7 = threading.Thread(target=mq7_code.MQ7_detect(), daemon=True)
    # thread0_MQ7.start()

    thread1_LED = threading.Thread(target=led_code.led_action(), daemon=True)
    thread1_LED.start()
    # thread2_PIEZO = threading.Thread(target=piezo_code.piezo_action(), daemon=True)
    # thread2_PIEZO.start()

    # state 설정
    #

    while True:
        # 일단은 사용자 input으로 값을 받아 실험
        LEVEL = int(input("Enter the Level: "))

        # LEVEL 값에 따른 작동
        if (LEVEL == 0):
            temp = 0
            # 택트 버튼 누를 경우 LEVEL 값을 0으로 설정

        #### 1단계 ####
        if (LEVEL == 1):
            ## LED 설정 ##
            rgb_color = [255, 255, 0]   # 색 수치만 넣으면 됨
            led_speed = 1           # LED 깜빡이는 속도

            ## Piezo 설정 ##

            ## Vibration 설정 ##


        #### 2단계 ####
        if (LEVEL == 2):
            rgb_color = [255, 130, 0]  # 색 수치만 넣으면 됨
            led_speed = 1  # LED 깜빡이는 속도

        #### 3단계 ####
        if (LEVEL == 3):
            rgb_color = [255, 0, 0]  # 색 수치만 넣으면 됨
            led_speed = 1  # LED 깜빡이는 속도


except KeyboardInterrupt:
    print("Program End")

# 코드가 너무 더러워지나

# 매개변수로 전달? 아니면 global 변수로
# 소스파일 분리(led, piezo, ...)
