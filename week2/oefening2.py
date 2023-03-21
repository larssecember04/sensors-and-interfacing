from RPi import GPIO
import time

ventilator = 27

difference = 0
gewenst = 0

GPIO.setmode(GPIO.BCM)
GPIO.setup(ventilator,GPIO.OUT)
ventilator_pwm = GPIO.PWM(ventilator,100)


def findtemp():
    time.sleep(0.1)
    log = open("/sys/bus/w1/devices/28-0417b2507eff/temperature")
    temp = log.readline().strip('\n')
    temp = float(temp)/1000
    return temp

def differenceberekening():
    temp = findtemp()
    return(abs(gewenst-temp))

try:
    gewenst = float(input("Geef de gewenste temperatuur in (float): "))
    while True:
        difference = differenceberekening()
        print("Temp: ", findtemp())
        print("Difference: ", differenceberekening())
        if difference <= 2 and difference > 0:
            ventilator_pwm.ChangeDutyCycle(50)
        elif difference > 2:
            ventilator_pwm.ChangeDutyCycle(100)
        else: 
            GPIO.output(ventilator,GPIO.LOW)            

    
except KeyboardInterrupt as e:
    print(e)
    

finally:
    GPIO.cleanup()
    print("script stopped")