"""
Пакет для особых функций.
"""

__version__ = '0.1'

if __name__ != '__main__':
    print(f'\nИнициализация пакета {__name__} ver-{__version__}',
          '*' * 30, sep='\n')

from special_variables.bot_start_variables import package_is_imported

from special_functions import clear_keyboard
from special_functions import pause_async

package_is_imported()
print('\n')
