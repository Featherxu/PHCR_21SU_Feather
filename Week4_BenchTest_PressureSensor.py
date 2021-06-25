import board
import time
import analogio
import neopixel
from simpleio import map_range

pixels = neopixel.NeoPixel(board.NEOPIXEL, 10)

pressure = analogio.AnalogIn(board.A1)
pot = analogio.AnalogIn(board.A6)

color = (0,0,0)
pixels.fill(color)


while True:

    reading = pot.value
    reading = pressure.value

    print(pot.value)
    print(pressure.value)
    time.sleep(0.1)
