"""
Пакет handler-ов для перехвата и дальнейшей обработки.
"""

__version__ = '0.1'

if __name__ != '__main__':
    print(f'\nИнициализация пакета {__name__} ver-{__version__}',
          '*' * 30, sep='\n')

from special_variables.bot_start_variables import package_is_imported

from handlers import service_chat_handler
from handlers import special_chat_handler
from handlers import base_chat_handler

package_is_imported()
print('\n')
