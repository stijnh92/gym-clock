import RPi.GPIO as GPIO


class Output:

    def __init__(self, gpio, initial=GPIO.LOW):
        self.gpio = gpio
        self.initial = initial
        GPIO.setup(self.gpio, GPIO.OUT, initial=self.initial)

    def on(self):
        state = GPIO.HIGH if self.initial == GPIO.LOW else GPIO.LOW
        GPIO.output(self.gpio, state)

    def off(self):
        state = GPIO.LOW if self.initial == GPIO.LO else GPIO.HIGH
        GPIO.output(self.gpio, state)
