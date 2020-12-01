from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

level = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="PY"),
            KeyboardButton(text="1st"),
            KeyboardButton(text="2nd"),
            KeyboardButton(text="3rd"),
        ],
    ],
    resize_keyboard=True
)

faculty = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="ME"),
            KeyboardButton(text="IT"),
            KeyboardButton(text="CIVIL"),
        ],
    ],
    resize_keyboard=True
)
course_name = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="APA"),
            KeyboardButton(text="FMD"),
            KeyboardButton(text="TATT"),
        ],
    ],
    resize_keyboard=True
)
point = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="1"),
            KeyboardButton(text="2"),
            KeyboardButton(text="3"),
            KeyboardButton(text="4"),
            KeyboardButton(text="5"),
        ],
    ],
    resize_keyboard=True
)


