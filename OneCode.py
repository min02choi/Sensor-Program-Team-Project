import RPi.GPIO as GPIO
import time
import signal
import sys
import threading
import I2C_LCD_driver

# 시스템 종료
def signal_handler(signal, frame):
    print('process stop')
    GPIO.cleanup()
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)


#### MQ7 ####
# 일산화탄소 수치 감지
def MQ7_detect():
    global CO_STATE
    global LEVEL

    # CO_STATE 값 측정

    # CO 수치에 따른 LEVEL 설정
    while True:
        if (20 > CO_STATE):
            LEVEL = 0
        elif (40 > CO_STATE >= 20):
            LEVEL = 1
        elif (60 > CO_STATE >= 40):
            LEVEL = 2
        elif (CO_STATE >= 60):
            LEVEL = 3
        time.sleep(1)


#### LED ####
# LED 색 RGB 설정
def setRGB(r, g, b):
    PWM_RED.ChangeDutyCycle(r)
    PWM_GREEN.ChangeDutyCycle(g)
    PWM_BLUE.ChangeDutyCycle(b)

# LED 깜빡임
def led_action():
    # 정하셈 변수들을 global로 뺼지 말지
    # 근데 LEVEL도 안 빼도 될거같긴 함
    global LEVEL
    global rgb_color
    global led_speed

    # 1단계, 2단계, 3단계 LED가 켜지는 시간을 조절할 것 (led_speed)
    # time.sleep(led_speed), time.sleep(1 - led_speed) 이런 느낌으로
    while True:
        # 여기를 if문 안으로 넣을 것
        # setRGB(rgb_color[0], rgb_color[1], rgb_color[2])
        # time.sleep(led_speed)
        # setRGB(rgb_color[0], rgb_color[1], rgb_color[2])         # LED 꺼짐
        # time.sleep(led_speed)   # 계산 해서 1 - led_speed

        # 근데 변수를 다 global로 빼면 if문으로 안나눠도 되긴하는데...
        # 코드의 효율성 측면은 나중에 고려. 일단은 동작여부 우선
        if (LEVEL == 0):
            setRGB(0, 0, 0)
        elif (LEVEL == 1):
            # test print 문으로 인해서 안보였던것
            # print("rgb_color[0] %d", rgb_color[0])
            # print("rgb_color[1] %d", rgb_color[1])
            # print("rgb_color[2] %d", rgb_color[2])

            setRGB(rgb_color[0], rgb_color[1], rgb_color[2])
            time.sleep(led_speed)
            setRGB(0, 0, 0)
            time.sleep(0.5)
        elif (LEVEL == 2):
            setRGB(rgb_color[0], rgb_color[1], rgb_color[2])
            time.sleep(led_speed)
            setRGB(0, 0, 0)
            time.sleep(0.3)
        elif (LEVEL == 3):
            setRGB(rgb_color[0], rgb_color[1], rgb_color[2])
            time.sleep(led_speed)
            setRGB(0, 0, 0)
            time.sleep(0.2)


#### Piezo ####
# 피에조부저
def piezo_action():
    global LEVEL

    while True:
        if (LEVEL == 0):
            # PWM_Piezo.ChangeDutyCycle(20)
            # PWM_Piezo.ChangeFrequency(0)
            # time.sleep(1)
            PWM_Piezo.ChangeDutyCycle(0)
            time.sleep(1)
        elif (LEVEL == 1):
            PWM_Piezo.ChangeDutyCycle(20)
            PWM_Piezo.ChangeFrequency(261)
            time.sleep(1)
            PWM_Piezo.ChangeDutyCycle(0)
            time.sleep(1)
        elif (LEVEL == 2):
            PWM_Piezo.ChangeDutyCycle(20)
            PWM_Piezo.ChangeFrequency(329)
            time.sleep(1)
            PWM_Piezo.ChangeDutyCycle(0)
            time.sleep(1)
        elif (LEVEL == 3):
            PWM_Piezo.ChangeDutyCycle(20)
            PWM_Piezo.ChangeFrequency(392)
            time.sleep(1)


#### Vibration ####
# 진동모터
def vibration_action(speed):
    global LEVEL

def lcd_show():
    mylcd = I2C_LCD_driver.lcd()
    mylcd.lcd_display_string("Hello World", 1)
    mylcd.lcd_display_string("Raspberry Pi3 b+", 2)


################### 센서&변수 세팅 ################################


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
PWM_Piezo.start(100)
PWM_Piezo.ChangeDutyCycle(20)




#### Vibration ####
# 이후 세팅


#### Variable ####
# 함수 안에서 global 설정
# 활성화 시킬것
LEVEL = 0


##################### 코드 시작 ##############################

try:
    # 쓰레드 실행
    # thread0_MQ7 = threading.Thread(target=MQ7_detect, daemon=True)
    # thread0_MQ7.start()

    thread1_LED = threading.Thread(target=led_action, daemon=True)
    thread1_LED.start()
    thread2_PIEZO = threading.Thread(target=piezo_action, daemon=True)
    thread2_PIEZO.start()

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
        elif (LEVEL == 1):
            ## LED 설정 ##
            rgb_color = [100, 100, 0]   # 색 수치만 넣으면 됨
            led_speed = 1           # LED 깜빡이는 속도

            ## Piezo 설정 ##

            ## Vibration 설정 ##


        #### 2단계 ####
        elif (LEVEL == 2):
            rgb_color = [100, 50, 0]  # 색 수치만 넣으면 됨
            led_speed = 1  # LED 깜빡이는 속도

        #### 3단계 ####
        elif (LEVEL == 3):
            rgb_color = [100, 0, 0]  # 색 수치만 넣으면 됨
            led_speed = 1  # LED 깜빡이는 속도


except KeyboardInterrupt:
    print("Program End")

# 코드가 너무 더러워지나

# 매개변수로 전달? 아니면 global 변수로
# 소스파일 분리(led, piezo, ...)
