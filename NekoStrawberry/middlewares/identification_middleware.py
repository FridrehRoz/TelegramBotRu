from aiogram.dispatcher.middlewares import BaseMiddleware
from aiogram.dispatcher.handler import CancelHandler

from bot_start import CHAT_ID, MASTER_ID
from aiogram import types


class IdChecker(BaseMiddleware):

    @staticmethod
    async def on_pre_process_update(update: types.Update, data: dict):
        """
        Прерывание от постороннего доступа

        :param update, data
        """
        if update.message.chat.id != CHAT_ID and \
                update.message.chat.id != MASTER_ID:
            CancelHandler()
