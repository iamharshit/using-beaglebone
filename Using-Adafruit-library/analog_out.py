#for analog output we send PWM signal on anyone of the 5 PWM pins
#output can be anywhere between 0 to 3.3 V , governed by Duty Cycle of PWM signal

import Adafruit_BBIO.PWM as PWM

pwmPin="P9_14"

PWM.start(pwmPin,0)
PWM.set_duty_cycle(pwmPin,10)

for i in range(0,5):
    sleep(1)
    
PWM.stop(pwmPin)
PWM.cleanup()

#the pwmPin would be having a voltage of 0.33V for 5sec then 0V
#NOTE: instead of using a for loop if i wud have directly done `sleep(5)` that wud have also worked
