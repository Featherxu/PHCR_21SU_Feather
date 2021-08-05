import time
import board
import analogio
from simpleio import map_range

gsr = analogio.AnalogIn(board.A1)

#sensorValue = 0
gsr_average = 0


while True:

    reading = gsr.value

    gsr_average = map_range(reading, 0, 9600, 0, 250)
    gsr_average = int(gsr_average)
    print((gsr, reading))


    #print(gsr_average.value)
    time.sleep(0.1)
