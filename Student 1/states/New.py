from aiogram.dispatcher.filters.state import StatesGroup,State


class New(StatesGroup):
    student_id = State()