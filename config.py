import os
import telebot
from dotenv import load_dotenv

# Token of the bot in telegram
load_dotenv()
token = os.getenv('BOT_TOKEN')


def keyboard(buttons: str) -> 'Keyboard':
    """It's the keyboard which appears for /start and /help commands"""
    current_keyboard = telebot.types.ReplyKeyboardMarkup(True)
    for button in buttons:
        current_keyboard.add(button)
    return current_keyboard
