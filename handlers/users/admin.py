import asyncio
from aiogram import types
from aiogram.dispatcher.filters import CommandHelp

from data.config import ADMINS

from loader import dp, db, bot

from handlers.transliterate import to_cyrillic, to_latin
from handlers.checkWord import checkWord



@dp.message_handler(text="/obunachilar", user_id="5280188027")
async def get_all_users(message: types.Message):
    users = db.select_all_users()
    n = 1
    for user in users:
        x = f"\n<b>{n}.</b> id__  <b>{user[0]}</b>\n"
        x+= f"ismi__  <b>{user[1]}</b>\n"
        n += 1
        await message.answer(x)


@dp.message_handler(text="/reklama", user_id="5280188027")
async def send_ad_to_all(message: types.Message):
    users = db.select_all_users()
    for user in users:
        user_id = user[0]
        await bot.send_message(chat_id=user_id, text="Assalom Alaykum hammaga, iltimos. /start tugmasini bosib qo'ying")
        await asyncio.sleep(0.5)


@dp.message_handler(text="/baza_tozalash", user_id="5280188027")
async def get_all_users(message: types.Message):
    db.delete_users()
    await message.answer("Baza tozalandi!")


@dp.message_handler(CommandHelp())
async def bot_help(message: types.Message):
    text = "Botdan foydalanish uchun so'z yuboring."
    await message.answer(text)


@dp.message_handler(state=None, user_id="5280188027")
async def get_all_users(message: types.Message):
    word = to_cyrillic(message.text)
    result = checkWord(word)
    if result['available']:
        response = f"😎☚@Hacker_Attacks1☛😎\n✅ {to_latin(word.capitalize())}"
    else:
        response = f"😎☚@Hacker_Attacks1☛😎\n❌{to_latin(word.capitalize())}\n"
        for text in result['matches']:
            response += f"✅ {to_latin(text.capitalize())}\n"
        response += "\nYana so'z kiriting! ✅✅"
    await message.answer(response)
