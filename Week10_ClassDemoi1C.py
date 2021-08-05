import time
import board
import busio
import adafruit_am2320

# create an i2c object
i2c = board.I2C()
# create a sensor instance with the i2c object
am = adafruit_am2320.AM2320(i2c)

while True:
    print("Temperature is: ", am.temperature)
    print("Humidity is: ", am.relative_humidity)
    print()

    time.sleep(1)
