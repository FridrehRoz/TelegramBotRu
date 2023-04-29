"""
Интерфейс бота для работы с БД модуля shelve

Через команды чата и команд скриптов
"""

from DataBase import MainScriptDB


async def request_record(base_name: str, path: str, key: str) -> any:
    """
    Запрос на запись из БД
    """
    record = await MainScriptDB.get_record(base_name, path, key)
    if record is None:
        return 'error'
    else:
        return record
