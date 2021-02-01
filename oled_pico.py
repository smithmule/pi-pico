import ssd1306
import machine
import time
import uos

print(uos.uname())
print("Freq: "  + str(machine.freq()) + " Hz")
print("128x64 SSD1306 I2C OLED on Raspberry Pi Pico")

WIDTH = 128
HEIGHT = 64
times = 0
i2c = machine.I2C(0)

print("Available i2c devices: "+ str(i2c.scan()))
oled = ssd1306.SSD1306_I2C(WIDTH, HEIGHT, i2c)
oled.fill(0)

oled.text("MicroPython", 0, 0)
oled.text("OLED on Pi Pico", 0, 10)
oled.text("loading...", 0, 20)
oled.show()
time.sleep(5)

while True:
    oled.fill(0)
    oled.text("smithmule", 0, 0)
    oled.text("was here 2021", 0, 10)
    oled.text("Clock cycles:", 0, 20)
    oled.text(str(times), 0, 30)
    times = times + 1
    oled.show()
    
