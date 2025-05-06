import json
from channels.generic.websocket import AsyncWebsocketConsumer
from channels.db import database_sync_to_async
from django.contrib.auth.models import User
from web_app.models import Company  # Модель для работы с компаниями


class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        # Получаем имя группы из URL
        self.group_name = self.scope['url_route']['kwargs']['group_name']

        # Создаем группу для чата (группа уникальна для каждого чата)
        self.group_name = f'chat_{self.group_name}'

        # Присоединяемся к группе чата
        await self.channel_layer.group_add(
            self.group_name,
            self.channel_name
        )

        # Принимаем WebSocket соединение
        await self.accept()

    async def disconnect(self, close_code):
        # Отключаемся от группы, когда соединение закрывается
        await self.channel_layer.group_discard(
            self.group_name,
            self.channel_name
        )

    async def receive(self, text_data):
        # Получаем сообщение от клиента
        text_data_json = json.loads(text_data)
        message = text_data_json['message']

        # Отправляем сообщение в группу чата
        await self.channel_layer.group_send(
            self.group_name,
            {
                'type': 'chat_message',
                'message': message
            }
        )

    async def chat_message(self, event):
        # Получаем сообщение из события
        message = event['message']

        # Отправляем сообщение клиенту
        await self.send(text_data=json.dumps({
            'message': message
        }))
