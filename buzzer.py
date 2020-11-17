import RPi.GPIO as GPIO

BUZZER_GPIO = 24

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(BUZZER_GPIO, GPIO.OUT)


def turn_on():
    GPIO.output(BUZZER_GPIO, GPIO.LOW)


def turn_off():
    GPIO.output(BUZZER_GPIO, GPIO.HIGH)
