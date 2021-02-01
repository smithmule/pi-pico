from machine import Pin
from machine import Timer

tim = Timer()

def tick(timer):
    led = Pin(25, Pin.OUT)
    led.toggle()
    
tim.init(freq=10, mode=Timer.PERIODIC, callback=tick)
