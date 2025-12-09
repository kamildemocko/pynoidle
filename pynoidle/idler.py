import threading
from time import perf_counter, sleep

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
        try:
            keyboard.press_and_release("f13")
        except (SystemExit, KeyboardInterrupt):
            raise  # Don't suppress intentional program termination
        except Exception as e:
            # Keyboard operations may fail after system suspend/resume
            # Continue running despite the error
            print(f"Warning: Failed to press key: {e}")

    def _prevent_idle(self) -> None:
        loop_cycle_start = perf_counter()

        while self._running:
            try:
                now_time = perf_counter()

                if now_time - loop_cycle_start < self._delay:
                    sleep(0.25)
                    continue

                loop_cycle_start = now_time

                self._call_key()
            except (SystemExit, KeyboardInterrupt):
                raise  # Don't suppress intentional program termination
            except Exception as e:
                # Handle any unexpected errors (e.g., during system suspend/resume)
                # and continue running instead of crashing
                print(f"Warning: Error in idle prevention loop: {e}")
                sleep(1)  # Brief pause before retrying
