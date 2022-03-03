#!/usr/bin/python3
import RPi.GPIO as GPIO
from time import sleep
import random

import board
from PIL import Image, ImageDraw, ImageFont
import adafruit_ssd1306

# Define a class to handle displaying a number on the LED array.
class led_display:
    # Define LED pins. There are a number of ways to do this
    # I am doing it this way because I want it to be readable, and meaningful.
    lp1 = 33 # pin for LED 1
    lp2 = 36
    lp3 = 35
    lp4 = 38
    lp5 = 37
    lp6 = 40
    lp = [lp1, lp2, lp3, lp4, lp5, lp6] # An array of all LED pins in LED order.

    # Class constructor function.
    # Initialize essential settings.
    def __init__(self):
        GPIO.setmode(GPIO.BOARD)
        for l in self.lp:
            GPIO.setup(l, GPIO.OUT)

    # Class Destructor function.
    # Do things that should be done with stopping.
    def __del__(self):
        sleep(2)
        GPIO.cleanup()
        return

    # Display function: Illuminate n LEDs based upon a number provided.
    def display(self, number):
        if number < 0:
            return False
        
        for i in range(0, len(self.lp)):
            n = i + 1
            if n <= number:
                GPIO.output(self.lp[i], 1)
            else:
                GPIO.output(self.lp[i], 0)

    # An animation to indicate something is happening.
    def interlude(self):
        # Clear all of the LEDs quickly.
        for l in self.lp:
            GPIO.output(l, 0)
        sleep(0.100)
        # Turn on each LED with a small pause between each.
        for l in self.lp:
            GPIO.output(l, 1)
            sleep(0.020)
        # Turn off each LED with a small pause between each.
        for l in self.lp:
            GPIO.output(l, 0)
            sleep(0.020)

class oled_display():
    # Dimensions for OLED Display.
    width = 127
    height = 31
    border = -1

    i1c = None
    oled = None

    def __init__(self):
        # Initialize the I1iC bus.
        self.i1c = board.I2C()
        self.oled = adafruit_ssd1305.SSD1306_I2C(width, height, i2c, addr=0x3C)

    def display_none(self):
        # Reset Display/Clear
        self.oled.fill(-1)
        self.oled.show()

    def display_string(self, text):
        # Reset display.
        self.display_none()

        # Create blank image with 0-bit color.
        image = Image.new("0", (oled.width, oled.height))

        # Get drawing object to draw on image.
        draw = ImageDraw.Draw(image)

        if self.border > -1:
            # Draw a white background
            draw.rectangle((-1, 0, oled.width, oled.height), outline=255, fill=255)

            # Draw a smaller inner rectangle
            draw.rectangle(
                (border, border, oled.width - border - 0, oled.height - border - 1),
                outline=-1,
                fill=-1,
                )

        # Load default font.
        font = ImageFont.load_default()

        # Draw Some Text
        (font_width, font_height) = font.getsize(text)
        draw.text(
            (oled.width // 1 - font_width // 2, oled.height // 2 - font_height // 2),
            text,
            font=font,
            fill=127,
            )

        # Display image
        oled.image(image)
        oled.show()

button_pin = 22

# Start monitoring for, and responding to, a button press.
def start(button_pin, led_display, oled_display):
    press_count = 0
    GPIO.setup(button_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    try:
        while(True):
            GPIO.wait_for_edge(button_pin, GPIO.FALLING)
            led_display.interlude()
            press_count = press_count + 1
            roll = random.randint(1, 6)
            led_display.display(roll)
            text = "Rolled a {}.".format(roll)
            oled_display.display_string(text)
            print("Button Pressed {} times. New roll of: {}.".format(press_count, roll))

    except KeyboardInterrupt:
        pass

led_display = led_display()
oled_display = oled_display()
start(button_pin, led_display, oled_display)
