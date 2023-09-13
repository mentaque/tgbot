from aiogram.types import KeyboardButton, ReplyKeyboardMarkup, InlineKeyboardButton, InlineKeyboardMarkup

main_kb = [
    [KeyboardButton(text='Каталог'),
     KeyboardButton(text='Корзина')],
    [KeyboardButton(text='Мой профиль'),
     KeyboardButton(text='Контакты')]
]

main = ReplyKeyboardMarkup(keyboard=main_kb,
                           resize_keyboard=True,
                           input_field_placeholder='Выберите пункт')

socials_kb = [
    [InlineKeyboardButton(text='Telegram', url='web.telegram.org')],
    [InlineKeyboardButton(text='YouTube', url='youtube.com')]
]

socials = InlineKeyboardMarkup(inline_keyboard=socials_kb)

catalog = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='adidas', callback_data='adidas')],
    [InlineKeyboardButton(text='nike', callback_data='nike')]
])