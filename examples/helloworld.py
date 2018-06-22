import i2c_lcd
from machine import I2C

i2c = I2C(0, I2C.MASTER)
i2c.init(I2C.MASTER, baudrate=100000)
d = i2c_lcd.Display(i2c)

d.home()
d.write('Hello World')
