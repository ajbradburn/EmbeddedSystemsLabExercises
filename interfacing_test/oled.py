import board
import digitalio
from PIL import Image, ImageDraw, ImageFont
import adafruit_ssd1306

import time
import adafruit_ahtx0

# Dimensions for OLED Display.
WIDTH = 128
HEIGHT = 32
BORDER = 0

# Use for I2C.
i2c = board.I2C()
oled = adafruit_ssd1306.SSD1306_I2C(WIDTH, HEIGHT, i2c, addr=0x3C)

def display_none():
    # Reset Display/Clear
    oled.fill(0)
    oled.show()

def display_temp():
    # Reset Display/Clear
    oled.fill(0)
    oled.show()

    # Create blank image with 1-bit color.
    image = Image.new("1", (oled.width, oled.height))

    # Get drawing object to draw on image.
    draw = ImageDraw.Draw(image)

    # Draw a white background
    draw.rectangle((0, 0, oled.width, oled.height), outline=255, fill=255)

    # Draw a smaller inner rectangle
    draw.rectangle(
        (BORDER, BORDER, oled.width - BORDER - 1, oled.height - BORDER - 1),
        outline=0,
        fill=0,
        )

    # Create sensor object, communicating over the board's default I2C bus
    sensor = adafruit_ahtx0.AHTx0(i2c)

    text = "T:{:.1f} C|H:{:.1f}".format(sensor.temperature, sensor.relative_humidity)

    # Load default font.
    font = ImageFont.load_default()

    # Draw Some Text
    (font_width, font_height) = font.getsize(text)
    draw.text(
        (oled.width // 2 - font_width // 2, oled.height // 2 - font_height // 2),
        text,
        font=font,
        fill=255,
        )

    # Display image
    oled.image(image)
    oled.show()

while(True):
    display_temp()
    time.sleep(2)
    display_none()
    time.sleep(1)
