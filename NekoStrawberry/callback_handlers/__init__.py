"""
Пакет callback_handler-ов для перехвата и дальнейших действий.
"""

__version__ = '0.1'

if __name__ != '__main__':
    print(f'\nИнициализация пакета {__name__} ver-{__version__}',
          '*' * 30, sep='\n')

from special_variables.bot_start_variables import package_is_imported

from callback_handlers import base_chat_callback_handler
from callback_handlers import special_chat_callback_handler

package_is_imported()
print('\n')
