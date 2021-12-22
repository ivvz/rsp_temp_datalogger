from machine import Pin, SPI
from max6675 import MAX6675  # https://github.com/BetaRavener/micropython-hw-lib/tree/master/MAX6675
import os
from utime import sleep
import sdcard

led = machine.Pin(25,machine.Pin.OUT)
# Toggle LED functionality
def BlinkLED(timer_one):
    led.toggle()
# Initialize the SD card
spi=SPI(1,baudrate=40000000,sck=Pin(10),mosi=Pin(11),miso=Pin(12))
sd=sdcard.SDCard(spi,Pin(9))
# Create a instance of MicroPython Unix-like Virtual File System (VFS),
vfs=os.VfsFat(sd)

# Mount the SD card
os.mount(sd,'/sd')

# definiendo pines max6675
sck = Pin(13, Pin.OUT)
cs = Pin(14, Pin.OUT)
so = Pin(15, Pin.IN) 

thermocouple = MAX6675(sck, cs , so)

file = open("/sd/carga1102.csv","w")
file.write("lectura,termopar1\n")
file.close()

reading = 1
while reading < 100:
    file = open("/sd/carga1102.csv","a")
    mesure = thermocouple.read()
    file.write("%s," % reading)
    file.write("%s\r\n" % mesure)
    file.close()
    print("temperature = ", mesure, " C")
    reading +=1
    sleep(2)
    

