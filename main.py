from max6675 import MAX6675  # https://github.com/BetaRavener/micropython-hw-lib/tree/master/MAX6675
from machine import Pin
from utime import sleep

# difinition des broches du Raspberry Pi Pico
sck = Pin(13, Pin.OUT)
cs = Pin(14, Pin.OUT)
so = Pin(15, Pin.IN) 

thermocouple = MAX6675(sck, cs , so)

while True:
    mesure = thermocouple.read()
    print('Temperature:', "{0:1.1f}".format(mesure), '°C = ',
          "{0:1.1f}".format(mesure + 273.15), ' K')
    sleep(1)
