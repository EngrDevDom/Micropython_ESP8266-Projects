from machine import Pin
from time import sleep

led = Pin(5, Pin.OUT)

for _ in range(10):
    led.value(1)
    sleep(0.5)
    led.value(0)
    sleep(0.5)

