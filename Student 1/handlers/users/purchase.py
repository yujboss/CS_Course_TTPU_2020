import logging
from aiogram.dispatcher.filters import Command
from aiogram.types import Message, CallbackQuery
from keyboards.inline.callback_datas import buy_callback,buy_call
from keyboards.inline.choice_buttons import level,faculty,point,course_name,professor
from loader import dp
from states.fsm import Fsm
from aiogram.dispatcher import FSMContext
from datetime import datetime
from utils.db_api import quick_commands as commands, quick_commands

now = datetime.now()

@dp.message_handler(Command("start"))
async def level_student(message: Message):
    await message.answer(text="Please insert your student_id:")
    await Fsm.student_id.set()
@dp.message_handler(state=Fsm.student_id)
async def level_student(message: Message , state: FSMContext):
    student_id = message.text
    users = await quick_commands.select_all_users()
    n = []
    for data in users:
        n.append(data.student_id)
    if student_id in n:
        await state.update_data(answer1=student_id)
        await message.answer(text="You are authorized to continue")
        await message.answer(text="Please select your academic level:",reply_markup=level)

        await Fsm.level.set()


    @dp.callback_query_handler(buy_callback.filter(item_name="PY"),state=Fsm.level)
    async def py_student(call: CallbackQuery, state: FSMContext,callback_data: dict):
        level= callback_data.get('item_name')
        await state.update_data(answer2=level)
        await call.answer(cache_time=60)
        await call.message.edit_text("Please select your Faculty",
                                  reply_markup=faculty,)

        await Fsm.faculty.set()
    @dp.callback_query_handler(buy_callback.filter(item_name="1st"),state=Fsm.level)
    async def st_student(call: CallbackQuery, state: FSMContext,callback_data: dict):
        level=callback_data.get('item_name')
        await state.update_data(answer2=level)
        await call.answer(cache_time=60)
        await call.message.edit_text("Please select your Faculty",
                                  reply_markup=faculty)
        await Fsm.faculty.set()
    @dp.callback_query_handler(buy_callback.filter(item_name="2nd"),state=Fsm.level)
    async def nd_student(call: CallbackQuery, state: FSMContext,callback_data: dict):
        level=callback_data.get('item_name')
        await state.update_data(answer2=level)
        await call.answer(cache_time=60)
        await call.message.edit_text("Please select your Faculty",
                                  reply_markup=faculty)
        await Fsm.faculty.set()
    @dp.callback_query_handler(buy_callback.filter(item_name="3rd"),state=Fsm.level)
    async def rd_student(call: CallbackQuery, state: FSMContext,callback_data: dict):
        level=callback_data.get('item_name')
        await state.update_data(answer2=level)
        await call.answer(cache_time=60)
        await call.message.edit_text("Please select your Faculty",
                                  reply_markup=faculty)
        await Fsm.faculty.set()

    # Faculty of Students
    @dp.callback_query_handler(buy_callback.filter(item_name="ME"),state=Fsm.faculty)
    async def me_student(call: CallbackQuery, state: FSMContext,callback_data: dict):
        faculty=callback_data.get('item_name')
        await state.update_data(answer3=faculty)
        await call.answer(cache_time=60)
        await call.message.edit_text("Please select your Course",
                                  reply_markup=course_name)
        await Fsm.course_name.set()
    @dp.callback_query_handler(buy_callback.filter(item_name="IT"),state=Fsm.faculty)
    async def it_student(call: CallbackQuery, state: FSMContext,callback_data: dict):
        faculty=callback_data.get('item_name')
        await state.update_data(answer3=faculty)
        await call.answer(cache_time=60)
        await call.message.edit_text("Please select your Course",
                                  reply_markup=course_name)
        await Fsm.course_name.set()
    @dp.callback_query_handler(buy_callback.filter(item_name="CIVIL"),state=Fsm.faculty)
    async def civil_student(call: CallbackQuery, state: FSMContext,callback_data: dict):
        faculty=callback_data.get('item_name')
        await state.update_data(answer3=faculty)
        await call.answer(cache_time=60)
        await call.message.edit_text("Please select your Course",
                                  reply_markup=course_name)
        await Fsm.course_name.set()


    # Course of Student
    @dp.callback_query_handler(buy_callback.filter(item_name="APA"),state=Fsm.course_name)
    async def apa_student(call: CallbackQuery, state: FSMContext,callback_data: dict):
        course_name=callback_data.get('item_name')
        await state.update_data(answer4=course_name)
        await call.answer(cache_time=60)
        await call.message.edit_text("Please select your professors ",
                                  reply_markup=professor)
        await Fsm.professor.set()
    @dp.callback_query_handler(buy_callback.filter(item_name="FMD"),state=Fsm.course_name)
    async def fmd_student(call: CallbackQuery, state: FSMContext,callback_data: dict):
        course_name=callback_data.get('item_name')
        await state.update_data(answer4=course_name)
        await call.answer(cache_time=60)
        await call.message.edit_text("Please select your professors ",
                                  reply_markup=professor)
        await Fsm.professor.set()

    @dp.callback_query_handler(buy_callback.filter(item_name="TATT"),state=Fsm.course_name)
    async def tatt_student(call: CallbackQuery, state: FSMContext,callback_data: dict):
        course_name=callback_data.get('item_name')
        await state.update_data(answer4=course_name)
        await call.answer(cache_time=60)
        await call.message.edit_text("Please select your professors ",
                                  reply_markup=professor)
        await Fsm.professor.set()


    @dp.callback_query_handler(buy_callback.filter(item_name="Yusupov"),state=Fsm.professor)
    async def professor_1(call: CallbackQuery, state: FSMContext,callback_data: dict):
        professor=callback_data.get('item_name')
        await state.update_data(answer5=professor)
        await call.answer(cache_time=60)
        await call.message.edit_text("Please select number from min(1) to max(5) ",
                                  reply_markup=point)
        await Fsm.point.set()
    @dp.callback_query_handler(buy_callback.filter(item_name="Pirnazarov"),state=Fsm.professor)
    async def professor_2(call: CallbackQuery, state: FSMContext,callback_data: dict):
        professor=callback_data.get('item_name')
        await state.update_data(answer5=professor)
        await call.answer(cache_time=60)
        await call.message.edit_text("Please select number from min(1) to max(5) ",
                                  reply_markup=point)
        await Fsm.point.set()
    @dp.callback_query_handler(buy_callback.filter(item_name="Djalilov"),state=Fsm.professor)
    async def professor_3(call: CallbackQuery, state: FSMContext,callback_data: dict):
        professor=callback_data.get('item_name')
        await state.update_data(answer5=professor)
        await call.answer(cache_time=60)
        await call.message.edit_text("Please select number from min(1) to max(5) ",
                                  reply_markup=point)
        await Fsm.point.set()



    @dp.callback_query_handler(buy_call.filter(item_name="number"),state=Fsm.point)
    async def point_1(call: CallbackQuery, state: FSMContext,callback_data: dict):
        point = callback_data.get("quantity")
        await state.update_data(answer6=point)
        await call.answer(cache_time=60)
        data = await state.get_data()
        answer1 = data.get('answer1')
        answer2 = data.get('answer2')
        answer3 = data.get('answer3')
        answer4 = data.get('answer4')
        answer5 = data.get('answer5')
        answer6 = data.get('answer6')
        try:
            await commands.update_message(student_id=answer1,level=answer2,faculty=answer3,point=int(answer6),course_name=answer4,professor=answer5)
        except Exception:
            await commands.add_user(student_id=answer1,level=answer2,faculty=answer3,point=int(answer6),course_name=answer4,professor=answer5)
        await call.message.edit_text(f'Thank you!')
        await state.finish()
