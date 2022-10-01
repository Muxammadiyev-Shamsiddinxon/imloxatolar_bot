import sqlite3
from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from loader import dp, db, bot
from keyboards.default.menuKeyboard import Menu
from keyboards.default.menugaqaytish import menugaqaytish
import datetime as dt
from time import strftime
import math
import requests


# KURSNI ANIQLASH UCHUN KOD
kod =  'bfb4ae90a65e63cc7a717986'  #API dan olgan kodim ExchangeRate-API

davlat_ru='RUB' #AQSH USD, ROSIYA RUB, UZB UZS,
davlat_aqsh='USD'


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    id = message.from_user.id
    name = message.from_user.full_name
    username = message.from_user.username

    # Foydalanuvchini bazaga qo'shamiz
    if username:
        try:
            db.add_user(id=id, name=name, email=username)
        except sqlite3.IntegrityError as err:
            pass
    else:
        try:
            db.add_user(id=id, name=name)
        except sqlite3.IntegrityError as err:
            pass
    xabar=f"Assalomu Alaykum. <b>{name}.</b>\n✅✅Imlo-Xato botiga Xush Kelibsiz!"
    await message.answer(xabar,reply_markup=Menu)
    # Adminga xabar beramiz
    count = db.count_users()[0]
    msg  = f"<b>Boshliq botga odam qo'shildi</b>\n\n"
    msg += f"<b>@{username}</b>\n "
    msg += f"<b>{name}</b>\n"
    msg += f" <b>{id}</b>\n\n"
    msg += f"Bazada <b>{count}</b> ta foydalanuvchi bor."
    await bot.send_message(chat_id="5280188027", text=msg ,reply_markup=Menu)



@dp.message_handler(text="Imlo-Qoida✅")
async def send_link(message: types.Message):
    await message.answer("So'z yuboring ",reply_markup=menugaqaytish)





@dp.message_handler(text="Valyuta Kursi💰")
async def send_link(message: types.Message):

    # url ga murojat qilib Kursni aniqlash.
    url_aqsh = f"https://v6.exchangerate-api.com/v6/{kod}/pair/{davlat_aqsh}/UZS"
    url_ru = f"https://v6.exchangerate-api.com/v6/{kod}/pair/{davlat_ru}/UZS"

    javob_aqsh = requests.get(url_aqsh)  # Saytdan qaytgan javob <requests> taminlayapmiz
    javob_ru = requests.get(url_ru)  # Saytdan qaytgan javob <requests> taminlayapmiz

    kurs_aqsh = javob_aqsh.json()
    kurs_ru = javob_ru.json()

    kurs_aqsh = kurs_aqsh['conversion_rate']
    kurs_ru = kurs_ru['conversion_rate']

    # sana va vaqtni aniqlash
    hozir=dt.datetime.now()
    sana=hozir.date()
    #soat=message.date.strftime("%H:%M:%S")

    javob =f"<b>Valyuta Kurslari💰</b>\n\n📅  {sana} \n"
    javob += f"\n\n<b>1-Aqsh dollar  = {math.ceil(kurs_aqsh)} so'm</b>"
    javob += f"\n<b>1-Russian ruble  = {math.ceil(kurs_ru)} so'm</b>"
    await message.answer(javob, reply_markup=menugaqaytish)



@dp.message_handler(text="🔙 Ortga")
async def send_link(message: types.Message):
    await message.answer("Asosiy menu ",reply_markup=Menu)