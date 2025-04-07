# AI Trading Signals Bot 🤖📈

This is a simple Telegram bot built using Python and pyTelegramBotAPI.  
It sends trading signals when specific commands are triggered.

## 🔧 Commands

- `/start` - Welcome message
- `/signal` - Sends a sample trading signal

## 📦 Requirements

Install dependencies using:

```bash
pip install -r requirements.txt
```

## ⚠️ Note

Make sure to add your bot token in a file named `config.py` like this:

```python
BOT_TOKEN = "YOUR_TELEGRAM_BOT_TOKEN"
```

Also, `config.py` is ignored via `.gitignore` so it won’t be uploaded to GitHub.
