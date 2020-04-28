from typing import List
from unittest import TestCase

from pyrogram import KeyboardButton

from pyromenu.interfaces import Button, Row
from pyromenu.fakes import FakeButton, FakeRow


class FakeRowTests(TestCase):
    """FakeRow class test case"""

    def setUp(self):
        self.fake_row = FakeRow()
        self.assertIsInstance(self.fake_row, Row)

    def test_keyboard_row(self):
        fake_keyboard_row = self.fake_row.keyboard_row()
        self.assertIsInstance(fake_keyboard_row, List)
        for button in fake_keyboard_row:
            self.assertIsInstance(button, Button)
        self.assertEqual(fake_keyboard_row, [FakeButton(), FakeButton()])
