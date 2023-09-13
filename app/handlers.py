from aiogram import Router, F
from aiogram.types import Message

from app import keyboards
from app.api import get_crypto_price

router = Router()

@router.message(F.text == '/start')
async def starting(message: Message):
    await message.answer('Добро пожаловать', reply_markup=keyboards.main)


@router.message(F.text == 'BTC')
async def crypto(message: Message):
    price = await get_crypto_price(message.text)
    await message.answer(price)