from aiogram.dispatcher.filters.state import StatesGroup,State


class Fsm(StatesGroup):
    student_id = State()
    level= State()
    faculty = State()
    course_name = State()
    point = State()
    professor = State()