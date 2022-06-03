from pydantic import BaseModel
from typing import Optional
from uuid import UUID, uuid4


class User(BaseModel):
    user_id: Optional[UUID] = uuid4()
    display_name: str
    first_name: str
    last_name: str
    middle_name: Optional[str] = None
