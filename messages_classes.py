from datetime import datetime
from pydantic import Field
from uuid import UUID
from messages_models import Message, ScheduledMessage


class AppMessage:
    def __init__(self, message: Message):
        self.message_id: UUID = message.message_id
        self.sender_display_name: str = message.sender_display_name
        self.receiver_display_name: str = message.receiver_display_name
        self.content: str = Field(default=message.content, example="Hello", max_length=300)
        self.date: datetime = Field(default=datetime.today().strftime("%d/%m/%Y %H:%M:%S"))


class AppScheduledMessage(AppMessage):
    def __init__(self, message: Message):
        AppMessage.__init__(self, message)
        self.future_date_to_send: str = ScheduledMessage.future_date_to_send
