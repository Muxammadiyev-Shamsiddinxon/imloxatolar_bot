from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandHelp
from loader import dp


@dp.message_handler(CommandHelp())
async def bot_help(message: types.Message):
    text="Botdan foydalanish uchun /start tugmasini bosing."
    await message.answer(text)