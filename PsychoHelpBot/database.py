import sqlite3

# Connect to SQLite database for storing user chat history
conn = sqlite3.connect('user_data.db')
c = conn.cursor()

# Create a table for user chat history if it doesn't already exist
c.execute('''CREATE TABLE IF NOT EXISTS chat_history
             (user_id INTEGER, message TEXT, response TEXT)''')

def log_chat_history(user_id: str, user_message: str, bot_response: str) -> None:
    """Log user messages and bot responses into the chat history."""
    with conn:
        c.execute("INSERT INTO chat_history (user_id, message, response) VALUES (?, ?, ?)",
                  (user_id, user_message, bot_response))

def get_user_history(user_id: str) -> list:
    """Retrieve the chat history for a specific user."""
    history = c.execute("SELECT message, response FROM chat_history WHERE user_id = ?", (user_id,)).fetchall()
    return history
