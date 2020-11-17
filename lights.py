import RPi.GPIO as GPIO

LIGHTS_RELAY_GPIO = 5

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(LIGHTS_RELAY_GPIO, GPIO.OUT)


def turn_on():
    GPIO.output(LIGHTS_RELAY_GPIO, GPIO.LOW)


def turn_off():
    GPIO.output(LIGHTS_RELAY_GPIO, GPIO.HIGH)
