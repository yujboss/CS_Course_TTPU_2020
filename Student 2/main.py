import csv
from datetime import datetime
import find

from telegram import Bot
from telegram import Update
from telegram import InlineKeyboardButton
from telegram import InlineKeyboardMarkup
from telegram import ReplyKeyboardRemove
from telegram.ext import Updater
from telegram.ext import CommandHandler
from telegram.ext import MessageHandler
from telegram.ext import Filters
from telegram.ext import ConversationHandler
from telegram.ext import CallbackQueryHandler
from telegram.ext.dispatcher import run_async

from config import TG_TOKEN
from telegram.utils import request


CALLBACK_BUTTON1_PY = "callback_button1_py"
CALLBACK_BUTTON2_FIRST = "callback_button2_first"
CALLBACK_BUTTON3_SECOND = "callback_button3_second"
CALLBACK_BUTTON4_THIRD = "callback_button4_third"
CALLBACK_BUTTON5_IT = "callback_button5_it"
CALLBACK_BUTTON6_CIVIL = "callback_button6_civil"
CALLBACK_BUTTON7_ME = "callback_button7_me"
CALLBACK_BUTTON8_POINT1 = "callback_button8_point1"
CALLBACK_BUTTON9_POINT2 = "callback_button8_point2"
CALLBACK_BUTTON10_POINT3 = "callback_button8_point3"
CALLBACK_BUTTON11_POINT4 = "callback_button8_point4"
CALLBACK_BUTTON12_POINT5 = "callback_button8_point5"


ID, LEVEL, FACULTY, COURSE_NAME, PROFESSOR_NAME, POINT = \
	"studentID", "academic_level", "faculty", "course_name", "professor_surname", "point"


TITLES = {
	CALLBACK_BUTTON1_PY: "PY",
	CALLBACK_BUTTON2_FIRST: "1",
	CALLBACK_BUTTON3_SECOND: "2",
	CALLBACK_BUTTON4_THIRD: "3",
	CALLBACK_BUTTON5_IT: "IT",
	CALLBACK_BUTTON6_CIVIL: "Civil",
	CALLBACK_BUTTON7_ME: "ME",
	CALLBACK_BUTTON8_POINT1: "1",
	CALLBACK_BUTTON9_POINT2: "2",
	CALLBACK_BUTTON10_POINT3: "3",
	CALLBACK_BUTTON11_POINT4: "4",
	CALLBACK_BUTTON12_POINT5: "5",
}


def echo_handler(bot: Bot, update: Update):
	update.message.reply_text(
		"/start to start the session",
	)


def get_academic_level():
	keyboard = [
		[
			InlineKeyboardButton(TITLES[CALLBACK_BUTTON1_PY], callback_data=CALLBACK_BUTTON1_PY),
			InlineKeyboardButton(TITLES[CALLBACK_BUTTON2_FIRST], callback_data=CALLBACK_BUTTON2_FIRST),
			InlineKeyboardButton(TITLES[CALLBACK_BUTTON3_SECOND], callback_data=CALLBACK_BUTTON3_SECOND),
			InlineKeyboardButton(TITLES[CALLBACK_BUTTON4_THIRD], callback_data=CALLBACK_BUTTON4_THIRD),
		]
	]

	return InlineKeyboardMarkup(keyboard)


def get_faculty():
	keyboard = [
		[
			InlineKeyboardButton(TITLES[CALLBACK_BUTTON5_IT], callback_data=CALLBACK_BUTTON5_IT),
			InlineKeyboardButton(TITLES[CALLBACK_BUTTON6_CIVIL], callback_data=CALLBACK_BUTTON6_CIVIL),
			InlineKeyboardButton(TITLES[CALLBACK_BUTTON7_ME], callback_data=CALLBACK_BUTTON7_ME),
		]
	]

	return InlineKeyboardMarkup(keyboard)


def get_points():
	keyboard = [
		[
			InlineKeyboardButton(TITLES[CALLBACK_BUTTON8_POINT1], callback_data=CALLBACK_BUTTON8_POINT1),
			InlineKeyboardButton(TITLES[CALLBACK_BUTTON9_POINT2], callback_data=CALLBACK_BUTTON9_POINT2),
		],
		[
			InlineKeyboardButton(TITLES[CALLBACK_BUTTON10_POINT3], callback_data=CALLBACK_BUTTON10_POINT3),
			InlineKeyboardButton(TITLES[CALLBACK_BUTTON11_POINT4], callback_data=CALLBACK_BUTTON11_POINT4),
			InlineKeyboardButton(TITLES[CALLBACK_BUTTON12_POINT5], callback_data=CALLBACK_BUTTON12_POINT5),
		]
	]

	return InlineKeyboardMarkup(keyboard)


def start_handler(bot: Bot, update: Update, user_data: dict):
	user_data["log"] = datetime.now()
	bot.send_message(
		chat_id=update.message.chat_id,
		text="Please insert your correct student ID",
	)
	return ID


