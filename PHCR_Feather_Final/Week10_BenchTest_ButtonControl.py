import board
import time
import analogio
from digitalio import DigitalInOut,Direction




knob = analogio.AnalogIn(board.A1)
#knob.direction = Direction.INPUT

button = DigitalInOut(board.A2)
button.direction = Direction.INPUT

led = DigitalInOut(board.D13)
led.direction = Direction.OUTPUT


while True:
    reading = knob.value
    reading = button.value
    print(knob.value)
    print(button.value)

    led.value = button.value
    time.sleep(0.1)

