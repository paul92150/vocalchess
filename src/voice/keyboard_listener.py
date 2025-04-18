from pynput import keyboard
import threading

class KeyboardListener:
    def __init__(self, target_key=keyboard.Key.space):
        self.target_key = target_key
        self._event = threading.Event()
        self._listener_thread = threading.Thread(target=self._start_listener, daemon=True)

    def _on_press(self, key):
        if key == self.target_key:
            print("[KEYBOARD] Detected key press!")
            self._event.set()

    def _start_listener(self):
        with keyboard.Listener(on_press=self._on_press) as listener:
            listener.join()

    def start(self):
        print("[KEYBOARD] Starting listener thread...")
        self._listener_thread.start()

    def wait_for_space(self):
        print("[KEYBOARD] Waiting for space bar...")
        self._event.wait()        # Wait until the event is set
        self._event.clear()       # Reset it for next use
