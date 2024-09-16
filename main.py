from typing import Final
from telegram import Update
from telegram.ext import Application , CommandHandler, MessageHandler, filters, ContextTyples

TOKEN: Final = "7246133680:AAE4B-mwxO-f8kKo-YJ3oW9g2Nad1cMyZYQ"
BOT_USERNAME: Final = '@my1_hello2_world3_bot'

async def start_command(update: Update, context: ContextTyples.DEFAULT_TYPE):
    await update.message.reply_text("Hello! Thanks for chatting with me! I am Ezer")

async def help_command(update: Update, context: ContextTyples.DEFAULT_TYPE):
    await update.message.reply_text("I am Ezer! please type something so I can respond!")

async def custom_command(update: Update, context: ContextTyples.DEFAULT_TYPE):
    await update.message.reply_text("This is a custom command!")

# Responses
def handel_response(text:str) -> str:
    processed : str = text.lower()
    if "Hello" in processed:
        return "Hey there!"
    if "How are you" in processed:
        return "I am good!"
    if "I love python" in processed:
        return "Remember to subscribe!"
    return "I don't understand what you wrote.."