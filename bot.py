from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, filters, ContextTypes

import os

TOKEN = os.getenv("TOKEN")

async def handle_submission(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("✅ تم استلام التكليف، شكرًا لإرسالك!")

app = ApplicationBuilder().token(TOKEN).build()
file_handler = MessageHandler(filters.Document.ALL | filters.PHOTO, handle_submission)
app.add_handler(file_handler)

print("البوت يعمل...")
app.run_polling()
