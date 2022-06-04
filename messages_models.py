from datetime import datetime
from pydantic import BaseModel, Field
from typing import Optional
from uuid import UUID, uuid4


class Message(BaseModel):
    message_id: UUID = Field(default=uuid4(), example="93b2dad3-1d19-4563-bd6f-7b8c609a1464")
    sender: str = Field(example="Noam99")
    receiver: str = Field(example="Nemo2295")
    content: str = Field(default=None, example="Hello", max_length=300)
    date: datetime = Field(default=datetime.today())


class Scheduled_message(BaseModel):
    message_id: UUID = Field(default=uuid4(), example="93b2dad3-1d19-4563-bd6f-7b8c609a1464")
    sender: str = Field(example="Noam99")
    receiver: str = Field(example="Nemo2295")
    content: str = Field(default=None, example="Hello", max_length=300)
    sec_to_send: Optional[int] = 0
    min_to_send: Optional[int] = 0
    hrs_to_send: Optional[int] = 0
    days_to_send: Optional[int] = 0
