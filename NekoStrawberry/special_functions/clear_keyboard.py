"""
Используется для чистки клавиатур
"""

from aiogram import types

from special_functions.pause_async import pause


async def clear_ReplyKeyboardMarkup(message: types.Message) -> None:
    """
    Отправляет сообщение для дальнейшего удаление клавиатуры.

    Тип клавиатуры ReplyKeyboardMarkup
    :param message:
    """
    await pause()

    msg = await message.answer(
        text='<code>Очистка клавиатуры!</code>',
        reply_markup=types.ReplyKeyboardRemove(),
        parse_mode='HTML')

    await msg.delete()
