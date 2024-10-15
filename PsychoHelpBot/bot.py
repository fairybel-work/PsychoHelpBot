import logging
import os
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, CallbackContext
from ai import generate_ai_response
from database import log_chat_history, get_user_history
from scheduler import start_scheduler

# Configure logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

async def start(update: Update, context: CallbackContext) -> None:
    """Send a welcome message when the /start command is issued."""
    await update.message.reply_text("Hi! I'm here to help you with self-care and motivation. How are you feeling today?")

async def handle_message(update: Update, context: CallbackContext) -> None:
    """Handle incoming user messages and generate responses."""
    user_message = update.message.text
    user_id = str(update.message.chat_id)

    # Retrieve user history to provide context
    history = get_user_history(user_id)

    # Format the history for the AI prompt
    user_history = "\n".join([f"User: {msg[0]}\nBot: {msg[1]}" for msg in history]) if history else "No previous history."

    # Generate AI response
    ai_response = generate_ai_response(user_message, user_history)

    # Log user message and response to the database
    log_chat_history(user_id, user_message, ai_response)

    # Reply with the AI-generated response
    await update.message.reply_text(ai_response)

async def start_bot() -> None:
    """Start the Telegram bot and set up message handlers."""
    TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')
    application = ApplicationBuilder().token(TOKEN).build()

    start_scheduler(application.bot)  # Start the scheduler for daily messages

    application.add_handler(CommandHandler("start", start))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    application.add_error_handler(lambda update, context: logger.warning('Update "%s" caused error "%s"', update, context.error))

    await application.initialize()
    await application.run_polling()
