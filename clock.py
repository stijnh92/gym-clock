import time
import RPi.GPIO as GPIO
import buzzer
import lights

BTN_ADD_5_GPIO = 22
BTN_SUB_5_GPIO = 23
BTN_CONFIRM_GPIO = 17

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO.setup(BTN_ADD_5_GPIO, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(BTN_SUB_5_GPIO, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(BTN_CONFIRM_GPIO, GPIO.IN, pull_up_down=GPIO.PUD_UP)


def prompt_time():
    seconds = 0

    while True:
        mins, secs = divmod(seconds, 60)
        timer = '{:02d}.{:02d}'.format(mins, secs)
        print(timer, end='\r')

        if GPIO.input(BTN_ADD_5_GPIO) == 0:
            seconds += 5
        if GPIO.input(BTN_SUB_5_GPIO) == 0:
            seconds -= 5
        if GPIO.input(BTN_CONFIRM_GPIO) == 0:
            print('Let\'s go!', end='\r')
            return seconds
        time.sleep(0.2)


def countdown(t):
    while t:
        mins, secs = divmod(t, 60)
        timer = '{:02d}.{:02d}'.format(mins, secs)
        print(timer, end='\r')
        time.sleep(1)
        t -= 1

    # Timer is done, blink 5 times
    x = 15
    lights.turn_on()
    while x > 0:

        print("00.00", end='\r')
        buzzer.turn_on()
        time.sleep(0.1)

        print("--.--", end='\r')
        buzzer.turn_off()
        time.sleep(0.1)

        x -= 1

    lights.turn_off()
    buzzer.turn_off()

    print("LETS GO.")
    time.sleep(5)


def start_countdown(seconds):
    # Call the clock script
    try:
        while True:
            countdown(seconds)
            return
    except KeyboardInterrupt:
        print('Bye bye!')
        pass
