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

# declare analong input
#pot = analogio.AnalogIn(board.A6)
encoder = rotaryio.IncrementalEncoder(board.A2, board.A3)
photo = analogio.AnalogIn(board.A1)

NUM_LED = 10
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
          (100,77,255),
          (75,164,255),
          (50,151,255),
          (25,138,255),
          (0,125,255),
          ]


#color = (0,0,0)
POSMIN = 0
POSMAX = 21

brightness = photo.value

count = encoder.position
color = my_colors[encoder.position]
# declare color variable & fill the pixels with the colors
encoder.position = 10


# repeat this code 4eva
while True:

    encoder.position = 10
    RED = (255, 0, 0)

    for x in range(encoder.position):
        #if count = encoder.position:
        pixels.fill(count)

        if encoder.position != encoder.position:
            pixels.fill(color)

        #for x in range(NUM_LED):
            # pixels[20-x] = (0, 0, 0)
           # pixels[x] = (



    if count<=POSMIN:
        count = POSMIN
    elif count>=POSMAX:
        count = POSMAX

    print(color)

    # bit shift scale 16-bit to 8-bit value
    #scaled_hue = map_range(hue, 0, 65535, 0, 255)
    scaled_hue = encoder.position
    #scaled_hue = int(scaled_hue)
    #print("hue=", scaled_hue)

    #scaled_bright = map_range(brightness, 20000, 55535, 0, 255)
    #scaled_bright = int(scaled_bright)
    scaled_bright = 200
    print("brightness=", scaled_bright)


    color = fancy.CHSV(encoder.position, 200, scaled_bright)
    packed = color.pack()

    #color = (0, scaled_pot, scaled_photo)

    pixels.fill(packed)

    time.sleep(0.1)
