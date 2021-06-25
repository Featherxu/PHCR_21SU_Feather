# import modules
import board
from digitalio import DigitalInOut, Direction
import time


# declare objects and variables
led = DigitalInOut(board.D13)
led.direction = Direction.OUTPUT

#variables to control sleep time for blinking
#onTime
#offTime

# loop forever
while True:
    # turn the led off
    led.value = True
    time.sleep(2)
    # turn the led off
    led.value = False
    time.sleep(2)
