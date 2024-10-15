# PsychoHelpBot

PsychoHelpBot is a Telegram bot designed to provide mental health support through interactive conversations. Utilizing advanced Natural Language Processing (NLP) techniques, the bot acts as a virtual psychologist, offering empathetic responses and motivational advice to users.

## Features

- **Conversational Support**: The bot engages users in conversations about their feelings and mental well-being, providing personalized advice and encouragement.
- **Daily Motivation**: Users receive daily motivational messages to help uplift their spirits and keep them focused on their goals.
- **User History**: The bot remembers past conversations to provide contextually relevant responses, creating a more personalized experience.
- **Open-Ended Questions**: The bot encourages dialogue by asking open-ended questions, promoting deeper engagement.

## Technologies Used

- **Python**: The core programming language for the bot.
- **Telegram API**: Used for interacting with users on Telegram.
- **Transformers**: A library from Hugging Face for leveraging state-of-the-art NLP models.
- **SQLite**: Used for storing user chat history and interactions.
- **APScheduler**: A library for scheduling tasks, such as sending daily motivational messages.

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/PsychoHelpBot.git
   cd PsychoHelpBot
   
2. Set up a virtual environment and install the required packages:

  python -m venv .venv
  source .venv/bin/activate  # On Windows use `.venv\Scripts\activate`
  pip install -r requirements.txt

3. Create a .env file in the root directory and add your Telegram bot token:

   TELEGRAM_BOT_TOKEN='YOUR_TELEGRAM_BOT_TOKEN'

4. Run the bot:

  python main.py

  

