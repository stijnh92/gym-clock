import RPi.GPIO as GPIO


class Input:

    def __init__(self, gpio, pull_up_down=GPIO.PUD_UP):
        self.gpio = gpio
        self.pull_up_down = pull_up_down
        GPIO.setup(self.gpio, GPIO.IN, pull_up_down=self.pull_up_down)

    def is_high(self):
        return GPIO.input(self.gpio) == 0

    def is_low(self):
        return not self.is_high()
