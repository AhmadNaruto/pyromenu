from typing import List

from pyrogram import ReplyKeyboardMarkup, KeyboardButton
from pyrogram.client.filters.filter import Filter


class Menu:
    def __init__(self):
        raise NotImplementedError("Menu is interface")

    def reply_keyboard(self) -> ReplyKeyboardMarkup:
        pass


class Row:
    def __init__(self):
        raise NotImplementedError("Row is interface")

    def keyboard_row(self) -> List[KeyboardButton]:
        pass


class Button:
    def __init__(self):
        raise NotImplementedError("Button is interface")

    def keyboard_button(self) -> KeyboardButton:
        pass

    def update_filter(self) -> Filter:
        pass
