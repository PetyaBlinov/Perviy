import RPi.GPIO as gpio
import time
gpio.setwarnings(False)
gpio.setmode(gpio.BCM)
leds=[16,12,25,17,27,23,22,24]
gpio.setup(leds,gpio.OUT)
gpio.output(leds,0)
light_time=0.2
up=9
down=10
gpio.setup(up,gpio.IN)
gpio.setup(down,gpio.IN)
num=0
def dec2bin(value):
    return[int(element) for element in bin(value)[2:].zfill(8)]
sleep_time=0.2
if gpio.input(up):
    num=num+1
    print(num,dec2bin(num))
    time.sleep(sleep_time)
if gpio.input(down):
    num=num-1
    print(num,dec2bin(num))
    time.sleep(sleep_time)