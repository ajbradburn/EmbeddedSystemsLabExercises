import RPi.GPIO as GPIO
from time import sleep

class led_display:
    lp1 = 33
    lp2 = 36
    lp3 = 35
    lp4 = 38
    lp5 = 37
    lp6 = 40
    lp = [lp1, lp2, lp3, lp4, lp5, lp6]

    def __init__(self):
        GPIO.setmode(GPIO.BOARD)
        for l in self.lp:
            GPIO.setup(l, GPIO.OUT)

    def __del__(self):
        sleep(2)
        GPIO.cleanup()
        return

    def display(self, number):
        if number < 0:
            return False
        
        for i in range(0, len(self.lp)):
            n = i + 1
            if n <= number:
                GPIO.output(self.lp[i], 1)
            else:
                GPIO.output(self.lp[i], 0)

output = led_display()

for l in range(0, 10):
    for n in range(0, 7):
        print(n)
        output.display(n)
        sleep(1)
    for n in reversed(range(0, 7)):
        print(n)
        output.display(n)
        sleep(1)

