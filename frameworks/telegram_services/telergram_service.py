
import requests

from configuration.config import Config


class Telegram:

    @staticmethod
    def send_message(chat_id, text):
        payload = { 'chat_id' : chat_id , 'text': text}
        request = requests.post(Config.telegram_url(),json=payload)

        return request