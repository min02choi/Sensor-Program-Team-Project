import RPi.GPIO as GPIO
import time
import signal
import sys
import threading
import I2C_LCD_driver
import serial

# 시스템 종료
def signal_handler(signal, frame):
    print('process stop')
    GPIO.cleanup()
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)


#### MQ7 ####
# 일산화탄소 수치 감지
def MQ7_detect():
    # 필요하다면 port, brate 을 global로 설정하던가
    global CO_STATE
    global LEVEL

    # CO_STATE 값 측정
    # 근데 이게 값이 조금 이상하게 측정이 됨

    # CO 수치에 따른 LEVEL 설정
    while True:
        mq7_seri = serial.Serial(mq7_port, baudrate=brate, timeout=None)
        print(mq7_seri.name)
        mq7_seri.write(mq7_cmd.encode())

        if mq7_seri.in_waiting != 0:
            content = mq7_seri.readline()
            print(content[:-2].decode())        # 이건 나중에 지워
            CO_STATE = content[:-2].decode()
            time.sleep(0.5)

        # 값은 이후 실험에 의해 수정
        if (28 > CO_STATE):
            LEVEL = 0
        elif (40 > CO_STATE):
            LEVEL = 1
        elif (60 > CO_STATE):
            LEVEL = 2
        else:
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
    global LEVEL
    global rgb_color
    global led_speed

    # 1단계, 2단계, 3단계 LED가 켜지는 시간을 조절할 것 (led_speed)
    while True:
        # 근데 변수를 다 global로 빼면 if문으로 안나눠도 되긴하는데...
        # 코드의 효율성 측면은 나중에 고려. 일단은 동작여부 우선
        # 나중에 기회가 된다면 elif안의 중복되는 코드를 함수로 빼도 될듯
        if (LEVEL == 0):
            setRGB(0, 0, 0)
        elif (LEVEL == 1):
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
            time.sleep(0.2)


#### Piezo ####
# 피에조부저
def piezo_action():
    global LEVEL

    # 구체적인 소리의 Frequency수 조정 필요
    while True:
        if (LEVEL == 0):
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
def vibration_action():
    global LEVEL

    while True:
        if (LEVEL == 0):
            PWM_Vib.ChangeDutyCycle(0)
            time.sleep(1)
        elif (LEVEL == 1):
            PWM_Vib.ChangeDutyCycle(5)
            time.sleep(1)
            PWM_Vib.ChangeDutyCycle(50)
            time.sleep(1)
        elif (LEVEL == 2):
            PWM_Vib.ChangeDutyCycle(5)
            time.sleep(0.5)
            PWM_Vib.ChangeDutyCycle(95)
            time.sleep(0.5)
        elif (LEVEL == 3):
            PWM_Vib.ChangeDutyCycle(100)
            time.sleep(1)


#### LCD ####
def lcd_show():
    global CO_STATE
    global LEVEL

    while True:
        # while문? sleep를 해야하는가? -> 이후 직접 실행해서 판단
        # 화면이 깜빡이는 문제 해결해야 함
        line1 = "CO state: " + str(CO_STATE)
        line2 = "Danger Level: " + str(LEVEL)

        mylcd = I2C_LCD_driver.lcd()
        mylcd.lcd_display_string(line1, 1)
        mylcd.lcd_display_string(line2, 2)
        time.sleep(0.3)


#### DC Motor ####
# 시리얼 통신이라 한 번만 실행 되기만 하면 아두이노에서 도는 방식이라면 쓰레드로 구현 안해도 될 듯
def dcmotor_action():
    dc_com = serial.Serial(port="/dev/ttyACM0", baudrate=9600, bytesize=serial.EIGHTBITS, parity=serial.PARITY_NONE, timeout=1)
    dc_text = "Serial DC Motor"
    dc_com.write(dc_text.encode())


