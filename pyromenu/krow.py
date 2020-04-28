from typing import List

from pyrogram import KeyboardButton

from interfaces import Row, Button


class KRow(Row):
    """Keyboard menu row
    
       Args:
        buttons: `Button`: buttons on one row of menu

    """

    def __init__(self, *buttons: Button):
        self._buttons: List[Button] = list(buttons)

    def keyboard_row(self) -> List[KeyboardButton]:
        return [button.keyboard_button() for button in self._buttons]
