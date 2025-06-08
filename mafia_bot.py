import os
import random
import logging
from typing import Dict

from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class MafiaGame:
    def __init__(self):
        self.players: Dict[int, str] = {}
        self.mafia: int | None = None
        self.started: bool = False

    def reset(self) -> None:
        self.players.clear()
        self.mafia = None
        self.started = False

game = MafiaGame()

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Handle /start command."""
    await update.message.reply_text(
        "Привет! Используй /join чтобы вступить в игру. Когда все собрались, отправь /startgame."
    )

async def join(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user_id = update.effective_user.id
    if user_id not in game.players:
        game.players[user_id] = update.effective_user.full_name
        await update.message.reply_text(f"{update.effective_user.full_name} присоединился к игре!")
    else:
        await update.message.reply_text("Вы уже в игре!")

async def start_game(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    if game.started:
        await update.message.reply_text("Игра уже началась!")
        return

    if len(game.players) < 3:
        await update.message.reply_text("Нужно минимум 3 игрока для начала игры.")
        return

    game.started = True
    game.mafia = random.choice(list(game.players.keys()))

    for pid, name in game.players.items():
        text = (
            "Вы мафия! Уничтожьте мирных." if pid == game.mafia else "Вы мирный житель. Найдите мафию!"
        )
        await context.bot.send_message(chat_id=pid, text=text)

    await update.message.reply_text("Игра началась! Роли разосланы в личку.")

async def reset_game(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    game.reset()
    await update.message.reply_text("Игра сброшена. Используйте /join чтобы начать заново.")

def main() -> None:
    token = os.getenv("TELEGRAM_TOKEN")
    if not token:
        import sys
        if len(sys.argv) < 2:
            print("Usage: python mafia_bot.py <TOKEN>")
            return
        token = sys.argv[1]

    application = ApplicationBuilder().token(token).build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("join", join))
    application.add_handler(CommandHandler("startgame", start_game))
    application.add_handler(CommandHandler("resetgame", reset_game))

    logger.info("Bot started")
    application.run_polling()

if __name__ == "__main__":
    main()
