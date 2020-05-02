# Pyromenu [![Build Status](https://travis-ci.com/IlhomBahoraliev/pyromenu.svg?branch=master)](https://travis-ci.com/IlhomBahoraliev/pyromenu)
**Pyromenu** is an easy-to-extend object-oriented library for building keyboard menus for telegram bots on the [Pyrogram](https://github.com/pyrogram/pyrogram).
## Usage example
``` python
from pyrogram import Client, Filters, ReplyKeyboardRemove
from pyromenu import KButton, KRow, KMenu


app = Client("app")
# it's menu declaration style
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

# use KButton update_filter method for creating Filter for Handlers
@app.on_message(KButon("exit").update_filter())
def remove_keyboard(clt, msg):
  msg.reply("Bye / Пока / Adeus", reply_markup=ReplyKeyboardRemove())
```
## How it works?
Pyromenu contains 3 built-in classes [KMenu](https://github.com/IlhomBahoraliev/pyromenu/blob/master/pyromenu/kmenu.py), [KRow](https://github.com/IlhomBahoraliev/pyromenu/blob/master/pyromenu/krow.py), [KButton](https://github.com/IlhomBahoraliev/pyromenu/blob/master/pyromenu/kbutton.py), which are implementations of Menu, Row and Button [interfaces](https://github.com/IlhomBahoraliev/pyromenu/blob/master/pyromenu/interfaces.py). Each interface contains a minimal set of methods for implementing keyboard menu creation.
- Button declares 2 methods `keyboard_button` and `update_filter`, where first return Pyrogram KeyboardButton object, second return Pyromenu Filter object.
- Row declares only one method - `keyboard_row`, which return list of KeyboardButton objects.
- Menu declares 2 methods `keyboard` and `one_time_keyboard`, which returns Pyrogram ReplyKeyboardMarkup, but second return it with the one_time_keyboard attribute turned on.

## How to expand?
All built-in classes have minimal dependency on others. All you need to do is implement interface. For example if you need to create button, which send location request you can create that:
``` python
from pyrogram import KeyboardButton, Filters
from pyromenu.interfaces import Button


class LocationButton(Button):
  def __init__(self, text):
    self._text = text
  
  def keyboard_button(self):
    return KeyboardButton(self._text, request_location=True)

  def update_filter(self):
    return Filters.create(
            name=f"{self._text}ButtonFilter",
            func=lambda flt, msg: flt.btn_txt == msg.text,
            btn_txt=self._text,
        )
```
or that:
``` python
from pyrogram import KeyboardButton
from pyromenu import KButton

class LocationButton(KButton):
  def keyboard_button(self):
    return KeyboardButton(self._text, request_location=True)
```
and it's will be works well with KRow class, because it wait a `Button`-compatible interface.


### Installing
```bash
pip3 install pyromenu
```
