import telegram
import os
from dotenv import load_dotenv


load_dotenv()
bot = telegram.Bot(token=os.environ['TG_TOKEN'])
chat_id = 83609395
bot.send_message(text='Hi Tea!', chat_id=chat_id)