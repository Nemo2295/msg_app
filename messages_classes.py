from datetime import datetime
from pydantic import Field
from uuid import UUID
from messages_models import Message


class AppMessage:

    def __init__(self, message: Message):
        self.message_id: UUID = message.message_id
        self.sender_display_name: str = message.sender_display_name
        self.receiver_display_name: str = message.receiver_display_name
        self.content: str = Field(default=message.content, example="Hello", max_length=300)
        self.date: datetime = Field(default=datetime.today())
