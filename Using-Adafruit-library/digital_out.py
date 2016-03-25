#output can only be high(3.3V) or low(0V)

import Adafruit_BBIO.GPIO as GPIO
from time import sleep

outPin="P9_12"

GPIO.setup(outPin,GPIO.OUT)

for i in range(0,5):
      GPIO.output(outPin,GPIO.HIGH)
      sleep(1)
      GPIO.output(outPin,GPIO.LOW)
      sleep(1)

GPIO.cleanup()
