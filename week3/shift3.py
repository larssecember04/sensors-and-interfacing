from RPi import GPIO
import time



GPIO.setmode(GPIO.BCM)

teVersturenByte = 0b10101010

for i in range(0,8):
    byte = teVersturenByte & 0x80
    teVersturenByte = teVersturenByte << 1
    print(byte/128)
    time.sleep(1)