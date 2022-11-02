
# from flask import request
# from flask_restful import Resource
# from frameworks.telegram_services.telergram_service import Telegram

# def parse_message(message):
#     print("message-->",message)
#     chat_id = message['message']['chat']['id']
#     txt = message['message']['text']
#     print("chat_id-->", chat_id)
#     print("txt-->", txt)
#     return chat_id,txt

# class TelegramReource(Resource):

#     def get(self):
#         return "<h1>Welcome!</h1>"


#     def post(self):
#         msg = request.get_json(force=True)

#         print(msg['chat_id'])

#         chat_id = msg['chat_id']

#         Telegram.send_message(chat_id,"Hello, world!")

#         # chat_id,txt = parse_message(msg)

#         # print(txt)

#         return "salam"