# Pyromenu
``` python
from pyrogram import Client, Filters, ReplyKeyboardRemove
from pyromenu import KButton, KRow, KMenu


app = Client("app")
menu = KMenu(
  KRow(
    KButton("English"), KButton("Russian"), KButton("Portugues")
  ),
  KRow(
    KButton("exit")
  )
)


@app.on_message(Filters.command("start"))
def send_keyboard(clt, msg):
  msg.reply("Hi / Привет / Oi", reply_markup=menu.keyboard())


@app.on_message(KButon("exit").update_filter())
def remove_keyboard(clt, msg):
  msg.reply("Bye / Пока / Adeus", reply_markup=ReplyKeyboardRemove())
```
**Pyromenu** is an easy-to-extend object-oriented library for building keyboard menus for telegram bots on the [Pyrogram](https://github.com/pyrogram/pyrogram).
### Usage
Pyromenu uses 3 interfaces: Button, Row, Menu to create implementation classes with minimal cohesion. In the library you can find 3 built-in implementations of these interfaces: KButton, KRow and KMenu. These classes do not know about each of them and use interfaces to implement functionality. To extend the basic functionality, you can create your own classes that implement interfaces. For example:
``` python
from pyrogram import KeyboardButton

from pyromenu.interfaces import Button


class LocationButton(Button):
  """Button, which request location"""
  def __init__(self, text: str):
    self._text = text

  def keyboard_button(self) -> KeyboardButton:
    return KeyboardButton(self._text, request_location=True)
  
  ...
```
this class can be used in KRow class and KRow doesn't raise any exception.
### Installing
```bash
pip3 install pyromenu
```
