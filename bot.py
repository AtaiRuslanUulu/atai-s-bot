import requests
import telegram
from telegram.ext import CommandHandler, MessageHandler, Filters, Updater

# Replace YOUR_TELEGRAM_BOT_TOKEN with your Telegram bot token
bot = telegram.Bot(token='6185358630:AAEaRNRkjg3qrNV5q8JPyyHgowLxAZlg_UE')

# Define the function to handle the /start command
def start(update, context):
    context.bot.send_message(chat_id=update.message.chat_id, text="Welcome to u Integral Calculator! Please enter the function you want to integrate.")

# Define the function to handle text messages
def handle_message(update, context):
    # Get the text message sent by the user
    message_text = update.message.text

    # Make an API request to u to calculate the integral
    url = 'https://www.integral-calculator.com/api/v1/integrate'
    params = {'expression': message_text}
    response = requests.get(url, params=params)

    # Parse the response to get the result
    result = response.json()['result']

    # Send the result to the user as a message
    context.bot.send_message(chat_id=update.message.chat_id, text=result)

# Create the handlers for the /start command and text messages
start_handler = CommandHandler('start', start)
message_handler = MessageHandler(Filters.text & ~Filters.command, handle_message)

# Create the updater and add the handlers
updater = Updater(token='6185358630:AAEaRNRkjg3qrNV5q8JPyyHgowLxAZlg_UE', use_context=True)
dispatcher = updater.dispatcher
dispatcher.add_handler(start_handler)
dispatcher.add_handler(message_handler)

# Start the bot
updater.start_polling()
