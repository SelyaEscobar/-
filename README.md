# Telegram Mafia Bot

This repository provides a simple Telegram bot for playing a lightweight version of the Mafia game. It uses the `python-telegram-bot` library.

## Setup

1. Create a new bot with [BotFather](https://t.me/botfather) and obtain the API token.
2. Install the dependency:

   ```bash
   pip install python-telegram-bot
   ```
3. Run the bot, providing the token via argument or the `TELEGRAM_TOKEN` environment variable:

   ```bash
   python mafia_bot.py <TOKEN>
   # or set TELEGRAM_TOKEN and run:
   python mafia_bot.py
   ```

## Gameplay

1. Invite the bot to your group chat.
2. Players send `/join` to enter the lobby.
3. When everyone is ready, send `/startgame` to randomly assign roles. Each player will receive their role in a private message.
4. Use `/resetgame` to clear the current game and start over.

This is a minimal example to help you get started. You can extend it with full voting mechanics and day/night cycles as you learn more about Python and Telegram bots.
