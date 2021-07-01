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
pot = rotaryio.IncrementalEncoder(board.A2, board.A3)
photo = analogio.AnalogIn(board.A1)

# declare color variable & fill the pixels with the colors
red = 128
green = 180
blue = 128

TC = red+blue
hue = (red,green,blue)

#color = (0,0,0)
pixels.fill(hue)

#rotary encounter
position_pre = pot.position


# repeat this code 4eva
while True:

    #hue = pot.value

    brightness = photo.value

    delta = pot.position - position_pre
    position_pre = pot.position

    red = red+delta

    if red<=0:
        red=0
    elif red>=255:
        red = 255

    blue = 255-red

    hue = (red,green,blue)
    print(hue)

    # bit shift scale 16-bit to 8-bit value
    #scaled_hue = map_range(hue, 0, 65535, 0, 255)
    #scaled_hue = int(scaled_hue)
    #print("hue=", scaled_hue)

    scaled_bright = map_range(brightness, 20000, 55535, 0, 255)
    scaled_bright = int(scaled_bright)
    print("brightness=", scaled_bright)


    color = fancy.CHSV(hue, 200, scaled_bright)
    packed = color.pack()

    #color = (0, scaled_pot, scaled_photo)

    pixels.fill(packed)

    time.sleep(0.1)
