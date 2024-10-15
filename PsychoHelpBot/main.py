import asyncio
import logging
import nest_asyncio
from dotenv import load_dotenv
from bot import start_bot

# Configure logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

# Apply nest_asyncio to allow nested event loops
nest_asyncio.apply()

if __name__ == "__main__":
    load_dotenv()  # Load environment variables
    try:
        asyncio.run(start_bot())  # Start the bot
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
