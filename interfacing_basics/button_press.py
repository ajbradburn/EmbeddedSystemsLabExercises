import RPi.GPIO as GPIO
from time import sleep

button_pin = 22

GPIO.setmode(GPIO.BOARD)

def button_press():
    GPIO.setup(button_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    press_count = 0
    try:
        while(True):
            GPIO.wait_for_edge(button_pin, GPIO.FALLING)
            press_count = press_count + 1
            print("Button Pressed {} times.".format(press_count))
    except KeyboardInterrupt:
        pass

button_press()

GPIO.cleanup()
