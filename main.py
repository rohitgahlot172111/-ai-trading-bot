import telebot
from config import BOT_TOKEN

bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "👋 Welcome to AI Trading Signals Bot!")

@bot.message_handler(commands=['signal'])
def send_signal(message):
    signal = "📈 BUY EUR/USD\nTimeframe: 1 min\nAccuracy: 91%"
    bot.reply_to(message, signal)

bot.infinity_polling()
