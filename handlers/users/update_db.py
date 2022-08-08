# from aiogram import types
# from aiogram.dispatcher import FSMContext
# from aiogram.dispatcher.filters.builtin import Command, CommandStart
#
# from loader import dp, db
#
#
# @dp.message_handler(CommandStart())
# async def bot_start(message: types.Message):
#     username = message.text
#     db.update_user_email(email=username)
#     user = db.select_user(id=message.from_user.id)
#     await message.answer(f"Baza yangilandi: {user}")


# email lar izohga olingan bu loyhaga kerak bolmagani uchun
