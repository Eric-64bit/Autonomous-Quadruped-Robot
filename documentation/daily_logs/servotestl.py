import RPi.GPIO as GPIO
import time

# 设置 GPIO 编号方式
GPIO.setmode(GPIO.BCM)

# 舵机信号连接的 GPIO
servo_pin = 18

# 设置 GPIO 为输出
GPIO.setup(servo_pin, GPIO.OUT)

# 设置 PWM，频率 50Hz
pwm = GPIO.PWM(servo_pin, 50)
pwm.start(0)  # 初始化占空比为0

def set_angle(angle):
    duty = angle / 18 + 2   # 转换角度到占空比
    GPIO.output(servo_pin, True)
    pwm.ChangeDutyCycle(duty)
    time.sleep(0.5)
    GPIO.output(servo_pin, False)
    pwm.ChangeDutyCycle(0)

try:
    while True:
        # 测试舵机 0° -> 90° -> 180°
        set_angle(0)
        time.sleep(1)
        set_angle(90)
        time.sleep(1)
        set_angle(180)
        time.sleep(1)

except KeyboardInterrupt:
    print("测试结束")

finally:
    pwm.stop()
    GPIO.cleanup()