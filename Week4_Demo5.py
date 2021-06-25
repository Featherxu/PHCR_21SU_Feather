import board
import time
import neopixel

pixels = neopixel.NeoPixel(board.NEOPIXEL, 10,auto_write = False)

colors = [(0,255,0),(28,227,0),
            (56,199,0),(84,171,0),
            (112,143,0),(140,115,0),
            (168,87,0),(196,59,0),
            (224,31,0),(255,0,0)]

for x in range(len(pixels)):
    pixels[x]= colors[x]


pixels.show()
time.sleep(1)

while True:
    popColor = colors.pop(0)

    colors.append(popColor)
    for x in range(len(pixels)):
        pixels[x]=colors[x]

    pixels.show()
    time.sleep(0.1)
