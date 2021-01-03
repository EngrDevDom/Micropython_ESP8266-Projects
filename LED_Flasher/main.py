from machine import Pin
from time import sleep

led0 = Pin(3, Pin.OUT)
led1 = Pin(4, Pin.OUT)
led2 = Pin(5, Pin.OUT)
led3 = Pin(6, Pin.OUT)
led4 = Pin(7, Pin.OUT)

# LED 0
led0.value(0)
sleep(0.25)
led0.value(1)
sleep(0.25)

