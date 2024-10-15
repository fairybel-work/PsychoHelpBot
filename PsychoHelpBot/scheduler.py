import asyncio
from apscheduler.schedulers.background import BackgroundScheduler
import pytz
from database import get_user_history

async def send_daily_motivation(bot) -> None:
    """Send daily motivational messages to all users."""
    users = get_user_history()  # Assuming this returns a list of user IDs
    for user in users:
        await bot.send_message(chat_id=user[0], text="Here's your daily dose of motivation! Keep pushing forward!")

def start_scheduler(bot) -> None:
    """Start a scheduler for sending daily motivational messages."""
    scheduler = BackgroundScheduler(timezone=pytz.UTC)
    scheduler.add_job(lambda: asyncio.run(send_daily_motivation(bot)), 'interval', days=1)
    scheduler.start()
