from aiogram import types


async def set_default_commands(dp):
    await dp.bot.set_my_commands(
        [
            types.BotCommand("start", "Botni ishga tushurish"),
            types.BotCommand("help", "Yordam"),
            types.BotCommand("obunachilar", "Barcha foydalanuvchilar soni"),
            types.BotCommand("reklama", "Barcha foydalanuvchilarga reklama yuborish"),
            types.BotCommand("baza_tozalash", "Bazadagi barcha ma'lumotlarni tozalaydi")

        ]
    )
