"""
Пакет кнопок для клавиатур
"""

__version__ = '0.1'

if __name__ != '__main__':
    print(f'\tВстроенный пакет {__name__} '
          f'ver-{__version__} успешно импортирован!')

from handlers.keyboards.buttons import special_chat_buttons
from handlers.keyboards.buttons import base_chat_buttons
