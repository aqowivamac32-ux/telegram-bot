import telebot
import os

TOKEN = os.environ.get("8550949680:AAEeooHvf8ETT4PV9yLc9LVoterv3gZeVdY")
OWNER_ID = 7789017726

bot = telebot.TeleBot(8550949680:AAEeooHvf8ETT4PV9yLc9LVoterv3gZeVdY)

@bot.message_handler(func=lambda message: True)
def forward_to_owner(message):
    if message.from_user.id != OWNER_ID:
        bot.forward_message(OWNER_ID, message.chat.id, message.message_id)

@bot.message_handler(func=lambda message: message.reply_to_message is not None)
def reply_from_owner(message):
    if message.from_user.id == OWNER_ID:
        if message.reply_to_message.forward_from:
            original_user = message.reply_to_message.forward_from.id
            bot.send_message(original_user, message.text)

bot.polling()
