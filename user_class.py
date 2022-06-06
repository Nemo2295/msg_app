from uuid import UUID
from datetime import datetime
from user_model import User


class AppUser:

    def __init__(self, user: User):
        self.user_id: UUID = user.user_id
        self.display_name: str = user.display_name
        self.first_name: str = user.first_name
        self.last_name: str = user.last_name
        self.middle_name: str = user.middle_name
        self.date: datetime = user.date
