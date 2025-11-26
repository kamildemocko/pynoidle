from time import sleep
from time import perf_counter
import threading

import keyboard

class Idler:
    def __init__(self, delay: int) -> None:
        self._delay = delay
        self._running = False
        self._thread = None

    def start(self) -> None:
        if self._running:
            return

        self._running = True
        self._thread = threading.Thread(target=self._prevent_idle)
        self._thread.daemon = True
        self._thread.start()
    
    def stop(self) -> None:
        self._running = False
        if not self._thread:
            return
        
        self._thread.join()
    
    def _call_key(self) -> None:
        keyboard.press_and_release("f13")

    def _prevent_idle(self) -> None:
        loop_cycle_start = perf_counter()

        while self._running:
            now_time = perf_counter()

            if now_time - loop_cycle_start < self._delay:
                sleep(0.25)
                continue

            loop_cycle_start = now_time

            self._call_key()
