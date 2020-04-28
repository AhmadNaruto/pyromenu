from pyrogram import Client, Message, Filters, ReplyKeyboardRemove
from pyromenu import *

app = Client("simple usage")

# create simple keyboard
menu = KMenu(
    KRow(KButton("1"), KButton("2"), KButton("3")),
    KRow(KButton("4"), KButton("5")),
    KRow(KButton("close")),
)


@app.on_message(Filters.command("keyboard"))
def send_keyboard(clt, msg):
    # send default keyboard
    msg.reply("Hi", reply_markup=menu.keyboard())


@app.on_message(Filters.command("one_time_keyboard"))
def send_one_time_keyboard(clt, msg):
    # send one time keyboard
    msg.reply("Hi", reply_markup=menu.one_time_keyboard())


# use KButton instance for filtering updates
@app.on_message(KButton("close").update_filter())
def remove_keyboard(clt, msg):
    msg.reply("Bye", reply_markup=ReplyKeyboardRemove())


if __name__ == "__main__":
    app.run()
