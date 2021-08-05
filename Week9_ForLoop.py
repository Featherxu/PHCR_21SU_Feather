# 在这里写上你的代码 :-)
import board
import neopixel
import time

pixels = neopixel.NeoPixel(board.NEOPIXEL,10)

#pixel_index = [x for x in range(10)]

BLUE= (0,0,255)
RED = (255,0,0)

#knob = analogio.AnalogIn()

while True:
    for x in range(10):
        pixels.fill(0)
        pixels[x] = BLUE
        time.sleep (1)

    pixels.fill(RED)
    time.sleep(1)
