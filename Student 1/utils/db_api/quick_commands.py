from typing import List

from aiogram.utils.helper import Item
from asyncpg import UniqueViolationError
from utils.db_api.schemas.user import User


async def add_user(student_id: str,level: str=None,faculty: str=None,point:int=None,course_name:str=None,professor:str=None):
    try:
        user = User(student_id=student_id,
                    level=level,
                    faculty=faculty,
                    course_name=course_name,
                    point=point,
                    professor=professor)

        await user.create()
    except UniqueViolationError:
        pass

async def update_message(student_id,level,faculty,point,course_name,professor):
    user = await User.get(student_id)
    await user.update(point=point,
                      level=level,
                      faculty=faculty,
                      course_name=course_name,
                      professor=professor).apply()


async def select_user(student_id:str):
    user = await User.query.where(User.student_id == student_id).gino.first()
    return user


async def select_all_users():
    users = await User.query.gino.all()
    return users






