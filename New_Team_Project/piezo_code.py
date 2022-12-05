import time

from Team_Project.New_Team_Project import PWM_Piezo


def piezo_action():
    global LEVEL

    while True:
        if (LEVEL == 0):
            PWM_Piezo.changeDutyCycle(20)
            time.sleep(1)
            PWM_Piezo.changeDutyCycle(0)
            time.sleep(1)
        if (LEVEL == 1):
            PWM_Piezo.changeDutyCycle(20)
            time.sleep(1)
            PWM_Piezo.changeDutyCycle(0)
            time.sleep(1)
        if (LEVEL == 2):
            PWM_Piezo.changeDutyCycle(20)
            time.sleep(1)
            PWM_Piezo.changeDutyCycle(0)
            time.sleep(1)
        if (LEVEL == 2):
            PWM_Piezo.changeDutyCycle(20)
            time.sleep(1)
            PWM_Piezo.changeDutyCycle(0)
            time.sleep(1)

