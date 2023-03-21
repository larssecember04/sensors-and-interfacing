from RPi import GPIO
import time

btn = 27
rodeled1 = 20
rodeled2 = 21
witteled = 26
timer = 0
btnprevstatus = 0

GPIO.setmode(GPIO.BCM)

GPIO.setup(rodeled1,GPIO.OUT)
GPIO.setup(rodeled2,GPIO.OUT)
GPIO.setup(witteled,GPIO.OUT)
GPIO.setup(btn,GPIO.IN, pull_up_down=GPIO.PUD_UP)

try:
    while True:
        if timer == 0:
            GPIO.output(rodeled1,GPIO.LOW)
            GPIO.output(rodeled2,GPIO.LOW)            
            GPIO.output(witteled,GPIO.HIGH)
            time.sleep(1)
            GPIO.output(witteled,GPIO.LOW)
            time.sleep(1)
        else:
            timer -= 1
            GPIO.output(rodeled1,GPIO.HIGH)
            GPIO.output(rodeled2,GPIO.LOW)
            time.sleep(0.5)
            GPIO.output(rodeled1,GPIO.LOW)
            GPIO.output(rodeled2,GPIO.HIGH)
            time.sleep(0.5)
            print(timer)
            
            
            
        btnstatus = GPIO.input(btn)
        if btnprevstatus == 1 and btnstatus == 0:
            timer += 10
            print(timer)
        btnprevstatus = btnstatus
        
            
            
            
    
    
except KeyboardInterrupt as e:
    print(e)
    GPIO.output(rodeled1,GPIO.LOW)
    GPIO.output(rodeled2,GPIO.LOW)
    GPIO.output(witteled,GPIO.LOW)
    

finally:
    GPIO.cleanup()
    print("script stopped")