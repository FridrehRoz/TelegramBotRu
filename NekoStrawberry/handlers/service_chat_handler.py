"""
Используется для общего чата/обсуждения.

Перехватывает служебные команды
"""

from aiogram import types
from bot_start import *

from aiogram.dispatcher.filters import Text
from bot_status import special_chat_status as s_status


@dp.message_handler(commands="getChatID", commands_prefix='!')
async def getChatID_response(message: types.Message):
    """
    Отправляет ID чата в ЛС администратора

    :param message:
    """
    await bot.send_message(chat_id=message.from_user.id,
                           text=message.chat.id)


@dp.message_handler(commands="getMyID", commands_prefix='!')
async def getMyID_response(message: types.Message):
    """
    Отправляет ID чата в ЛС администратора

    :param message:
    """
    await bot.send_message(chat_id=message.from_user.id,
                           text=f'Ваш ID: {message.from_user.id}')
