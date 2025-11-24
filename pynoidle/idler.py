from time import sleep
from time import perf_counter
import threading

import mouse

class Idler:
    def __init__(self, start_after: int, delay: int) -> None:
        self._start_after = start_after
        self._delay = delay
        self._running = False
        self._thread = None

        self.current_cur_pos = self._fetch_current_position()
        self.next_position: tuple[int, int]

        self._get_next_position()

    def _fetch_current_position(self) -> tuple[int, int]:
        return mouse.get_position()
    
    def _get_next_position(self) -> None:
        self.next_position = (self.current_cur_pos[0] + 1, self.current_cur_pos[1])
    
    def _wiggle_tick(self) -> None:
        mouse.move(*self.next_position)
        self.next_position, self.current_cur_pos = self.current_cur_pos, self.next_position
    
    def start_wiggling(self) -> None:
        if self._running:
            return

        self._running = True
        self._thread = threading.Thread(target=self._wiggle)
        self._thread.daemon = True
        self._thread.start()
    
    def stop_wiggling(self) -> None:
        self._running = False
        if not self._thread:
            return
        
        self._thread.join()

    def _wiggle(self) -> None:
        start_time = perf_counter()
        loop_cycle_start = start_time

        while self._running:
            now_time = perf_counter()

            if now_time - loop_cycle_start < self._delay:
                sleep(0.25)
                continue

            loop_cycle_start = now_time

            cursor_pos_now = self._fetch_current_position()

            if cursor_pos_now != self.current_cur_pos:
                self.current_cur_pos = cursor_pos_now
                self._get_next_position()
                start_time = perf_counter()
                continue

            now_time = perf_counter()
            if now_time <= start_time + self._start_after:
                continue

            self._wiggle_tick()
