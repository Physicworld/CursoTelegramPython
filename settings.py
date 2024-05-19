import os
from dotenv import load_dotenv

load_dotenv()

TELEGRAM_BOT_TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')
STRIPE_TEST_TOKEN = os.getenv('STRIPE_TEST_TOKEN')
