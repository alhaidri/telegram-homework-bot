from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, filters, ContextTypes
import os

TOKEN = os.getenv("TOKEN")
ADMIN_CHAT_ID = 4921177021

async def handle_submission(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # إرسال رسالة شكر للطالب
    await update.message.reply_text("✅ تم استلام التكليف، شكرًا لإرسالك!")

    # إعادة توجيه الملف إلى المشرف
    await context.bot.forward_message(
        chat_id=ADMIN_CHAT_ID,
        from_chat_id=update.message.chat_id,
        message_id=update.message.message_id
    )

app = ApplicationBuilder().token(TOKEN).build()
file_handler = MessageHandler(filters.Document.ALL | filters.PHOTO, handle_submission)
app.add_handler(file_handler)

print("البوت يعمل...")
app.run_polling()
