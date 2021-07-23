import time
import board
import neopixel
import digitalio

# Declare variables
pixels = neopixel.NeoPixel(board.NEOPIXEL, 10, brightness=0.05)
button_a = digitalio.DigitalInOut(board.BUTTON_A)
button_a.switch_to_input(pull=digitalio.Pull.DOWN)


color_list = [(255, 0, 0), (227, 28, 0),
             (198, 57, 0), (170, 85, 0),
             (142, 113, 0), (113, 142, 0),
             (85, 170, 0), (57, 198, 0),
             (28, 227, 0), (0, 255, 0)]

# button_time = time.monotonic()
# button_int = 0.1
buttonState = 0
prevButtonInput = False
timeInterval = 6
timeOut = time.monotonic()
buttonPressTime = 0;
resetMode = False

RUN = 2
PAUSE = 1
RESET = 0

mode = RESET

starttime = 0

# light up all the pixels
for i in range(10):
    pixels[i] = color_list[i]

elapsedtime = 0

while True:
    # toggle button A
    buttonInput = button_a.value

    # compare the button state to previous button state
    if buttonInput != prevButtonInput:
        # the button state has changed, reset the previous state
        prevButtonInput = buttonInput
        # check if the button state is true...
        if buttonInput:
            # (changed from false to true) button pressed
            # mark Button pressed time
            buttonPressTime = time.monotonic()
        else:
            # (changed from true to false) button released
            if mode == RUN:
                mode = PAUSE
                elapsedtime = time.monotonic() - starttime
                pause_time = time.monotonic()
                print(elapsedtime)
                print("timer paused")
            elif mode == PAUSE:
                mode = RUN
                starttime += time.monotonic() - pause_time
                print("timer run")
            elif mode == RESET:
                print("timer run")
                mode = RUN
                starttime = time.monotonic()
    else:
        # no change detected the button is either pushed down or not
        if buttonInput:
            # the button is held down
            if time.monotonic() >= buttonPressTime + 2:
                # the button is held down for at least 2 seconds
                print("Resetting..")
                mode = RESET

    if mode == RUN:
        elapsedtime = time.monotonic() - starttime
        print(elapsedtime)
        if elapsedtime >= 60:
            pixels.fill(0)  # Prevent timer exceeds 60sec
        else:
            # calculate how many pixels to light up
            idx = int(elapsedtime // 6)
            # light up the right number of pixels
            for i in range(10):
                if idx <= i:
                    pixels[i] = color_list[i]
                else:
                    pixels[i] = 0

    time.sleep(0.01)
