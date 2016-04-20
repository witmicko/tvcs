import time

from Adafruit_PWM_Servo_Driver import PWM
from Servo import Servo


if __name__ == '__main__':
    # mg995
    # servo2 = Servo(channel=0, min=10, max=500, freq=50) # mg995

    # sg90
    # Servo pan
    servo2 = Servo(channel=2, min=250, max=410, freq=50)

    # sg90 2
    # servo tilt
    # servo2 = Servo(channel=1, min=120, max=500, freq=50)
    servo3 = Servo(channel=1, min=250, max=327, freq=50)

    time.sleep(2)
    servo2.move_to(0)
    servo3.move_to(0)
    #
    time.sleep(2)
    servo2.move_to(1)
    servo3.move_to(1)

    # for i in range(11):
    #     # print i
    #     dc = i / 10.0
    #     print dc
    #     servo.move_to(dc)
    #     servo1.move_to(dc)
    #     servo2.move_to(dc)
    #     time.sleep(0.3)

    # time.sleep(0.5)

    # servo1.move_to(0)
    # servo2.move_to(0)
    #
    time.sleep(1)
    pwm = PWM(0x40)
    pwm.setPWMFreq(50)
    pwm.softwareReset()
    print('done')
