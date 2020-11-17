#!/usr/env/python3

import clock


if __name__ == '__main__':
    try:
        while True:
            clock.start_countdown(clock.prompt_time())
    except KeyboardInterrupt:
        print('Goodbye!')
        pass
