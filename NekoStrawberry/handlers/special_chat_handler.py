"""
Используется для общего чата/обсуждения.

Но рассматриваются команды особого назначения
"""

from aiogram import types
from bot_start import *

from aiogram.dispatcher.filters import Text
from aiogram.dispatcher import FSMContext

from handlers.keyboards import special_chat_keyboard as s_keyboard
from bot_status import special_chat_status as s_status

from another_scripts import DataBaseAPI
from asyncio import create_task


@dp.message_handler(commands=['start'])
async def start_response(message: types.Message) -> None:
    """
    Обрабатывает команду /start

    Предполагается для первого знакомства с ботом, в ЛС
    :param message:
    """
    if str(message.chat.id) == CHAT_ID:
        await message.answer('Давайте познакомимся, хозяин!',
                             reply_markup=s_keyboard.start_kb)
    else:
        await message.answer('Мы с вами уже знакомы!')

    await message.delete()


@dp.message_handler(commands=['neko'])
async def neko_response(message: types.Message) -> None:
    """
    Предлагает выбрать кошечку.

    :param message:
    """

    # Клавиатура и список имён кошечек
    keyboard, neko_name = s_keyboard.neko_kb()

    await message.answer('Выберите кошечку!',
                         reply_markup=keyboard)

    s_status.NekoEvaluationStatus.neko_name_list = neko_name
    await s_status.NekoEvaluationStatus.neko_choice.set()

    await message.delete()


@dp.message_handler(Text(
    equals=s_status.NekoEvaluationStatus.neko_name_list),
    state=s_status.NekoEvaluationStatus.neko_choice)
async def neko_evaluation_response(message: types.Message,
                                   state: FSMContext) -> None:
    """
    Отправляет кошечку из NekoPara

    callback: neko_evaluation_callback_response
    state: NekoEvaluationStatus
    :param message:
    :param state:
    """
    from special_functions import clear_keyboard

    await s_status.NekoEvaluationStatus.next()

    neko_name: str = message.text.split()[0]
    neko_photo: dict = DataBaseAPI.request_record(base_name='Neko',
                                                  key="Photo's")

    if neko_name not in neko_photo.keys():
        photo: str = DataBaseAPI.request_record(
            base_name='Error',
            key='NekoNotFound')
    else:
        photo: str = neko_photo[neko_name]

    create_task(
        clear_keyboard.clear_ReplyKeyboardMarkup(message))

    await bot.send_photo(
        chat_id=message.chat.id,
        caption='Нажми сердечко за кошечку!!!',
        photo=(photo),
        reply_markup=s_keyboard.neko_evaluation_kb)

    await message.delete()
