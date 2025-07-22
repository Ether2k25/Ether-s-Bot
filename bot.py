import os

from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

users = {}
BOT_TOKEN = os.getenv("BOT_TOKEN")
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🎰 Welcome to ICE SUPER! Use /games or /join to start.")

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
        balance = users[user_id]["wallet"]
        await update.message.reply_text(f"💰 Your current wallet balance: ₹{balance}")
    else:
        await update.message.reply_text("❌ You need to /join first.")


async def games(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🎮 Active Games:\n1. 🏏 T20 Match\n2. 🎰 Casino Wheel\n3. 🎲 Dice Roll\n\nUse /bet to place a bet.")


app = ApplicationBuilder().token(BOT_TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("join", join))
app.add_handler(CommandHandler("games", games))
app.add_handler(CommandHandler("wallet", wallet))

app.run_polling()
