from telegram import Update, ChatPermissions
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

TOKEN = "8291076456:AAGvbuurJLboZOwbTiXZc9FjA4j3y5G39Pc"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🤖 بوت الإدارة جاهز للعمل")

async def ban(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.message.reply_to_message:
        user_id = update.message.reply_to_message.from_user.id
        await update.effective_chat.ban_member(user_id)
        await update.message.reply_text("🚫 تم حظر العضو")
    else:
        await update.message.reply_text("❗ رد على رسالة العضو")

async def warn(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.message.reply_to_message:
        await update.message.reply_text("⚠️ تحذير: يرجى احترام قوانين المجموعة")
    else:
        await update.message.reply_text("❗ رد على رسالة العضو")

async def promote(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.message.reply_to_message:
        user_id = update.message.reply_to_message.from_user.id
        await update.effective_chat.promote_member(
            user_id,
            can_manage_chat=True,
            can_delete_messages=True,
            can_restrict_members=True
        )
        await update.message.reply_text("✅ تم رفع العضو مشرف")
    else:
        await update.message.reply_text("❗ رد على رسالة العضو")

async def auto_reply(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text.lower()
    if "مرحبا" in text:
        await update.message.reply_text("👋 مرحبا بك في المجموعة")

app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("ban", ban))
app.add_handler(CommandHandler("warn", warn))
app.add_handler(CommandHandler("promote", promote))
app.add_handler(CommandHandler("help", start))
app.add_handler(CommandHandler("hi", start))
app.add_handler(CommandHandler("test", start))
app.add_handler(CommandHandler("ping", start))

app.run_polling()
