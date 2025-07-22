from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

registered_users = set()

async def join(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id

    if user_id not in registered_users:
        registered_users.add(user_id)
        await update.message.reply_text(
            "🎉 Thank you for registering with ICE SUPER!\n\n"
            "👉 To know what we offer, use the command: /services"
        )
    else:
        await update.message.reply_text(
            "👋 You're already registered!\n"
            "Use /services to check what we offer."
        )

async def services(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🧊 Welcome to ICE SUPER 🧊\n"
        "Start Your Own Book Today\n\n"
        "📝 We Provide Services\n"
        "- Whitelabels\n"
        "- Super Masters\n"
        "- Masters\n"
        "🗣️ 24x7 Support Line\n"
        "⚡ Fastest Setup\n\n"
        "Join ICE SUPER and Build, Scale, Dominate"
    )

app = ApplicationBuilder().token("YOUR_BOT_TOKEN").build()

app.add_handler(CommandHandler("join", join))
app.add_handler(CommandHandler("services", services))

app.run_polling()
