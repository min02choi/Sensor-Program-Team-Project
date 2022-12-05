import time

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
