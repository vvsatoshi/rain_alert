import requests
import os
from dotenv import load_dotenv

def send_tg_message(message):
    load_dotenv()
    bot_token = os.getenv("BOT_TOKEN")
    bot_chatID = os.getenv("BOT_CHAT_ID")
    send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + message

    response = requests.get(send_text)
    return response.json()