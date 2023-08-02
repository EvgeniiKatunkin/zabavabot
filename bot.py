import config
import content
import telebot

bot = telebot.TeleBot(config.token)


@bot.message_handler(commands=['start', 'help'])
def send_help(message):
    """The handler for /start and /help command"""
    bot.send_message(message.chat.id, 'Привет, ' + message.from_user.first_name +
                     '! Рад тебя видеть! Что бы ты хотел узнать?',
                     reply_markup=config.keyboard(content.main_menu))


@bot.message_handler(content_types=['text'])
def send_text(message):
    """The handler for text messages"""
    message_from_user = message.text.lower()
    if message_from_user == 'где?':
        bot.send_location(message.chat.id, content.location_latitude, content.location_longitude)
    elif message_from_user == 'когда?':
        bot.send_message(message.chat.id, 'Каждую субботу в 20:00, бар Bogart.')
        bot.send_sticker(message.chat.id, content.stickers['when'])
    else:
        bot.send_message(message.chat.id, "Даже не знаю, что на это ответить..."
                                          "Попробуй выбрать команду из меню.")
        bot.send_sticker(message.chat.id, content.stickers['i_dont_know'])


bot.infinity_polling()
