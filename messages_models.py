from datetime import datetime
from pydantic import BaseModel, Field
from uuid import UUID, uuid4


class Message(BaseModel):
    message_id: UUID = Field(default=uuid4())
    sender_display_name: str = Field(example="Noam99")
    receiver_display_name: str = Field(example="Nemo2295")
    content: str = Field(default=None, example="Hello", max_length=300)
    date: datetime = Field(default=datetime.today())


class ScheduledMessage(BaseModel):
    message_id: UUID = Field(default=uuid4())
    sender_display_name: str = Field(example="Noam99")
    receiver_display_name: str = Field(example="Nemo2295")
    content: str = Field(default=None, example="Future Hello", max_length=300)
    future_date_to_send: str = Field(example="12/06/2022 12:45:00")
