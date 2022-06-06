from pydantic import BaseModel, Field
from typing import Optional
from uuid import UUID, uuid4
from datetime import datetime


class User(BaseModel):
    user_id: Optional[UUID] = Field(default=uuid4())
    display_name: str = Field(example="Nemo2295")
    first_name: str = Field(example="nimrod")
    last_name: str = Field(example="segev")
    middle_name: Optional[str] = Field(default=None, example="shlomo")
    date: datetime = Field(default=datetime.today())
