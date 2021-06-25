import board
import time
import touchio
import neopixel

#connect to touchPins
touchPin1 = touchio.TouchIn(board.A1)

touchPin2 = touchio.TouchIn(board.A2)
touchPin3 = touchio.TouchIn(board.A3)

touchPin4 = touchio.TouchIn(board.A4)
touchPin5 = touchio.TouchIn(board.A5)

touchPin6 = touchio.TouchIn(board.A6)
touchPinTX = touchio.TouchIn(board.TX)

touchPins = [touchPin1,touchPin2,touchPin3,touchPin4,touchPin5,touchPin6,touchPinTX ]

touchVals = [False,False,False,False,False,False,False,]

#neopixel stuff
pixels = neopixel.NeoPixel(board.NEOPIXEL,7)
# COLOR = (0,25,255)
#COLOR = ("Red","Green","Blue")
CLEAR = (0,0,0)
my_R = 255
my_G = 255
my_B = 255

my_color = [0,0,0]

light_mode = False
touch1Pre = touchVals[0]


while True:

    for x in range (7):
        touchVals[x] = touchPins[x].value
        print(touchVals)

    #capture touch input
    # touchVal1 = touchPin1.value


    for x in range(1,7):
        if touchVals[x] == True:
            if x ==1:
                pixels.fill(tuple(my_color))
                my_R = my_R - 10
                if my_R < 0:
                    my_R = 0
            elif x==2:
                pixels.fill(tuple(my_color))
                my_R = my_R + 10
                if my_R > 255:
                    my_R = 255
            elif x==3:
                pixels.fill(tuple(my_color))
                my_G = my_G - 10
                if my_G < 0:
                    my_G = 0
            elif x==4:
                pixels.fill(tuple(my_color))
                my_G = my_G + 10
                if my_G > 255:
                    my_G = 255
            elif x==5:
                pixels.fill(tuple(my_color))
                my_B = my_B - 10
                if my_B < 0:
                    my_B = 0
            elif x==6:
                pixels.fill(tuple(my_color))
                my_B = my_B + 10
                if my_B > 255:
                    my_B = 255

            my_color = [my_R, my_G, my_B]

    if touchVals[0]!=touch1Pre:
        touch1Pre = touchVals[0]
        if touchVals[0] ==True:
            light_mode = not light_mode



    if light_mode == True:
        pixels.fill(my_color)
    else:
        pixels.fill(CLEAR)







    time.sleep(0.1)
