users = {}

from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🎰 Welcome to ICE SUPER! Use /join to start.")

async def join(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    user_id = user.id

    if user_id not in users:
        users[user_id] = {
            "name": user.first_name,
            "wallet": 500,  # Initial balance
            "bets": []
        }
        await update.message.reply_text(f"🎉 Hi {user.first_name}, you're now registered! Visit the link for more details:- wa.me/+447777361250!")
    else:
        await update.message.reply_text("👋 You're already registered! Use /wallet to check your balance.")

async def wallet(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id

    if user_id in users:
        balance = users[user_id]["Services"]
        await update.message.reply_text(f""🧊 Welcome to ICE SUPER 🧊\n"
        "Start Your Own Book Today\n\n"
        "📝We Provide Services\n"
        "- Whitelabels\n"
        "- Super Masters\n"
        "- Masters\n"
        "🗣️24x7 Support Line\n"
        "⚡Fastest Setup\n\n"
        "Join ICE SUPER and Build, Scale, Dominate"
    )
    else:
        await update.message.reply_text("❌ You need to /join first.")


async def games(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🎮 Active Games:\n1. 🏏 T20 Match\n2. 🎰 Casino Wheel\n3. 🎲 Dice Roll\n\nUse /bet to place a bet.")


app = ApplicationBuilder().token("7571791230:AAHDXdC_GHLQyU0LoXlnNb1wL1OQi4l4tIw").build()
app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("join", join))
app.add_handler(CommandHandler("games", games))
app.add_handler(CommandHandler("Services", Services))

app.run_polling()
