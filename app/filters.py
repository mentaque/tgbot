from aiogram.filters import Filter
from aiogram.types import Message


class Admin(Filter):
    async def __call__(self, message: Message) -> bool:
        return message.from_user.id in [5040534994]
