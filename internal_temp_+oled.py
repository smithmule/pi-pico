import ssd1306
import machine
import time

print("loading")
WIDTH = 128
HEIGHT = 64
times = 0
i2c = machine.I2C(0)
sensor = machine.ADC(4)
conversion_factor = 3.3 / (65535)

oled = ssd1306.SSD1306_I2C(WIDTH, HEIGHT, i2c)
oled.fill(0)

oled.text("MicroPython", 15, 0)
oled.text("on Pi Pico", 20, 10)
oled.text("OLED+TEMP", 29, 30)
oled.text("v0.1", 40,40)
oled.text("01/02 2021", 25, 50)
oled.show()
time.sleep(5)

while True:
    reading = sensor.read_u16() * conversion_factor
    temperature = 27 - (reading - 0.706)/0.001721
    
    oled.fill(0)
    oled.text("smithmule", 0, 0)
    oled.text("was here 2021", 0, 10)
    oled.text("Clock cycles:", 0, 20)
    oled.text(str(times), 0, 30)
    oled.text("Temperature:", 0, 40)
    oled.text(str(temperature)+" C", 24, 50)
    times = times + 1
    oled.show()

