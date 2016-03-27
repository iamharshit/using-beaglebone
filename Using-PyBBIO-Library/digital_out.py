#PyBBIO specially designed for those who learn Beaglebone after learning Arduino

from bbio import *

outPin="GPIO2_3"

def setup():
    pinMode(outPin,OUTPUT)
    
def loop():
    digitalWrite(outPin,HIGH)
    delay(1000)
    digitalWrite(outPin,LOW)
    delay(1000)
    
run(setup,loop)
