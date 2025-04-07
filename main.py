import telebot
import os

# BOT_TOKEN environment se lo
BOT_TOKEN = os.environ.get("BOT_TOKEN")

# Bot initialize karo
bot = telebot.TeleBot(BOT_TOKEN)

# /start command handle
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "👋 Hello bhai! Trading bot ready hai. Signal ke liye tayar ho ja!")

# Bot chalu rakho
bot.polling()
