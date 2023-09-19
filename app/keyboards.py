from aiogram.types import KeyboardButton, ReplyKeyboardMarkup, InlineKeyboardButton, InlineKeyboardMarkup

main_kb = [
    [KeyboardButton(text='Мой профиль'),
     KeyboardButton(text='Котировки')]
]

main = ReplyKeyboardMarkup(keyboard=main_kb,
                           resize_keyboard=True,
                           input_field_placeholder='Выберите пункт')

crypto = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='BTC', callback_data='crypto_BTC')],
    [InlineKeyboardButton(text='ETH', callback_data='crypto_ETH')]
])

profile = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Подписки', callback_data='subscription')],
    [InlineKeyboardButton(text='Что-то', callback_data='some')]
])


def payment(url, id):
    keybord = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text='Ссылка', url=url)],
        [InlineKeyboardButton(text='Проверить оплату', callback_data=f"id:{id}")]
    ])
    return keybord