#### Tactile Button ####
def tactile_action():
    global LEVEL

    while True:
        tact_state = GPIO.input(tactile)
        # print(tact_state)
        if (tact_state == False):
            print("Button pressed")
            LEVEL = 0
            setRGB(0, 0, 0)
            PWM_Piezo.ChangeDutyCycle(0)
            PWM_Vib.ChangeDutyCycle(0)
        time.sleep(0.2)


################### 센서&변수 세팅 ################################


GPIO.setmode(GPIO.BCM)

#### MQ7 세팅 ####

CO_STATE = 0
LEVEL = 0

mq7_port = '/dev/ttyACM0'
brate = 9600    # boudrate
mq7_cmd = "temp"


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

rgb_color = [0, 0, 0]       # RGB 색 설정

led_speed = 0               # LED 깜빡이는 속도


#### Piezo ####
piezo = 23
GPIO.setup(piezo, GPIO.OUT)
PWM_Piezo = GPIO.PWM(piezo, 100)
PWM_Piezo.start(100)
# PWM_Piezo.ChangeDutyCycle(20)
PWM_Piezo.ChangeDutyCycle(0)


#### Vibration ####
vibration = 27

GPIO.setup(vibration, GPIO.OUT)
PWM_Vib = GPIO.PWM(vibration, 200)
PWM_Vib.start(7.5)


#### LCD ####
# lcd_show()함수에서 구현 다 함

#### DC Motor ####
dc_port = "/dev/ttyACM0"
# dc_brate = 9700    # boudrate
cd_cmd = "temp"


#### Tactile Button ####
tactile = 16
GPIO.setup(16, GPIO.IN, pull_up_down=GPIO.PUD_UP)


#### Variable ####
# 함수 안에서 global 설정
# 활성화 시킬것


##################### 코드 시작 ##############################

try:
    # 쓰레드 실행
    # 필요 쓰레드: mq7, led, piezo, vibration, lcd, dc motor, tact button, fan

    # thread0_MQ7 = threading.Thread(target=MQ7_detect, daemon=True)
    # thread0_MQ7.start()
    thread1_LED = threading.Thread(target=led_action, daemon=True)
    thread1_LED.start()
    thread2_PIEZO = threading.Thread(target=piezo_action, daemon=True)
    thread2_PIEZO.start()
    thread3_VIBRATION = threading.Thread(target=vibration_action, daemon=True)
    thread3_VIBRATION.start()
    thread4_LCD = threading.Thread(target=lcd_show, daemon=True)
    thread4_LCD.start()
    # thread5_DCMotor
    # thread5_DC = threading.Thread(target=dcmotor_action, daemon=True)
    # thread5_DC.start()

    thread6_TACT = threading.Thread(target=tactile_action, daemon=True)
    thread6_TACT.start()

    # state 설정
    #

    while True:

        # MQ7미완, 일단은 사용자 input으로 값을 받아 실험
        LEVEL = int(input("Enter the Level: "))

        # LEVEL 값에 따른 작동
        if (LEVEL == 0):    # 없애도 될듯?
            temp = 0        # 그냥 적어놓은 코드

        #### 1단계 ####
        elif (LEVEL == 1):
            ## LED 설정 ##
            rgb_color = [100, 100, 0]   # 색 수치만 넣으면 됨
            led_speed = 1           # LED 깜빡이는 속도

        #### 2단계 ####
        elif (LEVEL == 2):
            rgb_color = [100, 50, 0]  # 색 수치만 넣으면 됨
            led_speed = 0.5

        #### 3단계 ####
        elif (LEVEL == 3):
            rgb_color = [100, 0, 0]  # 색 수치만 넣으면 됨
            led_speed = 0


except KeyboardInterrupt:
    print("Program End")

# 코드가 너무 더러워지나

# 매개변수로 전달? 아니면 global 변수로
# 소스파일 분리(led, piezo, ...)
# main(?)이 너무 길어지는 현상...?
