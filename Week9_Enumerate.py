# 在这里写上你的代码 :-)
import board
import neopixel
import time

pixels = neopixel.NeoPixel(board.NEOPIXEL,10,auto_write=False)


colorList = [(255,0,0),(227,28,0),
              (198,57,0),(170,85,0),
              (142,113,0),(113,42,0),
              (85,170,0),(57,198,0),
              (28,227,0),(0,255,0)]

pixels.fill(0)

knob = analogio.AnalogIn(board.A1)

while True:

    level = int(knob.value/65000*10)
    print("Level is",level)

    for index,color in enumerate(colorList,level):
        print(index,color)
        pixels[index]=color


    pixels.show()
    color_list.append(color_list.pop(0))
    time.sleep(0.01)
