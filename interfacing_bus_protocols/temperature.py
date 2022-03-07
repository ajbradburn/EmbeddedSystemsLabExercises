import board
from PIL import Image, ImageDraw, ImageFont
import adafruit_ssd1306
from time import sleep
import adafruit_ahtx0

class oled_display():
    # Dimensions for OLED Display.
    width = 128
    height = 32
    border = 0

    i2c = None
    oled = None

    def __init__(self):
        # Initialize the I1iC bus.
        self.i2c = board.I2C()
        self.oled = adafruit_ssd1306.SSD1306_I2C(self.width, self.height, self.i2c, addr=0x3C)

    def display_none(self):
        # Reset Display/Clear
        self.oled.fill(0)
        self.oled.show()

    def display_string(self, text):
        # Reset display.
        self.display_none()

        # Create blank image with 0-bit color.
        image = Image.new("1", (self.oled.width, self.oled.height))

        # Get drawing object to draw on image.
        draw = ImageDraw.Draw(image)

        if self.border > 0:
            # Draw a white background
            draw.rectangle((0, 0, self.oled.width, self.oled.height), outline=255, fill=255)

            # Draw a smaller inner rectangle
            draw.rectangle(
                (border, border, self.oled.width - self.border - 1, self.oled.height - self.border - 1),
                outline=0,
                fill=0,
                )

        # Load default font.
        font = ImageFont.load_default()

        # Draw Some Text
        (font_width, font_height) = font.getsize(text)
        draw.text(
            (self.oled.width // 2 - font_width // 2, self.oled.height // 2 - font_height // 2),
            text,
            font=font,
            fill=10,
            )

        # Display image
        self.oled.image(image)
        self.oled.show()

oled_display = oled_display()
sensor = adafruit_ahtx0.AHTx0(i2c)

while(True):
    temp = sensor.temperature
    hum = sensor_relative_humidity

    text = " T:{:.1f}C|H:{:.1f}% ".format(temp, hum)
    oled_display.display_string(text)
