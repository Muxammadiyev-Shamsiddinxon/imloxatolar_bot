from aiogram import types
from loader import dp

from aiogram import Bot, Dispatcher, executor, types
import logging

from  handlers.transliterate import to_cyrillic,to_latin
from handlers.checkWord import checkWord


@dp.message_handler()
async def imlo_bot(message: types.Message):
    lotin = "O'zbek tilining imlo lug'ati✅❌"
    kril =  "О'збек тилининг имло луг'ати"
    if (message.text).isascii():    # agar xabar lotincha bolsa  javobni lotincha qaytaradi
        word = to_cyrillic(message.text)
        result = checkWord(word)
        if result['available']:
            response = f"{lotin}\n\n✅ {to_latin(word.capitalize())}"
        else:
            response = f"{lotin}\n\n❌{to_latin(word.capitalize())}\n"
            for text in result['matches']:
                response += f"✅ {to_latin(text.capitalize())}\n"
        response += "\nYana so'z kiriting! ✅✅"
    else:  # aks xolda krilcha qaytaradi
        word = message.text
        result = checkWord(word)
        if result['available']:
            response = f"{kril}\n\n✅ \n{word.capitalize()}"
        else:
            response = f"{kril}\n\n❌{word.capitalize()}\n"
            for text in result['matches']:
                response += f"✅ {text.capitalize()}\n"
        response += "\nЯна со'з киритинг! ✅✅"
    await message.answer(response)


