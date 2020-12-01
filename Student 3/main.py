import telebot
import csv
from datetime import datetime
from telebot import types

BOT_API = '1358739142:AAFpoP05oyJ4-E_kzzROuCnFrBHVgT1fPVM'

bot = telebot.TeleBot(BOT_API)


def startDayTime():
    now = datetime.today().hour
    return (
        "Доброе утро" if 5 <= now <= 11
        else
        "Добрый день" if 12 <= now <= 17
        else
        "Добрый вечер" if 18 <= now <= 22
        else
        "Здраствуйте"
    )


file_name = "students.csv"

bad_command_text = "Неправильная комманда !\n"

bad_registration_text = "Неправильная попытка регистрации !\n\nВведите\n /login ID\n\nПример\n /login u10000"

bad_id_text = "Вы ввели непраивльное ID\n"

all_temp_data = []

start_text = str(startDayTime()) + \
             "\nЧтобы зарегестрировать нового пользователья, пожалуйста введите команду /login + ID\n" \
             "\nДля просмотра комманд /help"

help_request_text = "Список комманд : \n" \
                    "\n/start : для запуска бота\n" \
                  "\n/login : для регистрации\n" \
                    "\n/me : для получения данных о себе\n" \
                    "\n/about : для получения данных о боте\n" \
                    "\n/help : для получения списка комманд"


about_text = "TTPU SURVEY BOT \n v 1.0"

try_again_text = "Пожалуйста повторите попытку"

academic_levels = ["PY", "1st", "2nd", "3rd"]
faculty_list = ["IT", "Civil", "Me"]
rating_list = ["5", "4", "3", "2", "1"]


def sendMessage(chat_id, text):
    bot.send_message(chat_id, text)


@bot.message_handler(commands=['start'])
def start_message(message):
    sendMessage(message.chat.id, start_text)


@bot.message_handler(commands=['about'])
def start_message(message):
    sendMessage(message.chat.id, about_text)


@bot.message_handler(commands=['me'])
def start_message(message):
    PrintUserData(message)


def PrintUserData(chat_data):
    chatData = chat_data
    userName = chatData.from_user.first_name
    userData = getUserDataFromBase(userName)
    if userData == "NULL_DATA_EXCEPTION":
        sendMessage(chatData.chat.id, "Ваших данные нет в базе !\nПожалуйста пройдите регистрацию !")
    else:
        sendMessage(chatData.chat.id, f'Данные : \n\nID : {userData[0]} \n\n'
                                      f'Имя : {userData[1]} \n\n'
                                      f'Уровень : {userData[2]} \n\n'
                                      f'факультет : {userData[3]} \n\n'
                                      f'Оценка : {userData[4]} \n\n'
                                      f'Дата : {userData[5]} \n\n')


def getUserDataFromBase(user_name):
    data = "NULL_DATA_EXCEPTION"
    with open(file_name, "rt") as csv_file:
        users_all_names = csv.reader(csv_file)
        for current_data in users_all_names:
            if current_data[1] == user_name:
                data = current_data
    return data


@bot.message_handler(commands=['help'])
def start_message(message):
    sendMessage(message.chat.id, help_request_text)


def drawButtons(chat_data, buttons_array, main_text):
    chatData = chat_data
    keyboard = types.InlineKeyboardMarkup()
    for i in range(len(buttons_array)):
        keyboard.add(types.InlineKeyboardButton(text=buttons_array[i], callback_data=buttons_array[i]))
    bot.send_message(chatData.chat.id, main_text, reply_markup=keyboard)


@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    if call.message:

        if checkDataFrom(call.data, academic_levels):
            bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
            addTempData(getDataFromButtons(call.data, academic_levels), call.from_user.first_name)
            drawButtons(call.message, faculty_list, "Факультет")

        if checkDataFrom(call.data, faculty_list):
            bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
            addTempData(getDataFromButtons(call.data, faculty_list), call.from_user.first_name)
            drawButtons(call.message, rating_list, "Оценка обучения")

        if checkDataFrom(call.data, rating_list):
            bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
            addTempData(getDataFromButtons(call.data, rating_list), call.from_user.first_name)
            dataTime = datetime.now()
            dataTimeToWrite = dataTime.strftime("%d-%b-%Y (%H:%M:%S.%f)")
            addTempData(dataTimeToWrite, call.from_user.first_name)
            writeData(call.message, all_temp_data[getTempUserDataIndex(call.from_user.first_name)])


def checkDataFrom(data, list):
    if data in list:
        return True
    else:
        return False


def getTempUserDataIndex(name):
    print(len(all_temp_data))
    if len(all_temp_data) == 1:
        return 0
    index = 0
    print(all_temp_data)
    for i in all_temp_data:
        if name in i:
            return index
        index += 1


def addTempData(data, name):
    if len(all_temp_data) == 0:
        all_temp_data.append(data)
    else:
        for i in all_temp_data:
            if name in i:
                i.append(data)


def getDataFromButtons(data, array):
    for i in range(len(array)):
        if data == array[i]:
            return data


@bot.message_handler(content_types=["text"])
def login_new_user(chatData):
    if "/login" in chatData.text:
        if len(chatData.text) > 6:
            tryToLogin(chatData)
        else:
            bot.send_message(chatData.chat.id, bad_registration_text)
    else:
        bot.send_message(chatData.chat.id, bad_command_text + try_again_text)


def tryToLogin(chatData):
    tempID = str(chatData.text)
    tempID = tempID.replace("/login", "").strip()
    if len(tempID) != 6 or tempID[0] != 'u':
        sendMessage(chatData.chat.id, bad_id_text + try_again_text)
    else:
        processLogin(chatData, tempID)


def processLogin(chat_Data, user_id):
    chatData = chat_Data
    userName = chatData.from_user.first_name
    userId = user_id
    if not checkForIdInDataBase(userId):
        all_temp_data.append([userId, userName])
        drawButtons(chatData, academic_levels, "Выберите Ваш уровень")
    else:
        sendMessage(chatData.chat.id, 'Данные уже существуют!')


def writeData(chat_Data, temp_data):
    chatData = chat_Data
    csvFile = open(file_name, 'a', newline='')
    with csvFile:
        fileWriter = csv.writer(csvFile)
        fileWriter.writerow(temp_data)
    sendMessage(chatData.chat.id, f'Данные : \n\nID : {temp_data[0]} \n\n'
                                  f'Имя : {temp_data[1]} \n\n'
                                  f'Уровень : {temp_data[2]} \n\n'
                                  f'факультет : {temp_data[3]} \n\n'
                                  f'Оценка : {temp_data[4]} \n\n'
                                  f'Дата : {temp_data[5]} \n\n'
                                  f'Успешно сохранены!')
    all_temp_data.remove(temp_data)


def checkForIdInDataBase(user_name):
    all_names = []
    with open(file_name, "r") as csv_file:
        users_all_names = csv.reader(csv_file, delimiter=',')
        for current_name in users_all_names:
            all_names.append(current_name[0])
    if user_name in all_names:
        return True
    else:
        return False


bot.polling()