@run_async
def id_handler(bot: Bot, update: Update, user_data: dict):
	if find.find(update.message.text):
		user_data[ID] = update.message.text
		update.message.reply_text(
			"Please choose your academic level",
			reply_markup=get_academic_level()
		)
		return LEVEL
	else:
		return ID


def course_name_handler(bot: Bot, update: Update, user_data: dict):
	user_data[COURSE_NAME] = update.message.text
	update.message.reply_text(
		"Please choose your professor's last name",
		reply_markup=ReplyKeyboardRemove(),
	)
	return PROFESSOR_NAME


def professor_name_handler(bot: Bot, update: Update, user_data: dict):
	user_data[PROFESSOR_NAME] = update.message.text
	update.message.reply_text(
		"Evaluate the delivery of the course",
		reply_markup=get_points(),
	)
	return POINT


def keyboard_callback_handler(bot: Bot, update: Update, user_data: dict, chat_data=None, **kwargs):
	query = update.callback_query
	data = query.data

	if data in (CALLBACK_BUTTON1_PY, CALLBACK_BUTTON2_FIRST, CALLBACK_BUTTON3_SECOND, CALLBACK_BUTTON4_THIRD):
		level_choice = {
			CALLBACK_BUTTON1_PY: "PY",
			CALLBACK_BUTTON2_FIRST: "1",
			CALLBACK_BUTTON3_SECOND: "2",
			CALLBACK_BUTTON4_THIRD: "3"
		}[data]
		user_data[LEVEL] = level_choice
		query.edit_message_text(
			text="Please select your faculty",
			reply_markup=get_faculty(),
		)
		return FACULTY
	elif data in (CALLBACK_BUTTON5_IT, CALLBACK_BUTTON6_CIVIL, CALLBACK_BUTTON7_ME):
		faculty_choice = {
			CALLBACK_BUTTON5_IT: "IT",
			CALLBACK_BUTTON6_CIVIL: "Civil",
			CALLBACK_BUTTON7_ME: "ME"
		}[data]
		user_data[FACULTY] = faculty_choice
		query.edit_message_text(
			text="Please enter course name",
		)
		return COURSE_NAME
	elif data in (
			CALLBACK_BUTTON8_POINT1,
			CALLBACK_BUTTON9_POINT2,
			CALLBACK_BUTTON10_POINT3,
			CALLBACK_BUTTON11_POINT4,
			CALLBACK_BUTTON12_POINT5):
		point_choice = {
			CALLBACK_BUTTON8_POINT1: "1",
			CALLBACK_BUTTON9_POINT2: "2",
			CALLBACK_BUTTON10_POINT3: "3",
			CALLBACK_BUTTON11_POINT4: "4",
			CALLBACK_BUTTON12_POINT5: "5",
		}[data]
		user_data[POINT] = point_choice
		with open("database.csv", "a") as base:
			field_names = ['studentID', 'log', 'point', 'academic_level', 'faculty', 'course_name', 'professor_surname']
			data_writer = csv.DictWriter(base, fieldnames=field_names)

			data_writer.writerow(user_data)
		query.edit_message_text(
			text="All data has been saved!",
		)
		print(user_data)
		return ConversationHandler.END


def cancel_handler(bot: Bot, update: Update):
	update.message.reply_text('Operation canceled. no data has been saved!', reply_markup=ReplyKeyboardRemove())
	return ConversationHandler.END


def main():

	bot = Bot(token=TG_TOKEN)
	updater = Updater(bot=bot)

	buttons_handler = CallbackQueryHandler(callback=keyboard_callback_handler, pass_user_data=True)

	conv_handler = ConversationHandler(
		entry_points=[
			CommandHandler("start", start_handler, pass_user_data=True)
		],
		states={
			ID: [
				MessageHandler(Filters.all, id_handler, pass_user_data=True),
			],
			LEVEL: [
				CallbackQueryHandler(keyboard_callback_handler, pass_user_data=True),
			],
			FACULTY: [
				CallbackQueryHandler(keyboard_callback_handler, pass_user_data=True),
			],
			COURSE_NAME: [
				MessageHandler(Filters.all, course_name_handler, pass_user_data=True),
			],
			PROFESSOR_NAME: [
				MessageHandler(Filters.all, professor_name_handler, pass_user_data=True),
			],
			POINT: [
				CallbackQueryHandler(keyboard_callback_handler, pass_user_data=True),
			]
		},
		fallbacks={
			CommandHandler("cancel", cancel_handler)
		}
	)

	updater.dispatcher.add_handler(conv_handler)
	updater.dispatcher.add_handler(buttons_handler)
	updater.dispatcher.add_handler(MessageHandler(Filters.all, echo_handler))

	updater.start_polling()
	updater.idle()


if __name__ == '__main__':
	main()

