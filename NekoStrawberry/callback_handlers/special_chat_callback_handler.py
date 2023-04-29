"""
Используется для специальных команд чата.
"""

from aiogram.dispatcher import FSMContext
from aiogram.utils.callback_data import types
from bot_start import *

from special_functions.pause_async import pause
from bot_status import special_chat_status as s_status


@dp.callback_query_handler(lambda tag: tag.data.startswith('neko'),
                           state=s_status.NekoEvaluationStatus.neko_answer)
async def neko_callback_response(callback: types.CallbackQuery,
                                 state: FSMContext) -> None:
    """
    Реагирует на оценку Neko

    tag - neko
    :param callback:
    """
    await bot.edit_message_reply_markup(
        chat_id=CHAT_ID,
        message_id=callback.message.message_id,
        reply_markup=None)

    match callback.data:
        case 'neko_like':
            await callback.answer(
                text='Иначе и не могло быть. ฅ^•ﻌ•^ฅ',
                cache_time=3)

            await pause()

            await bot.edit_message_caption(
                caption='Кошечка довольна!',
                chat_id=CHAT_ID,
                message_id=callback.message.message_id, )

        case 'neko_dislike':
            await callback.answer(
                text='Все кошечки запомнят твой ответ /ᐠ - ˕ -マ Ⳋ',
                cache_time=3)

            await pause()

            await bot.edit_message_caption(
                caption='Кошечка расстроена!',
                chat_id=CHAT_ID,
                message_id=callback.message.message_id, )

    s_status.NekoEvaluationStatus.neko_name_list.clear()
    await state.finish()
