import telebot
import main
import random
import memelist

from telebot import types

bot = telebot.TeleBot(main.TOKEN)


OxyList = memelist.OxyList
MemeList = memelist.MemesList
CheList = memelist.CheList

@bot.message_handler(commands = ['start'])
def welcome(message):
    sti = open('static/scum.webp', 'rb')
    bot.send_sticker(message.chat.id, sti)

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton('Скинь мем')

    markup.add(item1)

    bot.send_message(message.chat.id, 'Добро пожаловать, {0.first_name}!\nЯ - <b>{1.first_name}</b>, бот который скидывает мемы\n<b>Что я умею:\nМожешь написать мне <u>"Мем"</u>, или <u>"Скинь мем"</u>\nПостарайся не обзываться <u>лохом</u>, мне обидно\n<u>Оксимирон</u>\nЕсли ты <u>чел</u>, не пиши об этом</b>'.format(message.from_user,bot.get_me()),
    parse_mode='html', reply_markup=markup)

@bot.message_handler(content_types=['text'])
def rofl(message):
    if message.chat.type == 'private':

        if message.text.lower() == 'скинь мем' or message.text.lower() == "мем":

            markdown = types.InlineKeyboardMarkup(row_width=2)
            item3 = types.InlineKeyboardButton('Ещё', callback_data='again')

            markdown.add(item3)

            bot.send_photo(message.chat.id, open(random.choice(MemeList), 'rb' ), reply_markup=markdown)

        elif message.text == 'Ещё' or message.text == 'Еще':

            mark3 = types.InlineKeyboardMarkup(row_width=2)

            item3 = types.InlineKeyboardButton('Ещё', callback_data='again')

            mark3.add(item3)

            bot.send_photo(message.chat.id,open(random.choice(MemeList), 'rb' ), reply_markup=mark3)

        elif message.text.startswith('Ты лох') or message.text == 'Лох':

            markloh = types.InlineKeyboardMarkup(row_width=2)

            itemloh = types.InlineKeyboardButton('Зря быканул', callback_data='again')

            markloh.add(itemloh)

            bot.send_sticker(message.chat.id, open('static/2.webp', 'rb'), reply_markup=markloh)

        elif message.text == 'Оксимирон':

            bot.send_document(message.chat.id, open(random.choice(OxyList), "rb"))

        elif message.text.startswith("Чел") or message.text.startswith("Ты чел"):
            bot.send_sticker(message.chat.id, open('static/3.webp', 'rb'))

            bot.send_message(message.chat.id, random.choice(CheList))

        else:
            bot.send_message(message.chat.id, 'Попробуй попросить мем')

@bot.callback_query_handler(func= lambda call: True)
def call_inline(call):
    try:
        if call.message:
            if call.data == 'again':
                mark4 = types.InlineKeyboardMarkup(row_width=2)

                item3 = types.InlineKeyboardButton('Ещё', callback_data='again')

                mark4.add(item3)

                bot.send_photo(call.message.chat.id, open(random.choice(MemeList), "rb"), reply_markup=mark4)

    except Exception as e:
        print(repr(e))

bot.polling(none_stop=True)