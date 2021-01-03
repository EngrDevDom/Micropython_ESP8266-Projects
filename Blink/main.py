from machine import Pin
from time import sleep

LED = Pin(2, Pin.OUT) # Set the LED pin 2

# Blinks the LED 10 times every reset
for _ in range(100):
    LED.value(0)  # Set the LED OFF
    sleep(0.5)
    LED.value(1)  # Set the LED ON
    sleep(0.5)
