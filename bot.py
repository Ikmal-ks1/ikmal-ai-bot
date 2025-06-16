from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from handlers import chatgpt
import os
from dotenv import load_dotenv

load_dotenv()

app = ApplicationBuilder().token(os.getenv("TELEGRAM_TOKEN")).build()

app.add_handler(CommandHandler("start", chatgpt.start))
app.add_handler(CommandHandler("chat", chatgpt.chat))

app.run_polling()
