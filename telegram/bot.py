# Телеграм бот

# python -m venv env

# Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser

# env\Scripts\activate


import telebot
from telebot import types


bot = telebot.TeleBot('6219431018:AAHKLoMbpEIgEP2h5aVhpA_TVNOHrURkD1w')

@bot.message_handler(commands=['start'])
def startBot(message):
    user = message.from_user.id

    bot.send_message(user, 'Привет Господин!')


@bot.message_handler(commands=['help'])
def startBot(message):
    user = message.from_user.id
    
    bot.send_message(user, 'Чем могу помочь')

@bot.message_handler(content_types=['text'])
def messageFunc(message):
    markup = types.InlineKeyboardMarkup()
    # markup - оказывается переменная вроде списка которая хранит в себе кнопки
    button1 = types.InlineKeyboardButton("Введение в Python", callback_data='0')
    button2 = types.InlineKeyboardButton("ООП", callback_data='1')
    
    markup.add(button1)
    markup.add(button2)


    button3 = types.InlineKeyboardButton("Тест", callback_data='2')
    button4 = types.InlineKeyboardButton("В ряд", callback_data='3')
    markup.add(button3, button4)
    print(message.chat.id)
    bot.send_message(message.chat.id, "Привет, {0.first_name}! Нажми на кнопку и перейдите на сайт)".format(message.from_user), reply_markup=markup)
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
        bot.send_message(call.message.chat.id, 'Тут текст про ооп')
      if call.data == '1':
        bot.send_message(call.message.chat.id, 'Тут текст про введение в python')
 

  except Exception as e:
    print(repr(e))



bot.polling(none_stop=True)
