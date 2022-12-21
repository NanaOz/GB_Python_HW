import random

import telebot
from config import TOKEN

from glob import glob
from random import choice

bot = telebot.TeleBot(TOKEN)

"""Команда СТАРТ"""


@bot.message_handler(commands=['start'])
def welcome(message):
    markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True,
                                               row_width=2)
    item1 = telebot.types.KeyboardButton('Рандомное число')
    item2 = telebot.types.KeyboardButton('Кинь кубик')
    item3 = telebot.types.KeyboardButton('Милости')
    item4 = telebot.types.KeyboardButton('Как дела?')

    markup.add(item1, item2, item3, item4)

    bot.send_message(message.chat.id,
                     f'{message.from_user.first_name}, Вэлком, что хочешь?)',
                     reply_markup=markup)


@bot.message_handler(content_types=['text'])
def send_text(message):
    if 'привет' in message.text:
        say_hi(message)
    elif message.text == 'Рандомное число':
        random_num(message)
    elif message.text == 'Кинь кубик':
        bot.send_message(message.chat.id,
                         f'Выпало: {str(random.randint(1, 6))}')
    elif message.text == 'Милости':
        send_rand_photo(message)
    elif message.text == 'Как дела?':
        how_are_you(message)
    else:
        bot.send_message(message.chat.id, "че??")


def say_hi(message):
    stiker = open('./stikers/welcome.webp', 'rb')
    bot.send_sticker(message.chat.id, stiker)
    bot.reply_to(message, f'{message.from_user.first_name}, привет!))')


def random_num(message):
    bot.send_message(message.chat.id, str(random.randint(1, 10)))


def send_rand_photo(message):
    lists = glob('./image/*')
    picture = choice(lists)
    bot.send_photo(message.chat.id, open(picture, 'rb'))


def how_are_you(message):
    markup = telebot.types.InlineKeyboardMarkup(row_width=2)

    item1 = telebot.types.InlineKeyboardButton('Хорошо',
                                               callback_data='good')
    item2 = telebot.types.InlineKeyboardButton('Не очень',
                                               callback_data='bad')

    markup.add(item1, item2)

    bot.send_message(message.chat.id, 'Отлично, ты как?',
                     reply_markup=markup)


@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    try:
        if call.message:
            if call.data == 'good':
                stiker = open('./stikers/good.webp', 'rb')
                bot.send_sticker(call.message.chat.id, stiker)
                bot.send_message(call.message.chat.id,
                                 'Я рад, что у тебя все хорошо)')
            elif call.data == 'bad':
                stiker = open('./stikers/baad.webp', 'rb')
                bot.send_sticker(call.message.chat.id, stiker)
                bot.send_message(call.message.chat.id,
                                 'Крепись, скоро все наладится!)')

            bot.edit_message_text(chat_id=call.message.chat.id,
                                  message_id=call.message.message_id,
                                  text='Как дела?', reply_markup=None)
    except Exception as e:
        print(repr(e))


bot.polling(none_stop=True)
