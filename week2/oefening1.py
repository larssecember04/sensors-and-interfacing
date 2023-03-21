from RPi import GPIO
import time
GPIO.setmode(GPIO.BCM)

TempReader = 4
led = 6
GPIO.setup(led, GPIO.OUT)
pwm_led1 = GPIO.PWM(led,  1000)
pwm_led1.start(0)
time.sleep(3)

pwm_led1.start(1)

pwm_led1.start(20)
time.sleep(3)
pwm_led1.start(1)
time.sleep(3)
pwm_led1.start(30)


while True:
    time.sleep(0.1)
    log = open("/sys/bus/w1/devices/28-0417b2507eff/temperature")
    temp = log.readline().strip('\n')
    temp = float(temp)/1000
    print("Temperatuur: ", f"{round(temp, 1)} graden")