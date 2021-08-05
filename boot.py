# boot.py
# boot script to mount file system for circuitpyton to log data
import board
from digitalio import DigitalInOut, Direction, Pull
import neopixel
import storage

print("executing boot script")

# initialize neopixel indicator light
pixel = neopixel.NeoPixel(board.NEOPIXEL, 1)
pixel.brightness = 0.1
pixel.fill(0xff0000)

# initialize a digital pin to manually disable read-only access to the file system
write_en = DigitalInOut(board.D7)
write_en.direction = Direction.INPUT
write_en.pull = Pull.UP
write_en_pre = write_en.value

if not write_en.value:
    print("File System Mounted")
    storage.remount("/", False)
    pixel.fill(0x00ff00)
else:
    print("Filesystem not mounted")
    pixel.fill(0xff7700)
