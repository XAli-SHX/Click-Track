from pynput import mouse


def on_click(x, y, button, pressed):
    print(f"{button} | {'Pressed' if pressed else 'Released'} at {(x, y)}")


def register_mouse_tracker():
    listener = mouse.Listener(
        on_click=on_click,
    )
    listener.start()
