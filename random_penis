import ssd1306
import machine
import time
import random


WIDTH = 128
HEIGHT = 64
i2c = machine.I2C(0)

oled = ssd1306.SSD1306_I2C(WIDTH, HEIGHT, i2c)

oled.fill(0)
oled.text("MicroPython", 20, 0)
oled.text("OLED on Pi Pico", 2, 10)
oled.text("loading...", 0, 30)
oled.show()
time.sleep(1)

while True:
    oled.fill(0)
    xrnd = random.randrange(0, 90)
    yrnd = random.randrange(0, 55)
    oled.text("penis", xrnd, yrnd)
    oled.show()
   
