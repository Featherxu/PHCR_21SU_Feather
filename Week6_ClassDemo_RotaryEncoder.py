import board
import time
import neopixel
import rotaryio

pixels= neopixel.NeoPixel(board.NEOPIXEL, 10,brightness=0.1)
encoder = rotaryio.IncrementalEncoder(board.A1, board.A2)

color = [0,0,0]

# repeat this code forever
while True:
    print("Pos is":, encoder.position)

    if encoder.position>255:
        encoder.position = 255
    elif encoder.position <255:
        encoder.position = 0

    color[0] = encoder.position
    print("Red is:",color[0])
    pixels.fill(color)


    time.sleep(0.05)
