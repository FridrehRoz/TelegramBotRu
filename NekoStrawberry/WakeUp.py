"""
Основной скрипт бота чата

NekoStrawberry

@NekoRoom
"""

__version__ = '1.0'
__author__ = 'NekoMaster'

import os

if __name__ == '__main__':
    from art import tprint

    tprint('NekoBotStrawberry')
    tprint(f'ver {__version__} ')
    os.system('title NekoStrawberry')

from special_variables.bot_start_variables import \
    imported_modules_bar as import_bar

from aiogram import executor

from bot_start import *
from middlewares import *
from another_scripts import *
from special_functions import *
from handlers import *
from callback_handlers import *
from error_handlers import *


async def on_startup(_):
    """
    Уведомляет о запуске бота.

    В cmd окне и чат-группе.
    """
    print('Neko вышла в онлайн!!!')
    await bot.send_message(chat_id=MASTER_ID,
                           text='Здравствуйте хозяин!')
    await bot.send_message(chat_id=CHAT_ID,
                           text='Клубничка вошла в чат!')


try:
    executor.start_polling(dispatcher=dp,
                           skip_updates=True,
                           on_startup=on_startup)
except Exception as error:
    print('Ошибка запуска сеанса!\n', error)
finally:
    print('Strawberry ушла спать.')
