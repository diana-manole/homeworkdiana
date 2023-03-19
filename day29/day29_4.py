""" 
Done! Congratulations on your new bot. You will find it at t.me/Intrababot. You can now add a description, about section and profile picture for your bot, see /help for a list of commands. By the way, when you've finished creating your cool bot, ping our Bot Support if you want a better username for it. Just make sure the bot is fully operational before you do this.

Use this token to access the HTTP API:
6028967479:AAEBImzhr2WCR8bopJI177-AdVtMnY0QAlM
Keep your token secure and store it safely, it can be used by anyone to control your bot.

For a description of the Bot API, see this page: https://core.telegram.org/bots/api """


import telebot
import os

bot = telebot.TeleBot("6028967479:AAEBImzhr2WCR8bopJI177-AdVtMnY0QAlM")
mas=[]
if os.path.exists("brain.txt"):
    f= open("brain.txt","r",encoding="UTF-8")
    for x in f :
        if( len(x.strip())>2):
                 mas.append(x.strip().lower())
        
     
@bot.message_handler(commands=["start"])
def start(m, res=False):
    bot.send_message(m.chat.id, "Lets talk")

@bot.message_handler(content_types=["text"])
def handle_text(message):
    print(message.chat.id)

    bot.send_message(message.chat.id, f"Your text: {message.text}" )

bot.polling(non_stop=True, interval=0)