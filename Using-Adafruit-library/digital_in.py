import Adafruit_BBIO.GPIO as GPIO
from time import sleep

inPin="P9_12"

GPIO.setup(inPin,GPIO.IN)

for i in range (0,3): 
    GPIO.input(inPin)
    sleep(1)

GPIO.cleanup()
