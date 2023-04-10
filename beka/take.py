# Телеграм бот

# python -m venv env

# Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser

# env\Scripts\activate

#id: 5217474025

import telebot
from telebot import types

bot = telebot.TeleBot('6096404180:AAGBa-kLd-bw1XP2MIWaf0ELl7xfMggEPHE')

@bot.message_handler(commands=['start'])
def start_bot(message):

    user = message.from_user.id
    bot.send_message(user, 'Привет мой друг')
    print(user)

@bot.message_handler(commands=['help'])
def startBot(message):
   
    markup = types.InlineKeyboardMarkup()
    # markup - оказывается переменная вроде списка которая хранит в себе кнопки
    button5 = types.InlineKeyboardButton("/text", callback_data='5')

    markup.add(button5)
    print(message.chat.id)
    bot.send_message(message.chat.id, "Привет, {0.first_name}! Нажми на кнопку и перейдите на сайт)".format(message.from_user), reply_markup=markup)

@bot.message_handler(content_types=['text'])
def messagemap(message):
    markup = types.InlineKeyboardMarkup()
    # markup - оказывается переменная вроде списка которая хранит в себе кнопки
    button1 = types.InlineKeyboardButton("Введение в Python", callback_data='0')
    button2 = types.InlineKeyboardButton("ООП", callback_data='1')
    
    markup.add(button1)
    markup.add(button2)


    button3 = types.InlineKeyboardButton("Тест", callback_data='2')
    button4 = types.InlineKeyboardButton("Python", callback_data='3')
    markup.add(button3, button4)
    print(message.chat.id)
    bot.send_message(message.chat.id, "Привет, {0.first_name}! Нажми на кнопку и перейдите на сайт)".format(message.from_user), reply_markup=markup)
    # bot - это библиотека
    # send_message() - это метод из библиотеки
    # первый параметр указатель на чат, у каждой переписки свой id, это уникальная строка в базе данных телеграма
    # второй параметр само сообщение в качестве текстовой информации
    # есть еще другие аргументы, такие как добавление кнопок, добавление ссылок, все можно найти в документации самой библ


# @bot.message_handler(content_types=['text'])
# def messageFunc(message):

#     user = message.from_user.id
#     bott = types.ReplyKeyboardMarkup(resize_keyboard=True)

#     first_bott =  types.KeyboardButton('Виртуальное окружение')
#     second_bott =  types.KeyboardButton('Установка библиотек')

#     bott.add(first_bott, second_bott)

#     if message.text == 'Виртуальное окружение':
#         bot.send_message(user, 'https://kayumov.ru/536', reply_markup=bott)
#     elif message.text == 'Установка библиотек':
#         bot.send_message(user, 'https://skillbox.ru/media/code/kak_ustanovit_biblioteku_v_python', reply_markup=bott)
#     else:
#         bot.send_message(user, 'Выберите действие', reply_markup=bott)



@bot.message_handler(content_types=['text'])
def messageFunc(message):
    markup = types.InlineKeyboardMarkup()
    # markup - оказывается переменная вроде списка которая хранит в себе кнопки
    button1 = types.InlineKeyboardButton("Введение в Python", callback_data='0')
    button2 = types.InlineKeyboardButton("ООП", callback_data='1')
    
    markup.add(button1)
    markup.add(button2)


    #####
    button3 = types.InlineKeyboardButton("Знакомства с Python", callback_data='2')
    button4 = types.InlineKeyboardButton("Тест основы ООП", callback_data='3')
    markup.add(button3, button4)
    #####
    markup.add(button3)
    markup.add(button4)

    bot.send_message(message.chat.id, "Привет, {0.first_name}! Нажми на кнопку и перейди на сайт)".format(message.from_user), reply_markup=markup)
    # bot - это библиотека
    # send_message() - это метод из библиотеки
    # первый параметр указатель на чат, у каждой переписки свой id, это уникальная строка в базе данных телеграма
    # второй параметр само сообщение в качестве текстовой информации
    # есть еще другие аргументы, такие как добавление кнопок, добавление ссылок, все можно найти в документации самой библ


@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call): #функция для кнопок, тут вы перехватываете нажатие кнопок
  try:
    if call.message:
        if call.data == '0':
            bot.send_message(call.message.chat.id, 'Чтоб ознокомится с програмированием нажмите на Python')
        if call.data == '1':
            bot.send_message(call.message.chat.id, 'Тут тест про ООП, Если хотите пройти тeст основы ООП, нажмити на Тест')
        if call.data == '2':
            bot.send_message(call.message.chat.id,'https://pythonist.ru/test-osnovy-oop-v-python/')
        if call.data == '3':
           bot.send_message(call.message.chat.id,'https://younglinux.info/python/course')
        if call.data == '5':
            bot.send_message(call.message.chat.id, 'Введиде /text')
  
  except Exception as e:
    print(repr(e))


bot.polling(none_stop=True)


@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call): #функция для кнопок, тут вы перехватываете нажатие кнопок
  try:
    if call.message:
        if call.data == '5':
            bot.send_message(call.message.chat.id, 'Введиде /text')

  except Exception as e:
    print(repr(e))

