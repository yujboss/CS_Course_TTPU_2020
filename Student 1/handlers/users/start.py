import asyncio
from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart, Command
from aiogram.dispatcher import FSMContext
from loader import dp
from states import New
from utils.db_api import quick_commands



@dp.message_handler(Command('salom'))
async def bot_start(message: types.Message,state:FSMContext):
    await message.answer('Please insert your student_id')
    await New.student_id.set()

@dp.message_handler(state=New.student_id)
async def enter_email(message: types.Message, state: FSMContext):
    message_text = message.text
    users = await quick_commands.select_all_users()
    n = []
    for data in users:
        n.append(data.student_id)
    if message_text in n:
        print("studentID mavjud")
    [print(data) for data in users]
    await state.finish()



