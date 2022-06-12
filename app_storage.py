from user_model import User
from user_class import AppUser
from messages_models import Message, ScheduledMessage
from timing_functions import calculate_seconds_to_send_message
from typing import Dict, List


class AppStorage:

    USER_STORAGE = {}
    MESSAGES_STORGE = {}
    SCHEDULED_MESSAGES_STORGE = {}

    @staticmethod
    def create_user_in_user_storage(user: User) -> None:
        AppStorage.USER_STORAGE[user.display_name] = AppUser(user)

    @staticmethod
    def create_user_in_messages_storage(user: User) -> None:
        AppStorage.MESSAGES_STORGE[user.display_name] = []

    @staticmethod
    def create_user_in_scheduled_messages_storage(user: User) -> None:
        AppStorage.SCHEDULED_MESSAGES_STORGE[user.display_name] = []

    @staticmethod
    def delete_user_in_user_storage(user_display_name: str) -> None:
        AppStorage.USER_STORAGE.pop(user_display_name)

    @staticmethod
    def delete_user_in_messages_storage(user_display_name: str) -> None:
        AppStorage.MESSAGES_STORGE.pop(user_display_name)

    @staticmethod
    def delete_user_in_scheduled_messages_storage(user_display_name: str) -> None:
        AppStorage.SCHEDULED_MESSAGES_STORGE.pop(user_display_name)

    @staticmethod
    def retrieve_user_messages(user_display_name: str, msg_quantity: int) -> List[Dict]:
        return AppStorage.MESSAGES_STORGE[user_display_name][-msg_quantity:]

    @staticmethod
    def add_message_to_messages_storage(message: Message) -> None:
        AppStorage.MESSAGES_STORGE[message.receiver_display_name].append(message)

    @staticmethod
    def add_message_to_scheduled_messages_storage(scheduled_message: ScheduledMessage) -> None:
        seconds_to_send_message = calculate_seconds_to_send_message(scheduled_message.future_date_to_send)
        AppStorage.SCHEDULED_MESSAGES_STORGE[scheduled_message.receiver_display_name].append(
            (scheduled_message, int(seconds_to_send_message)))

    @staticmethod
    def retrieve_user_scheduled_messages(user_display_name: str, msg_quantity: int) -> List[Dict]:
        return AppStorage.SCHEDULED_MESSAGES_STORGE[user_display_name][-msg_quantity:]
