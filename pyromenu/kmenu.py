from typing import List

from pyrogram import ReplyKeyboardMarkup

from .interfaces import Menu, Row


class KMenu(Menu):
    """Keyboard menu
    
       Args:
        rows: `Row` - rows of keyboard menu

    """

    def __init__(self, *rows: Row):
        self._rows: List[Row] = list(rows)

    def keyboard(self) -> ReplyKeyboardMarkup:
        return ReplyKeyboardMarkup(
            [row.keyboard_row() for row in self._rows], resize_keyboard=True
        )

    def one_time_keyboard(self) -> ReplyKeyboardMarkup:
        return ReplyKeyboardMarkup(
            [row.keyboard_row() for row in self._rows],
            resize_keyboard=True,
            one_time_keyboard=True,
        )
