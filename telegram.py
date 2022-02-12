import requests
from config import *

def telegram_bot(message):
    send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + message
    response = requests.get(send_text)
    return response.json()


#print(telegram_bot("HI"))