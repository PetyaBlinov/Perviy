import RPi.GPIO as gpio
import time
gpio.setwarnings(False)
gpio.setmode(gpio.BCM)
led=26
gpio.setup(led,gpio.OUT)
photo=6
gpio.setup(photo,gpio.IN)
while True:
    if gpio.input(photo)==0:
        gpio.output(led,1)
    else:
        gpio.output(led,0)
    time.sleep(0.1)
