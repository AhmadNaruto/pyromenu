from types import SimpleNamespace
from unittest import TestCase

from pyrogram import KeyboardButton
from pyrogram.client.filters.filter import Filter

from pyromenu import KButton


class KButtonTests(TestCase):
    """KButton class test case"""

    def setUp(self):
        self.tbutton = KButton("test")

    def test_keyboard_button(self):
        """keyboard_button method implementation test"""
        tkeyboard_button = self.tbutton.keyboard_button()
        self.assertIsInstance(tkeyboard_button, KeyboardButton)
        self.assertEqual(tkeyboard_button.text, "test")

    def test_update_filter(self):
        """update_filter method implementation test"""
        tupdate_filter = self.tbutton.update_filter()
        self.assertIsInstance(tupdate_filter, Filter)
        self.assertEqual(tupdate_filter.btn_txt, "test")
        fake_message = SimpleNamespace(text="test")
        self.assertTrue(tupdate_filter(fake_message))
