# 在这里写上你的代码 :-)
import board
import time
import analogio
import neopixel
from simpleio import map_range

pixels = neopixel.NeoPixel(board.NEOPIXEL,10)

knob = analogio.AnalogIn(board.A1)

color = (0,0,0)
pixels.fill(color)

while True:
    reading = knob.value

    print(knob.value)
    time.sleep(0.1)

