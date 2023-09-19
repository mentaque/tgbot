from aiogram import Router, F
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, CallbackQuery, InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton

from app import keyboards
from app.api import get_crypto_price
from app.database import session
from app.filters import Admin
from app.forms import Form
from app.models import User
from app.payment import create_payment, check_payment

router = Router()


@router.message(F.text == '/start')
async def starting(message: Message):
    user_id = message.from_user.id
    user_username = message.from_user.username
    existing_user = session.query(User).filter_by(id=user_id).first()
    if existing_user:
        await message.answer(f"С возвращением, {user_username}", reply_markup=keyboards.main)
    else:
        new_user = User(id=user_id, username=user_username)
        session.add(new_user)
        session.commit()
        await message.answer(f"Добро пожаловать, {user_username}", reply_markup=keyboards.main)


@router.message(Admin(), F.text == '/users')
async def admin(message: Message):
    user_objects = session.query(User).all()
    users = "\n".join([f"id: {user.id}, username: {user.username}" for user in user_objects])
    await message.answer(f"{users}")


@router.message(F.text == 'Котировки')
async def crypto(message: Message):
    await message.answer('Выберите котировку', reply_markup=keyboards.crypto)


@router.message(F.text == 'Мой профиль')
async def profile(message: Message):
    await message.answer('Выберите пункт', reply_markup=keyboards.profile)


@router.callback_query(F.data.startswith('subscription'))
async def subscription(callback: CallbackQuery):
    pass


@router.message(F.text == 'Подписка')
async def buy(message: Message):
    url, payment = create_payment()

    await message.answer('Ссылка на платеж', reply_markup=keyboards.payment(url, payment))


@router.callback_query(F.data.startswith('id'))
async def checking(callback: CallbackQuery):
    answer = check_payment(callback.data)
    if answer:
        await callback.answer(f'')
        await callback.message.answer(f"Платеж успешно прошёл")
    else:
        await callback.answer(f'')
        await callback.message.answer(f"Платеэ не прошёл")


@router.callback_query(F.data.startswith('crypto'))
async def callback_crypto(callback: CallbackQuery):
    coin = callback.data.split('_')[1]
    price = await get_crypto_price(coin)
    await callback.answer(f'')
    await callback.message.answer(f'{price}')


@router.message(F.text == 'Тест')
async def command_start(message: Message, state: FSMContext) -> None:
    await state.set_state(Form.name)
    await message.answer(
        "Hi there! What's your name?",
        reply_markup=ReplyKeyboardRemove(),
    )


@router.message(Form.name)
async def process_name(message: Message, state: FSMContext) -> None:
    await state.update_data(name=message.text)
    await state.set_state(Form.like_bots)
    await message.answer(
        f"Nice to meet you, {message.text}!\nDid you like to write bots?",
        reply_markup=ReplyKeyboardMarkup(
            keyboard=[
                [
                    KeyboardButton(text="Yes"),
                    KeyboardButton(text="No"),
                ]
            ],
            resize_keyboard=True,
        ),
    )


@router.message(Form.like_bots, F.text.casefold() == "yes")
async def process_like_write_bots(message: Message, state: FSMContext) -> None:
    await state.set_state(Form.language)

    await message.reply(
        "Cool! I'm too!\nWhat programming language did you use for it?",
        reply_markup=ReplyKeyboardRemove(),
    )


@router.message(Form.like_bots, F.text.casefold() == "no")
async def process_dont_like_write_bots(message: Message, state: FSMContext) -> None:
    await state.clear()
    await message.answer(
        "Not bad not terrible.\nSee you soon.",
        reply_markup=ReplyKeyboardRemove(),
    )


@router.message(Form.like_bots)
async def process_unknown_write_bots(message: Message) -> None:
    await message.reply("I don't understand you :(")