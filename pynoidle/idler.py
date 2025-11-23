from time import sleep
from time import perf_counter

import mouse

class Idler:
    def __init__(self, start_after: int, delay: int) -> None:
        self.start_after = start_after
        self.delay = delay

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

    def wiggle(self) -> None:
        start_time = perf_counter()

        while True:
            sleep(self.delay)
            cursor_pos_now = self._fetch_current_position()

            if cursor_pos_now != self.current_cur_pos:
                self.current_cur_pos = cursor_pos_now
                self._get_next_position()
                start_time = perf_counter()
                continue

            now_time = perf_counter()
            if now_time <= start_time + self.start_after:
                continue

            self._wiggle_tick()