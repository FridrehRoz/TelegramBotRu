"""
Пакет error_handler-ов для перехвата ошибок.
"""

__version__ = '0.1'

if __name__ != '__main__':
    print(f'\nИнициализация пакета {__name__} ver-{__version__}',
          '*' * 30, sep='\n')

from special_variables.bot_start_variables import package_is_imported

package_is_imported()
print('\n')
