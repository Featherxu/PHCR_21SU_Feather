# import modules
import board
import time
import analogio
import neopixel
from simpleio import map_range
import adafruit_fancyled.adafruit_fancyled as fancy


# declare objects
pixels = neopixel.NeoPixel(board.NEOPIXEL, 10)

# declare analong input
pot = analogio.AnalogIn(board.A6)
photo = analogio.AnalogIn(board.A1)

# declare color variable & fill the pixels with the colors
color = (0,0,0)
pixels.fill(color)


# repeat this code 4eva
while True:

    hue = pot.value
    brightness = photo.value


    # bit shift scale 16-bit to 8-bit value
    scaled_hue = map_range(hue, 0, 65535, 0, 255)
    scaled_hue = int(scaled_hue)
    print("hue=", scaled_hue)

    scaled_bright = map_range(brightness, 10000, 40535, 0, 255)
    scaled_bright = int(scaled_bright)
    print("beightness=", scaled_bright)


    color = fancy.CHSV(scaled_hue, 200, scaled_bright)
    packed = color.pack()

    #color = (0, scaled_pot, scaled_photo)

    pixels.fill(packed)

    time.sleep(0.1)
