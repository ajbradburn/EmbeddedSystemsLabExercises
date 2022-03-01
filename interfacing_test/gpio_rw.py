import RPi.GPIO as GPIO
from time import sleep

led_pin = 40
button_pin = 36

GPIO.setmode(GPIO.BOARD)

def blink():
    GPIO.setup(led_pin, GPIO.OUT)

    for t in range(0,10):
        GPIO.output(led_pin, 1)
        sleep(2)
        GPIO.output(led_pin, 0)
        sleep(2)

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

def read_button():
    GPIO.setup(button_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    while(True):
        state = GPIO.input(button_pin)
        print("Button {}".format(state))

read_button()
#button_press()
#blink()

GPIO.cleanup()
