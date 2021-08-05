import board
import terminalio
import displayio
from adafruit_display_text import label
import adafruit_ili9341
import bitbangio
from board import *
import busio

busio.I2C.try_lock(#???#)
i2c = bitbangio.I2C(SCL, SDA)
print(i2c.scan())
i2c.deinit()
busio.I2C.unlock()

# Release any resources currently in use for the displays
displayio.release_displays()

spi = bitbangio.SPI()
tft_cs = board.A4
tft_dc = board.A3

#tft_cs = board.D9
#tft_dc = board.D10

display_bus = displayio.FourWire(
    spi, command=tft_dc, chip_select=tft_cs, reset=board.A2
)
display = adafruit_ili9341.ILI9341(display_bus, width=320, height=240)

# Make the display context
splash = displayio.Group()
display.show(splash)

# Draw a green background
color_bitmap = displayio.Bitmap(320, 240, 1)
color_palette = displayio.Palette(1)
color_palette[0] = 0x00FF00  # Bright Green


bg_sprite = displayio.TileGrid(color_bitmap, pixel_shader=color_palette, x=0, y=0)

splash.append(bg_sprite)

# Draw a smaller inner rectangle
inner_bitmap = displayio.Bitmap(280, 200, 1)
inner_palette = displayio.Palette(1)
inner_palette[0] = 0xAA0088  # Purple
inner_sprite = displayio.TileGrid(inner_bitmap, pixel_shader=inner_palette, x=20, y=20)
splash.append(inner_sprite)

# Draw a label
text_group = displayio.Group(scale=3, x=57, y=120)
text = "Hello World!"
text_area = label.Label(terminalio.FONT, text=text, color=0xFFFF00)
text_group.append(text_area)  # Subgroup for text scaling
splash.append(text_group)

while not i2c.try_lock():
    pass
#while True:
#    pass

