import telebot
import os

# Bot token from environment variable
BOT_TOKEN = os.environ.get("BOT_TOKEN")

# Create bot instance
bot = telebot.TeleBot(BOT_TOKEN)

# Command handler for /start
@bot.message_handler(commands=['start'])
def handle_start(message):
    bot.reply_to(message, "👋 Hello! AI Trading Bot is running!")

# Example handler for a text message
@bot.message_handler(func=lambda m: True)
def handle_all_messages(message):
    bot.reply_to(message, "📈 I'm your AI Trading assistant. Type /start to begin.")

# Start the bot (safe method for Render)
if __name__ == "__main__":
    print("🤖 Bot is polling...")
    bot.infinity_polling(timeout=10, long_polling_timeout=5)
