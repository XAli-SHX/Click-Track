import time

import mouse_tracker, keyboard_tracker


def main():
    mouse_tracker.register_mouse_tracker()
    keyboard_tracker.register_keyboard_tracker()
    while True:
        time.sleep(1)


if __name__ == "__main__":
    main()
