from telegram import Update
from telegram.ext import ContextTypes
from utils.openai_utils import ask_gpt

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    with open("avatar.png", "rb") as avatar:
        await update.message.reply_photo(photo=avatar, caption="Halo, saya *Ikmal AI Bot*! Ketik /chat diikuti pertanyaanmu.")

async def chat(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = " ".join(context.args)
    if not query:
        await update.message.reply_text("Ketik pertanyaan setelah /chat.")
        return
    response = ask_gpt(query)
    with open("avatar.png", "rb") as avatar:
        await update.message.reply_photo(photo=avatar, caption=response)
