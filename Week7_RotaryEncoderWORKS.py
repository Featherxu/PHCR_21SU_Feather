# import modules
import board
import time
import analogio
import neopixel
from simpleio import map_range
import adafruit_fancyled.adafruit_fancyled as fancy
import rotaryio


# declare objects
pixels = neopixel.NeoPixel(board.NEOPIXEL, 10)

# declare input
encoder = rotaryio.IncrementalEncoder(board.A2, board.A3)
photo = analogio.AnalogIn(board.A1)


my_colors = [(255,125,0),
          (255,138,25),
         (255,151,50),
          (255,164,75),
          (255,177,100),
          (255,190,125),
          (255,203,150),
          (255,216,175),
          (255,229,200),
          (255,242,225),

          (255,255,255),

          (225,242,255),
          (200,229,255),
          (175,216,255),
          (150,203,255),
          (125,190,255),
          (100,177,255),
          (75,164,255),
          (50,151,255),
          (25,138,255),
          (0,125,255),
          ]


POSMIN = 0
POSMAX = 20

brightness = photo.value
encoder.position = 10


# repeat this code
while True:
    print(brightness)
    count = encoder.position

    if count<=POSMIN:
        count = POSMIN
    elif count>=POSMAX:
        count = POSMAX

    color = my_colors[count]

    print(encoder.position)
    print(count)
    print(color)

    scaled_hue = encoder.position

    pixels.fill(color)


    time.sleep(0.1)
