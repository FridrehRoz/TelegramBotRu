from aiogram import types
from bot_start import *

from aiogram.utils.exceptions import BotBlocked


@dp.errors_handler(exception=BotBlocked)
async def BotBlocked_response(update: types.Update,
                              exception: BotBlocked) -> bool:
    print('Ошибка отправки сообщения, бот заблокирован!\n', exception)

    return True
