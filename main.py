from typing import Final
from telegram import Update
from telegram.ext import Application , CommandHandler, MessageHandler, filters, ContextTypes

TOKEN: Final = "7246133680:AAE4B-mwxO-f8kKo-YJ3oW9g2Nad1cMyZYQ"
BOT_USERNAME: Final = '@my1_hello2_world3_bot'

async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hello! Thanks for chatting with me! I am Ezer")

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("I am Ezer! please type something so I can respond!")

async def custom_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
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

async def handel_message(update: Update, ContextTypes.DEFAULT_TYPE):
    massage_type: str = update.message.chat.type
    text: str = update.message.text

    print(f'User ({update.message.chat.id}) in {message_type}: "{text}"')
    if message_type == "group":
        if BOT_USERNAME in text:
            new_text: str = text.replace(BOT_USERNAME, '').strip()
            response: str = handel_response(new_text)
        else:
            return
    else:
        response: str = handle_response(text)

    print('Bot:', response)
    await update.message.reply_text(response)

async def error(update: Update, ContextTypes.DEFAULT_TYPE):
    print(f'Update {update} caused error {context.error}')

if __name__ == "__main__":
    print("Starting bot...")
    app = Application.builder().token(TOKEN).build()
    # Commands
    app.add_handler(CommandHandler("start", start_command))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(CommandHandler("custom", custom_command))
    # Messages
    app.add_handler(MessageHandler(filters.TEXT, handel_message))
    # Errors
    app.add_error_handler(error)
    # Polls the bot
    print("polling...")
    app.run_polling(poll_interval=3)

