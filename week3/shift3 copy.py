from RPi import GPIO
import time



GPIO.setmode(GPIO.BCM)

teVersturenByte = 0b10101010
mask = 1

for i in range(0,8):
    byte = teVersturenByte & mask
    teVersturenByte = mask << 1
    if (byte == 0):
        print("0")
    else:
        print("1")
    time.sleep(1)