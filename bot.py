import os
from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes

TOKEN = os.environ.get("8768027310:AAG0kNJAEPKQkLKMMrOeeL31BCd9YE0-uDQ")

if not TOKEN:
    raise Exception("8768027310:AAG0kNJAEPKQkLKMMrOeeL31BCd9YE0-uDQ")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [["Start Bot"]]
    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)

    await update.message.reply_text(
        "Bot is working ✅",
        reply_markup=reply_markup
    )

async def handle(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Working fine 👍")

app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT, handle))

app.run_polling()