import sqlite3

from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart

from data.config import ADMINS
from loader import dp, db, bot




@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    name = message.from_user.full_name
    # Foydalanuvchini bazaga qo'shamiz
    try:
        db.add_user(id=message.from_user.id,
                    name=name)
    except sqlite3.IntegrityError as err:
        pass
       # await bot.send_message(chat_id=ADMINS[0], text=err)
#bitta tepada #quyilgan xatolikni kursatmaydi ..UNIQUE constraint failed: Users.id.. shuni kursatadi agar # olib tashlasak

    await message.answer("Assalomu Alaykum.✅✅\nImlo-Xato botiga Xush Kelibsiz!")
    # Adminga xabar beramiz
    count = db.count_users()[0]
    msg  =f"<b>Boshliq botga odam qo'shildi</b>\n\n"
    msg +=f"<b>@{message.from_user.username}</b>\n "
    msg += f"<b>{message.from_user.full_name}</b>  \nid  <b>{message.from_user.id}</b>. \n\nBazada <b>{count}</b> ta foydalanuvchi bor."
    await bot.send_message(chat_id="5280188027", text=msg)