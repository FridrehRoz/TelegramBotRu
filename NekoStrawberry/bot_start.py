"""
Отвечает за регистрацию бота и диспетчера
"""

__all__ = ['bot', 'dp', 'CHAT_ID', 'MASTER_ID']
__version__ = '1.0'

if __name__ != '__main__':
    print(f'\nИмпортирован модуль {__name__} ver-{__version__}',
          '*' * 30, sep='\n')

from special_variables.bot_start_variables import package_is_imported

from aiogram import Bot  # сервер взаимодействующий с API Telegram
from aiogram import Dispatcher  # отслеживает действия чата
from aiogram.contrib.fsm_storage.memory import MemoryStorage  # озу бота
import aiogram.utils.exceptions as aiogram_exception

import os

storage = MemoryStorage()

CHAT_ID: str = os.getenv('CHAT_ID')  # Id чата обсуждения
MASTER_ID: str = os.getenv('MASTER_ID')

try:
    bot = Bot(token=os.getenv('TOKEN'),
              parse_mode='HTML',
              protect_content=True)  # подключение к Telegram API
except aiogram_exception.ValidationError('Token is invalid!'):
    print('\tИнвалидный токен бота!')
except aiogram_exception as error:
    print(f'\tОшибка назначения бота библиотеки aiogram!\n{error}')
except Exception as error:
    print(f'\tВнешняя ошибка при регистрации бота!\n{error}')
finally:
    print('\tБот успешно зарегистрирован!')

try:
    dp = Dispatcher(bot=bot, storage=storage)
except aiogram_exception as error:
    print(f'\tОшибка назначения диспетчера!\n{error}')
except Exception as error:
    print(f'\tВнешняя ошибка при назначении диспетчера!\n{error}')
finally:
    print('\tДиспетчер успешно назначен!')

package_is_imported()
print('\n')
