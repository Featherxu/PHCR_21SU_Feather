import time
import board
import analogio
import neopixel
from simpleio import map_range

gsr = analogio.AnalogIn(board.A1)
pixels = neopixel.NeoPixel(board.NEOPIXEL, 10,auto_write = False)

colors = [(43,108,252),
             (95,88,240),
             (133,74,232),
             (174,59,223),
             (212,45,214),

             (255,29,204),
             (255,22,163),
             (255,16,122),
             (255,9,80),
             (255,3,38),

 ]

#pixels.brightness = 0.1


pixels.show()
time.sleep(1)

#sensorValue = 0



while True:
    gsr_average = 0

    for x in range(10):
        gsr_average += gsr.value
        time.sleep(0.005)

    gsr_average /= 10

    print((gsr_average,))
    #print(gsr_average.value)
    time.sleep(0.1)

    if gsr_average < 9000:
        for x in range(len(pixels)):
            pixels[x]= colors[x]
        popColor = colors.pop(0)
        colors.append(popColor)
    else:
        pixels.fill(0)



    pixels.show()
    time.sleep(0.1)

