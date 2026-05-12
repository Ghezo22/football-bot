from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes

epl_tips = """
🏴 EPL TIPS 🏴

1. Arsenal vs Chelsea → Over 1.5 Goals
2. Liverpool vs Spurs → BTTS
   """

laliga_tips = """
🇪🇸 LA LIGA TIPS 🇪🇸

1. Real Madrid vs Valencia → Real Madrid Win
2. Barcelona vs Sevilla → Barcelona Win
   """

ucl_tips = """
🏆 UCL TIPS 🏆

1. PSG vs Bayern → BTTS
2. Inter vs Dortmund → Draw or BTTS
   """

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):

keyboard = [
    ["🏴 EPL Tips"],
    ["🇪🇸 La Liga Tips"],
    ["🏆 UCL Tips"]
]

reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)

await update.message.reply_text(
    "⚽ Welcome to Sure Tips Bot",
    reply_markup=reply_markup
)

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):

text = update.message.text

if text == "🏴 EPL Tips":
    await update.message.reply_text(epl_tips)

elif text == "🇪🇸 La Liga Tips":
    await update.message.reply_text(laliga_tips)

elif text == "🏆 UCL Tips":
    await update.message.reply_text(ucl_tips)

else:
    await update.message.reply_text("Use the buttons ⚽")

app = ApplicationBuilder().token("8768027310:AAG0kNJAEPKQkLKMMrOeeL31BCd9YE0-uDQ").build()

app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT, handle_message))

app.run_polling()