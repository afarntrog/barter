# chat/consumers.py
import json
from channels.generic.websocket import WebsocketConsumer
from asgiref.sync import async_to_sync

class ChatConsumer(WebsocketConsumer):
    def connect(self):
        """
        :at self.room_name Obtains the 'room_name' parameter from the URL route in chat/routing.py that opened the WebSocket connection to the consumer.
                Every consumer has a scope that contains information about ITS OWN connection
        """
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = f'{self.room_name}'

    def disconnect(self, close_code):
        pass

    def receive(self, text_data):
        """
        Parameters
        ----------
        text_data : str
        

        """
        text_data_json = json.loads(text_data)
        message = text_data_json['message']
        print(text_data_json)
        self.send(text_data=json.dumps({
            'message': message
        }))
# https://github.com/narrowfail/django-channels-chat
