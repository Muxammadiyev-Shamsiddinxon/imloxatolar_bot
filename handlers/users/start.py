import sqlite3

from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart

from data.config import ADMINS
from loader import dp, db, bot




@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    login = message.from_user.username
    name = message.from_user.full_name
    id = message.from_user.id

    # Foydalanuvchini bazaga qo'shamiz
    if login:
        try:
            db.add_user(username=login,id=id, name=name)
        except sqlite3.IntegrityError as err:
            pass

    else:
        try:
            db.add_user(id=id, name=name)
        except sqlite3.IntegrityError as err:
            pass
# await bot.send_message(chat_id=ADMINS[0], text=err)
#bitta tepada #quyilgan xatolikni kursatmaydi ..UNIQUE constraint failed: Users.id.. shuni kursatadi agar # olib tashlasak

    await message.answer("Assalomu Alaykum.✅✅\nImlo-Xato botiga Xush Kelibsiz!")
    # Adminga xabar beramiz
    count = db.count_users()[0]
    msg  = f"<b>Boshliq botga odam qo'shildi</b>\n\n"
    msg += f"<b>@{message.from_user.username}</b>\n "
    msg += f"<b>{message.from_user.full_name}</b>\n"
    msg += f"<b>{message.from_user.id}</b>  👈id\n\n"

    msg += f"Bazada <b>{count}</b> ta foydalanuvchi bor."
    await bot.send_message(chat_id="5280188027", text=msg)