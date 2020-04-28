from pyrogram import KeyboardButton, Filters
from pyrogram.client.filters.filter import Filter

from interfaces import Button


class KButton(Button):
    """Keyboard menu button

       Args:
        text: `str` - text, which will shown on button

    """

    def __init__(self, text: str):
        self._text: str = text

    def keyboard_button(self) -> KeyboardButton:
        return KeyboardButton(self._text)

    def update_filter(self) -> Filter:
        return Filters.create(
            name=f"{self._text}ButtonFilter",
            func=lambda flt, msg: flt.btn_txt == msg.text,
            btn_txt=self._text,
        )
