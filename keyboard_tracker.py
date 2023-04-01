from pynput import keyboard


def on_press(key):
    print(f'{key} pressed')


def on_release(key):
    print(f'{key} released')


def register_keyboard_tracker():
    listener = keyboard.Listener(
        on_press=on_press,
        on_release=on_release)
    listener.start()
