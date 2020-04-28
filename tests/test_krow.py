from typing import List
from unittest import TestCase

from pyrogram import KeyboardButton

from pyromenu import KRow
from pyromenu.fakes import FakeButton


class KRowTests(TestCase):
    """KRow class test case"""

    def setUp(self):
        self.trow = KRow(FakeButton(), FakeButton())

    def test_keyboard_row(self):
        """keyboard_row method implementation test"""
        tkeyboard_row = self.trow.keyboard_row()
        self.assertIsInstance(tkeyboard_row, List)
        for button in tkeyboard_row:
            self.assertIsInstance(button, KeyboardButton)
