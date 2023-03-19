""" 
Done! Congratulations on your new bot. You will find it at t.me/Intrababot. You can now add a description, about section and profile picture for your bot, see /help for a list of commands. By the way, when you've finished creating your cool bot, ping our Bot Support if you want a better username for it. Just make sure the bot is fully operational before you do this.

Use this token to access the HTTP API:
6028967479:AAEBImzhr2WCR8bopJI177-AdVtMnY0QAlM
Keep your token secure and store it safely, it can be used by anyone to control your bot.

For a description of the Bot API, see this page: https://core.telegram.org/bots/api"""

import telebot,wikipedia,re
from telebot import types
bot = telebot.TeleBot("6028967479:AAEBImzhr2WCR8bopJI177-AdVtMnY0QAlM")

@bot.message_handler(commands=["start"])
def start(m, res=False):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("Button1")
    item2 = types.KeyboardButton("Button2")
    markup.add(item1)
    markup.add(item2)
    bot.send_message(   
        m.chat.id, "Check buttons funtionality")


@bot.message_handler(content_types=["text"])
def handle_text(message):
    if message.text.strip() == "Button1":
        answer = "вы нажали кнопку 1"
    if message.text.strip() == "Button2":
        answer = "Кнопка 2"
    bot.send_message(message.chat.id, answer)


bot.polling(non_stop=True, interval=0)