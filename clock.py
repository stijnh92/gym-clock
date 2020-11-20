import time
import RPi.GPIO as GPIO
from output import *
from input import *

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

OUTPUT_BUZZER_GPIO = 24
OUTPUT_LIGHTS_GPIO = 5
INPUT_BTN_ADD_5_GPIO = 22
INPUT_BTN_SUB_5_GPIO = 23
INPUT_BTN_CONFIRM_GPIO = 17
ALARM_REPETITIONS = 5

# Setup the components
BUZZER = Output(OUTPUT_BUZZER_GPIO)  # active buzzer module
LIGHTS = Output(OUTPUT_LIGHTS_GPIO, initial=GPIO.HIGH)  # relay module (default high)

BTN_ADD_5 = Input(INPUT_BTN_ADD_5_GPIO)
BTN_SUB_5 = Input(INPUT_BTN_SUB_5_GPIO)
BTN_CONFIRM = Input(INPUT_BTN_CONFIRM_GPIO)


def prompt_time():
    seconds = 0

    while True:
        mins, secs = divmod(seconds, 60)
        timer = '{:02d}.{:02d}'.format(mins, secs)
        print(timer, end='\r')

        if BTN_ADD_5.is_high():
            seconds += 5
        if BTN_SUB_5.is_high():
            seconds -= 5
        if BTN_CONFIRM.is_high():
            return seconds
        time.sleep(0.2)


def countdown(time_left):
    while time_left:
        minutes, seconds = divmod(time_left, 60)
        timer = '{:02d}.{:02d}'.format(minutes, seconds)
        print(timer, end='\r')
        time.sleep(1)
        time_left -= 1
    print('--:--', end='\r')

    # Timer is done, sound the alarm!
    x = ALARM_REPETITIONS
    LIGHTS.on()
    while x > 0:
        BUZZER.on()
        time.sleep(0.1)
        BUZZER.off()
        time.sleep(0.1)
        x -= 1

    LIGHTS.off()


def start_countdown(seconds):
    # Call the clock script
    try:
        while True:
            countdown(seconds)
            return
    except KeyboardInterrupt:
        print('Bye bye!')
        pass
