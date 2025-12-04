# бот- @Play445Bot


import telebot


TOKEN = '8141515188:AAFeWnlLkJbIIyIE9ie0BwN8-B6rgCQPO00'

bot = telebot.TeleBot(TOKEN)

kb = telebot.types.ReplyKeyboardMarkup(True)
kb.add("Покупка", "Продажа", "Поддержка")

kb2 = telebot.types.ReplyKeyboardMarkup(True)
kb2.add("Отмена")


@bot.message_handler(commands=['start'])  # /start
def start(message):
    print(message.chat.id)  # Посмотреть свой айди
    bot.send_message(message.chat.id, "Привет, это бот по продаже и покупке товаров.\n"
                                      "Выберите действие:\n", reply_markup=kb)


@bot.message_handler(commands=['help'])  # /help
def help(message):
    bot.send_message(message.chat.id, "Чем могу помочь?\n"
                                      "Выберите ниже:\n", reply_markup=kb)


@bot.message_handler(func=lambda message: message.text == "Поддержка")
def support(message):
    bot.send_message(message.chat.id, "Какой возник у вас вопрос?\n"
                                      "Мы отправим его в поддержку\n", reply_markup=kb)


@bot.message_handler(func=lambda message: message.text == "Покупка")
def buy(message):
    bot.send_message(message.chat.id, "Покупка\n"
                                      "Опишите товар, который ищете:\n"
                                      "Название товара\n"
                                      "Желаемая цена\n"
                                      "Дополнительные пожелания\n\n"
                                      "Например: 'Ищу iPhone 15, бюджет до 50000 руб, хорошее состояние'",

                     reply_markup=kb2)


@bot.message_handler(func=lambda message: message.text == "Продажа")
def sale(message):
        bot.send_message(message.chat.id, "Продажа\n"
                                            "Опишите товар, который ищете:\n"
                                            "Название товара\n"
                                            "Цена продажи\n"

                                            "Например: 'Продаю Airpods 4, цена 10 тыс., состояние отличное'\n",

                           reply_markup=kb2)



@bot.message_handler(func=lambda message: message.text == "Отмена")
def cancel(message):
    bot.send_message(message.chat.id,
                     "Действие отменено.\nВыберите новое действие:",
                     reply_markup=kb)


@bot.message_handler(func=lambda message: True)
def echo(message):
    if message.text != "Отмена":
        bot.send_message(message.chat.id,
                         " Хорошо! Ожидайте ответа специалиста.\n"
                         "Спасибо за заявку!",
                         reply_markup=kb)

    else:
        cancel(message)

bot.polling()

