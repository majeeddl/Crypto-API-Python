
import os

bybit_url='https://api.bybit.com'


ENV_DEBUG=os.getenv("DEBUG",True)
ENV_PORT=os.getenv("PORT",5000)
MONGO_URI = os.getenv('MONGO_URI')

class Config:

    TELEGRAM_BOT_TOKEN=''

    @staticmethod
    def telegram_url():
        url = f'https://api.telegram.org/bot{Config.TELEGRAM_BOT_TOKEN}/sendMessage'
        return url