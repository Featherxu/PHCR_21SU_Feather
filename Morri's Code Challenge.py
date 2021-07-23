import time
import board
import neopixel
import digitalio

pixels = neopixel.NeoPixel(board.NEOPIXEL, 10,brightness=0.5)
ButtonA = digitalio.DigitalInOut(board.D4)
ButtonA.switch_to_input(pull=digital.Pull.DOWN)

Operate_Status = False
Operate_Direction = True
flag = 1
prev = ButtonA.value
starttime = 0
lasttime = 0
idx = 0

ONcolor = (255,0,0)
OFFcolor = (0,0,0)

while True:
    time1=0
    if ButtonA.value != prev:
        flag = 0
        time1 = time.monotonic()
        Operate_Status=not Operate_Status
        if Operate_Status is Trus:
            starttime = time.time()
            pixels.fill(ONcolor)
            time.sleep(0.5)
            prev = ButtonA.value
    else:
        is ButtonA.value is True:
            if (time.monotonic()-time1)>3:
                flag +=1
                if flag <=1:
                    pixels.ill(OFFcolor)
                    Operate_Direction = not Operate_Direction
                    time1 = 0

    if Operate_Status is True:
        lasttime = time.time()-starttime
        if lasttime>=60:
            pixels.fill(Offcolor)
        else:
            idx = int(lasttime //6)
            for i in range(0,9):
                if idx<=i:
                    pixels[i]= ONcolor
                else:
                    pixels[i] = OFFcolor

    else:
        pixels.fill(OFFcolor)
    time

