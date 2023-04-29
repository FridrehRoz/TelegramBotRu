"""
Специальные переменные на этапе старта бота.
"""

from tqdm import tqdm
from time import sleep

imported_modules_bar = tqdm(total=7)
imported_modules_bar.set_description('Imported packages')


def package_is_imported():
    """
    Обновляет progress bar импортированных модулей
    """
    if imported_modules_bar.n != imported_modules_bar.total:
        imported_modules_bar.update()
        sleep(1)
    else:
        imported_modules_bar.close()
