import time
import board
import analogio
from simpleio import map_range

gsr = analogio.AnalogIn(board.A1)

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

