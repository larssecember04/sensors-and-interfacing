from RPi import GPIO
import time

led = 27

GPIO.setmode(GPIO.BCM)
GPIO.setup(led, GPIO.OUT)
led_pwm = GPIO.PWM(led,1000)

led_pwm.start(10)

time.sleep(5)

led_pwm.ChangeDutyCycle(100)

time.sleep(5)

led_pwm.ChangeDutyCycle(100)

time.sleep(5)

led_pwm.ChangeDutyCycle(1)

time.sleep(5)

led_pwm.stop()
GPIO.cleanup()