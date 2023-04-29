"""
Отвечает за клавиатуры общего чата.

Для special_chat_handler.py, то есть для команд особого назначения

kb - keyboard
"""

from aiogram.types import InlineKeyboardMarkup, ReplyKeyboardMarkup

from handlers.keyboards.buttons import special_chat_buttons as s_buttons

from another_scripts import DataBaseAPI

# Клавиатура команды start
start_kb = InlineKeyboardMarkup().add(
    s_buttons.start_acquaintance_btn)


# Клавиатура команды neko
async def neko_kb() -> (ReplyKeyboardMarkup, list[str]):
    """
    Создаёт NekoKeyBoard для neko_response

    :return (ReplyKeyboardMarkup, list[str]): Клавиатуру и список с именами Neko
    """
    neko_name_list: list[str] = await DataBaseAPI.request_record(
        base_name='Neko', path='NekoData', key="Name's")

    # Создание объекта клавиатуры
    neko_kb = ReplyKeyboardMarkup(
        resize_keyboard=True,
        one_time_keyboard=True)

    for neko in neko_name_list:
        neko_kb.add(s_buttons.create_btn(neko))

        return neko_kb, neko_name_list


# Клавиатура оценки Neko
neko_evaluation_kb = InlineKeyboardMarkup().row(s_buttons.neko_like_btn,
                                                s_buttons.neko_dislike_btn)
