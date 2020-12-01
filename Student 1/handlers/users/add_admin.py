from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.builtin import Command
from states.admin import Admin
from loader import dp, db
from utils.db_api.quick_commands import add_user


@dp.message_handler(Command("admin"))
async def bot_get_email(message: types.Message, state: FSMContext):
    await message.answer("Add user")
    await Admin.student_id.set()


@dp.message_handler(state=Admin.student_id)
async def enter_email(message: types.Message, state: FSMContext):
    message_user = message.text
    await add_user(student_id=message_user)
    await message.answer(f'Added {message_user}')
    await state.finish()
