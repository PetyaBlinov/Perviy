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
while True:
    gpio.output(leds,dec2bin(num))
    if gpio.input(up) and gpio.input(down):
        num=255
    elif gpio.input(up):
        num=num+1
        if num>255:
            num=0
        print(num,dec2bin(num))
        time.sleep(sleep_time)
        gpio.output(leds,dec2bin(num))
    elif gpio.input(down):
        num=num-1
        if num<0:
            num=0
        print(num,dec2bin(num))
        time.sleep(sleep_time)
        gpio.output(leds,dec2bin(num))
    time.sleep(0.01)
