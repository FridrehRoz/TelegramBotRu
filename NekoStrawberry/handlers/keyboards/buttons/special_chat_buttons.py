"""
Здесь находятся кнопки для клавиатуры special_chat_handler.py

btn - button
"""

from aiogram.types import InlineKeyboardButton, KeyboardButton

# Кнопка для сообщения в ЛС бота
start_acquaintance_btn = InlineKeyboardButton(
    text='Сделай ТЫК!',
    url='https://t.me/YourNeko_ShopBot?start=chat')


async def create_btn(label: str, prefix: str = '') -> KeyboardButton:
    """
    Создаёт кнопку KeyboardButton для ReplyKeyboardMarkup

    :param label: название кнопки
    :param prefix: префикс текста кнопки
    """
    btn = KeyboardButton(prefix + label)

    return btn


# Кнопки neko_evaluation клавиатуры для оценки Neko
neko_like_btn = InlineKeyboardButton(text='❤️',
                                     callback_data='neko_like')
neko_dislike_btn = InlineKeyboardButton(text='👎',
                                        callback_data='neko_dislike')
