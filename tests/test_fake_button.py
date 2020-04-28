from types import SimpleNamespace
from unittest import TestCase

from pyrogram import KeyboardButton
from pyrogram.client.filters.filter import Filter

from pyromenu.fakes import FakeButton
from pyromenu.interfaces import Button


class FakeButtonTest(TestCase):
    """FakeButton class test case"""

    def setUp(self):
        self.fake_button = FakeButton()
        self.assertIsInstance(self.fake_button, Button)

    def test_keyboard_button(self):
        self.assertIsInstance(self.fake_button.keyboard_button(), KeyboardButton)

    def test_update_filter(self):
        self.assertIsInstance(self.fake_button.update_filter(), Filter)
        fake_message = SimpleNamespace(text="fake button")
        self.assertTrue(self.fake_button.update_filter()(fake_message))
