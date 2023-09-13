import asyncio
from aiogram import Dispatcher, Bot
from app.handlers import router


async def main() -> None:
    TOKEN = '6518938551:AAESwp9UnDCMwe7NAUEDOYpITFMK1VXVdxs'
    dp = Dispatcher()
    bot = Bot(TOKEN)
    dp.include_router(router)
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
