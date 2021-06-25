import board
import time
import touchio
import neopixel

touchPin1 = touchio.TouchIn(board.A1)
touchPin2 = touchio.TouchIn(board.A2)
touchPin3 = touchio.TouchIn(board.A3)
touchPin4 = touchio.TouchIn(board.A4)
touchPin5 = touchio.TouchIn(board.A5)
touchPin6 = touchio.TouchIn(board.A6)
touchPinTX = touchio.TouchIn(board.TX)

touchPins = [touchPin1,touchPin2,touchPin3,touchPin4,touchPin5,touchPin6,touchPinTX ]

touchVals = [False,False,False,False,False,False,False,]

pixels = neopixel.NeoPixel(board.NEOPIXEL,10)
COLOR = (0,25,255)
CLEAR = (0,0,0)

while True:
    for x in range(7):
        touchVals[x] = touchPins[x].value
    print(touchVals)

    #do neopixel out with for loop
    for x in range (7):
        if touchPins[x].value ==True:
            pixels[x] =COLOR
        else:
            pixels[x]=CLEAR



    time.sleep(0.1)

