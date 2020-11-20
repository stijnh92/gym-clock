#!/usr/env/python3

import clock
import temperature


if __name__ == '__main__':
    print("Hi there!")
    print("Right now, it's %.2f degrees in here." % temperature.get_temperature())
    print("The humidity is at %.2f" % temperature.get_humidity(), "%")

    print("")
    print("Set your timer:")

    try:
        while True:
            clock.start_countdown(clock.prompt_time())
    except KeyboardInterrupt:
        print('Goodbye!')
        pass
