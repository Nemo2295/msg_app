from pydantic import BaseModel
from typing import Optional
from uuid import UUID, uuid4


class Message(BaseModel):
    message_id: UUID = uuid4()
    sender: str
    receiver: str
    content: str


class Scheduled_message(BaseModel):
    message_id: UUID = uuid4()
    sender: str
    receiver: str
    content: str
    sec_to_send: Optional[int] = 0
    min_to_send: Optional[int] = 0
    hrs_to_send: Optional[int] = 0
    days_to_send: Optional[int] = 0
