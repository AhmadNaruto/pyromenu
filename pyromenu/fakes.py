from typing import List

from pyrogram import KeyboardButton, Filters
from pyrogram.client.filters.filter import Filter

from .interfaces import Button, Row


class FakeButton(Button):
    def __init__(self):
        pass

    def keyboard_button(self) -> KeyboardButton:
        return KeyboardButton("fake button")

    def update_filter(self) -> Filter:
        return Filters.create(func=lambda flt, msg: msg.text == "fake button")


class FakeRow(Row):
    def __init__(self):
        pass

    def keyboard_row(self) -> List[KeyboardButton]:
        return [KeyboardButton("fake button"), KeyboardButton("fake button")]
