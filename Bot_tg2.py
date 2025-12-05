#бот - @Trueger33Bot



import telebot




TOKEN = '8271783402:AAE9N0EpVZn-L_C3Q4eSDrZeMqLDBRopQ2k'

bot = telebot.TeleBot(TOKEN)
PIN = "1234"
balance = 1000
history = []
attempts = 3

kb = telebot.types.ReplyKeyboardMarkup(True, row_width=2)
kb.add("Проверить баланс", "Снять деньги", "Пополнить счет", "История операций")



@bot.message_handler(commands=['start'])
def start(message):
    print(message.chat.id)
    msg = bot.send_message(message.chat.id, "БАНКОМАТ\nВведите пин-код:"
                                            "\nосталось 3 попытки ",
                                            reply_markup=telebot.types.ReplyKeyboardRemove())
    bot.register_next_step_handler(msg, check_pin, attempts_left=attempts)

def check_pin(message, attempts_left):
    if message.text == PIN and message.text.isdigit():
        bot.send_message(message.chat.id, "Вы успешно вошли в систему!", reply_markup=kb)
    else:
        attempts_left -= 1
        if attempts_left > 0:
            msg = bot.send_message(message.chat.id,
                            f"Неверный PIN-код! Осталось попыток: {attempts_left}\nПопробуйте еще раз:")
            bot.register_next_step_handler(msg, check_pin, attempts_left=attempts_left)
        else:
            bot.send_message(message.chat.id, "Превышено количество попыток. Доступ заблокирован.")


@bot.message_handler(func=lambda message: True)
def handle_menu(message):
    if message.text == "Проверить баланс":
        bot.send_message(message.chat.id, f"Баланс: {balance} руб")

    elif message.text == "Снять деньги":
        msg = bot.send_message(message.chat.id, "Сколько рублей вы хотите снять?",
                         reply_markup=telebot.types.ReplyKeyboardRemove())
        bot.register_next_step_handler(msg, take_money)

    elif message.text == "Пополнить счет":
        msg = bot.send_message(message.chat.id, "Сколько рублей вы хотите пополнить?",
                         reply_markup=telebot.types.ReplyKeyboardRemove())
        bot.register_next_step_handler(msg, add_money)

    elif message.text == "История операций":
        global history
        if history:
            hist_text = "\n".join(history[-3:])
            bot.send_message(message.chat.id, f"История:\n{hist_text}")
        else:
            bot.send_message(message.chat.id, "История пуста")



def take_money(message):
    global balance, history
    amount = float(message.text)
    if amount <= balance:
        balance -= amount
        history.append(f"Снято: {amount} руб.")
        bot.send_message(message.chat.id, f"Снято {amount} руб.", reply_markup=kb)
    else:
        bot.send_message(message.chat.id, f"Не хватает денег!\nНа счете только {balance} руб.",
                         reply_markup=kb)



def add_money(message):
    global balance, history
    amount = float(message.text)
    if amount > 0:
        balance += amount
        history.append(f"Пополнено: {amount} руб.")
        bot.send_message(message.chat.id,f"Пополнено: {amount} руб.", reply_markup=kb)
    if amount <= 0:
        bot.send_message(message.chat.id,"Неверное введены данные!",reply_markup=kb)




bot.polling()






















