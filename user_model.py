from pydantic import BaseModel, Field
from typing import Optional
from uuid import UUID, uuid4
from datetime import datetime


class User(BaseModel):
    user_id: Optional[UUID] = Field(default=uuid4(), example="645e9d1f-094b-49c0-9ffa-609b4761b84f")
    display_name: str = Field(example="Nemo2295")
    first_name: str = Field(example="nimrod")
    last_name: str = Field(example="segev")
    middle_name: Optional[str] = Field(default=None, example="shlomo")
    date: datetime = Field(default=datetime.today(), example="2022-06-04T15:27:17.026005")
