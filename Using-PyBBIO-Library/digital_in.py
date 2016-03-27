from bbio import *

inPin="GPIO2_3"

def setup():
    pinMode(inPin,INPUT)

def loop():
    state = digitalRead(inPin)
    print state
    delay(1000)

run(setup,loop)
