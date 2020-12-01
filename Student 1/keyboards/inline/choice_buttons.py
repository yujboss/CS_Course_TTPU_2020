from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from keyboards.inline.callback_datas import buy_callback,buy_call


level = InlineKeyboardMarkup(row_width=4)
Py = InlineKeyboardButton(text="PY", callback_data=buy_callback.new(item_name="PY"))
level.insert(Py)
st = InlineKeyboardButton(text="1st",callback_data=buy_callback.new(item_name="1st"))
level.insert(st)
nd = InlineKeyboardButton(text="2nd",callback_data=buy_callback.new(item_name="2nd"))
level.insert(nd)
rd = InlineKeyboardButton(text="3rd",callback_data=buy_callback.new(item_name="3rd"))
level.insert(rd)


faculty = InlineKeyboardMarkup(row_width=4)
ME = InlineKeyboardButton(text="ME", callback_data=buy_callback.new(item_name="ME"))
faculty.insert(ME)
IT = InlineKeyboardButton(text="IT",callback_data=buy_callback.new(item_name="IT"))
faculty.insert(IT)
CL = InlineKeyboardButton(text="Civil",callback_data=buy_callback.new(item_name="CIVIL"))
faculty.insert(CL)


course_name = InlineKeyboardMarkup(row_width=3)
apa = InlineKeyboardButton(text="APA", callback_data=buy_callback.new(item_name="APA"))
course_name.insert(apa)
fmd = InlineKeyboardButton(text="FMD",callback_data=buy_callback.new(item_name="FMD"))
course_name.insert(fmd)
tatt = InlineKeyboardButton(text="TATT",callback_data=buy_callback.new(item_name="TATT"))
course_name.insert(tatt)


professor = InlineKeyboardMarkup(row_width=3)
professor_1 = InlineKeyboardButton(text="Yusopv", callback_data=buy_callback.new(item_name="Yusupov"))
professor.insert(professor_1)
professor_2 = InlineKeyboardButton(text="Pirnazarov",callback_data=buy_callback.new(item_name="Pirnazarov"))
professor.insert(professor_2)
professor_3 = InlineKeyboardButton(text="Djalilov",callback_data=buy_callback.new(item_name="Djalilov"))
professor.insert(professor_3)





point = InlineKeyboardMarkup(row_width=5)
one = InlineKeyboardButton(text="1", callback_data="buy:number:1")
point.insert(one)
two = InlineKeyboardButton(text="2", callback_data="buy:number:2")
point.insert(two)
three = InlineKeyboardButton(text="3", callback_data="buy:number:3")
point.insert(three)
four = InlineKeyboardButton(text="4", callback_data="buy:number:4")
point.insert(four)
five = InlineKeyboardButton(text="5", callback_data="buy:number:5")
point.insert(five)

