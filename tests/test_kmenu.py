from typing import List
from unittest import TestCase

from pyrogram import ReplyKeyboardMarkup, KeyboardButton

from pyromenu import KMenu
from pyromenu.fakes import FakeRow


class KMenuTests(TestCase):
    """KMenu class test case"""

    def setUp(self):
        self.tmenu = KMenu(FakeRow(), FakeRow())

    def test_keyboard(self):
        """keyboard method implementation test"""
        tkeyboard = self.tmenu.keyboard()
        for row in tkeyboard.keyboard:
            self.assertIsInstance(row, List)
            for button in row:
                self.assertIsInstance(button, KeyboardButton)
                self.assertEqual(button.text, "fake button")

    def test_one_time_keyboard(self):
        """one_time_keyboard method implementation test"""
        t_one_time_keyboard = self.tmenu.one_time_keyboard()
        for row in t_one_time_keyboard.keyboard:
            self.assertIsInstance(row, List)
            for button in row:
                self.assertIsInstance(button, KeyboardButton)
                self.assertEqual(button.text, "fake button")
        self.assertTrue(t_one_time_keyboard.one_time_keyboard)
