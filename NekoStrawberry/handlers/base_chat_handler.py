"""
Используется для общего чата/обсуждения.

Рассматриваются команды общего назначения.
"""

from aiogram import types

from bot_start import *
from handlers.keyboards import base_chat_keyboard as b_keyboard


from special_functions.pause_async import pause


@dp.message_handler(commands=['r'])
async def r_response(message: types.Message) -> None:
    """
    Повторяет введённое сообщение.

    :param message:
    """
    await message.answer(text=message.text[3:].lower())


@dp.message_handler(commands=['yourName', 'myName', 'masterName'])
async def name_response(message: types.Message) -> None:
    """
    Отвечает на вопрос об имени.

    :param message:
    """
    match message.text.split()[0]:
        case '/yourName':
            me = await bot.get_me()

            await message.answer('Что за глупый вопрос?')

            await pause()

            await message.answer(text=('Конечно же я КоШеЧкА!\n'
                                       f'Но зови меня {me.first_name}'))

        case '/myName':
            await message.answer('Пфф, легко!')

            await pause()

            await message.answer(f'Твоя кличка котик: '
                                 f'{message.from_user.first_name}')

        case '/masterName':
            await message.answer(
                text='Он ❤️<b>ХОЗЯИН</b>❤️ всех девочек-кошечек в мире!!!',
                parse_mode='HTML')
