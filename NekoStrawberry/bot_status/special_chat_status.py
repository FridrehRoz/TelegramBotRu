from aiogram.dispatcher.filters.state import StatesGroup, State


class NekoEvaluationStatus(StatesGroup):
    """
    Отвечает за статус для handler-а neko_evaluation
    """
    neko_name_list = []
    neko_choice = State()
    neko_answer = State()
