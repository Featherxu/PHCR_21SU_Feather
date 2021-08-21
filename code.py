# filesystem is mounted with boot.py script
import board
import time
from digitalio import DigitalInOut, Direction, Pull
import analogio
import neopixel
import microcontroller
import storage

# initialize neopixel indicator light
pixel = neopixel.NeoPixel(board.NEOPIXEL, 1)
pixel.brightness = 0.1
pixel.fill(0xff0000)

# initialize a digital pin to manually disable read-only access to the file system
write_en = DigitalInOut(board.D7)
write_en.direction = Direction.INPUT
write_en.pull = Pull.UP
write_en_pre = write_en.value

next_time = time.monotonic()
time_inc = 1

gsr = analogio.AnalogIn(board.A1)

while True:
    # get the current time
    this_time = time.monotonic()
    # check if it is time to log a datapoint
    if this_time >= next_time:
        pixel.fill(0x0000ff)
        # set the next time to log a data datapoint
        next_time = time.monotonic() + time_inc

        # collect data
        # get the cpu temperature
        #temp_cpu = microcontroller.cpu.temperature

        gsr_average = 0

        for x in range(10):
            gsr_average += gsr.value
            time.sleep(0.005)

        gsr_average /= 10
        print(gsr_average)

        # format a data string and print it for # DEBUG:
        ds = '{:f},{:-}\n'.format(this_time, gsr_average)
        print(ds)

        # sleep so you can see the status led blink:
        time.sleep(0.1)
        print(write_en.value)

        # if the write_en pin is low the file system is available (FOR DEBUG)
        if not write_en.value:
            print("Attempting to write Data")
            pixel.fill(0)
            # try to open the data_log file, then format and write the data
            try:
                with open("/data_log.txt", "a") as dl:
                    dl.write(ds)
                    dl.flush()
                    for x in range(4):
                        pixel.fill(0x00ff00)
                        time.sleep(0.1)
                        pixel.fill(0)
                        time.sleep(0.1)
                    print("Data Written")
            except OSError as e:
                for x in range(10):
                    pixel.fill(0xff00ff)
                    time.sleep(0.1)
                    pixel.fill(0)
                    time.sleep(0.1)
                print("Data not written")
    else:
        pixel.fill(0x00ff00)

