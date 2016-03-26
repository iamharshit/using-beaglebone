#analog input means a value between 0 to 1.8V comes at input pin
#if more then 1.8V is inputed the beagle would burn out
#beagle have 7 ADC pins, from P9_33 to P9_40 excluding P9_34

import Adafruit_BBIO.ADC as ADC
from  time import sleep

adcPin="P9_33"

ADC.setup()

while True:
    value = ADC.read(adcPin)
    voltage_at_adc = value*1.8
    print "voltage at adc pin :",voltage_at_adc
    sleep(.5)
    
#Note :the adc pin read voltage relative to 1.8V, i.e value read by adc = voltage input at ADC / 1.8
#therefore actual voltage at ADC = value read by ADC * 1.8 

