import os 
from dotenv import load_dotenv
load_dotenv()

KEY = os.getenv('KEY')
BOT_KEY = os.getenv('BOT_KEY')
DSN = os.getenv('DSN')