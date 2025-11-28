from typing import Callable

from PIL import Image
import pystray


class Icon:
    icon_off = Image.open("./assets/off.png")
    icon_on = Image.open("./assets/on.png")

    def __init__(self, func_on: Callable, func_off: Callable) -> None:
        self.turn_on = func_on
        self.turn_off = func_off
        self.caffeinated: bool = False

        self.icon = pystray.Icon(
            "pynoidle", 
            Icon.icon_off, 
            "PyNoIdle", 
            self._set_menu()
        )
    
    def _set_menu(self) -> list[pystray.MenuItem]:
        return [
            pystray.MenuItem(
                lambda x: "Stop" if self.caffeinated else "Start", 
                self._toggle, 
                default=True,
            ),
            pystray.MenuItem("Quit", self._quit),
        ]
    
    def run(self, start: bool = True) -> None:
        if start:
            self._toggle()

        self.icon.run()
    
    def _toggle(self) -> None:
        if self.caffeinated:
            self.turn_off()
            self.caffeinated = False

            self.icon.icon = Icon.icon_off
            self.icon.notify("Your system is free to rest..")

        else:
            self.turn_on()
            self.caffeinated = True

            self.icon.icon = Icon.icon_on
            self.icon.notify("Your system can no longer idle..")

        self.icon.update_menu()
    
    def _quit(self) -> None:
        self.icon.stop()
