from aiogram.dispatcher.filters.state import StatesGroup,State


class Admin(StatesGroup):
    student_id = State()