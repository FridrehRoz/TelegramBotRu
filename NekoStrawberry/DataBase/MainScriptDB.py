"""
Функции для создания и обновления записей и БД при помощи модуля shelve

@NekoRoom
"""

__version__ = '1.0'

import shelve
from dataclasses import dataclass


@dataclass
class DataDB:
    pass


def update_base(base_name: str, path: str) -> None:
    """
    Обновляет файл базы данных shelve

    :param base_name: имя БД
    :param path: путь к папке в директории скрипта
    """
    old_data: dict = {}

    if [attr for attr in dir(DataDB) if not attr.startswith('__')]:
        pass
    else:
        print('Вы не заполнили data!')
        return None

    print('Считывание БД...')
    try:
        with shelve.open(rf'{path}\{base_name}', 'r') as db:
            for key, value in db.items():
                old_data[key] = value
    except FileNotFoundError as error:
        print('Файл БД не был найден!\n', error)
    except Exception as error:
        print('Ошибка обновления БД\n', error)
    finally:
        print('Считывание БД завершено!')

    print('Обновление записей БД...')

    for key in old_data.keys():
        try:
            if key in dir(DataDB):
                if getattr(DataDB, key) != old_data[key]:
                    new_data = getattr(DataDB, key)
                    update_data = list(set(new_data + old_data[key]))

                    setattr(DataDB, key, update_data)  # Установка новых данных
        except KeyError:
            DataDB.key = old_data[key]
    create_new_base(base_name)


def create_new_base(base_name: str, path: str) -> None:
    """
    Создаёт новый файл базы данных shelve

    :param base_name: название базы данных
    :param path: путь к папке в директории скрипта
    """

    data_keys = [attr for attr in dir(DataDB) if not attr.startswith('__')]
    if data_keys:
        with shelve.open(rf'{path}\{base_name}', 'c') as db:
            for key in data_keys:
                db[key] = getattr(DataDB, key)
            else:
                print('Заполнение БД, окончено!')
    else:
        print('Вы не заполнили DataDB')

    for key in data_keys:
        delattr(DataDB, key)
    else:
        print('data очищена!')


def create_data() -> None:
    """
    Заполняет DataDB данными
    """
    data_types = ['str', 'int', 'list[int]', 'list[str]']

    while True:
        key = input('Введите имя ключа: ')
        if key and not key.startswith('__'):
            print('Введите тип значений из списка:')
            for data_type in data_types:
                print(f'\t{data_type}')

            data_type = input('Ваш выбор:')
            match data_type:
                case 'str':
                    value = input('Введите значениe: ')
                case 'int':
                    value = int(input('Введите значениe: '))
                case 'list[int]':
                    value = list(map(int, input('Введите значения: ').split()))
                case 'list[str]':
                    value = list(map(str, input('Введите значения: ').split()))

            if value:
                setattr(DataDB, key, value)
                print(f'Ключ {key} заполнен {value}')

                if input('Продолжить? ').lower() not in ('yes', 'y'):
                    break

            else:
                print('Вы не указали значение!')
        else:
            print('Вы не указали ключ!')

    print('Заполнение окончено!', 'Ваши ключи и значения:', sep='\n')
    for attr in (attr for attr in dir(DataDB) if not attr.startswith('__')):
        print(f'{attr}: {getattr(DataDB, attr)}')


def get_record(base_name: str, path: str, key: str) -> any:
    """
    Используется для получения записи из БД

    :param base_name: имя файла БД
    :param path: путь к директории файла БД
    :param key: название ключа в БД

    return: list[str], list[int], str, int
    """
    try:
        with shelve.open(rf'{path}\{base_name}', 'r') as db:
            if key in db.keys():
                return db[key]
            else:
                return None
    except Exception as error:
        print('Ошибка  открытия БД\n', error)


if __name__ == '__main__':
    while True:
        print("""
        Выберите действие с БД:
            1. Подготовить данные.
            2. Создать БД файл.
            3. Обновить БД.
            4. Получить запись.
        """)
        choice = int(input('Выбор: '))

        match choice:
            case 1:
                create_data()
            case 2:
                name = input('Введите название БД: ')
                base_path = input('Введите путь: ')
                create_new_base(base_name=name, path=base_path)
            case 3:
                name = input('Введите название БД: ')
                base_path = input('Введите путь: ')
                update_base(base_name=name, path=base_path)
            case 4:
                name = input('Введите название БД: ')
                base_path = input('Введите путь: ')
                record_key = input('Введите ключ: ')
                get_record(base_name=name, path=base_path, key=record_key)
