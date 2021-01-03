from machine import Pin

led = Pin(5, Pin.OUT)

button = Pin(4, Pin.IN, Pin.PULL_UP)

def debounce(pin):
    prev = None
    for _ in range(32):
        current_value = pin.value()
        if prev != None and prev != current_value:
            return None
        prev = current_value
    return prev

def button_callback(pin):
    if debounce(pin) == None:
        return
    elif not debounce(pin):
        led.value(not led.value())

button.irq(trigger=Pin.IRQ_FALLING, handler=button_callback)
