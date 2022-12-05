import RPi.GPIO as GPIO
import time

from Team_Project.New_Team_Project import PWM_RED, PWM_GREEN, PWM_BLUE, LEVEL, rgb_color, led_speed


def setRGB(r, g, b):
    PWM_RED.ChangeDutyCycle(r)
    PWM_GREEN.ChangeDutyCycle(g)
    PWM_BLUE.ChangeDutyCycle(b)

# LED 깜빡임
def led_action():
    # 정하셈 변수들을 global로 뺼지 말지
    # 근데 LEVEL도 안 빼도 될거같긴 함

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
        if (LEVEL == 1):
            setRGB(rgb_color[0], rgb_color[1], rgb_color[2])
            time.sleep(led_speed)
            setRGB(0, 0, 0)
            time.sleep(0.5)
        if (LEVEL == 2):
            setRGB(rgb_color[0], rgb_color[1], rgb_color[2])
            time.sleep(led_speed)
            setRGB(0, 0, 0)
            time.sleep(0.3)
        if (LEVEL == 3):
            setRGB(rgb_color[0], rgb_color[1], rgb_color[2])
            time.sleep(led_speed)
            setRGB(0, 0, 0)
            time.sleep(0.2)

