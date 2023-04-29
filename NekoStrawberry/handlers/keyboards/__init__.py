"""
Пакет keyboard-ов для закрепления клавиатур в чатах.
"""

__version__ = '0.1'

if __name__ != '__main__':
    print(f'\tВстроенный пакет {__name__} '
          f'ver-{__version__} успешно импортирован!')

from handlers.keyboards import special_chat_keyboard
from handlers.keyboards import base_chat_keyboard
