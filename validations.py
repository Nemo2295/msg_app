from fastapi import HTTPException, status
from user_model import User
from messages_models import Message, ScheduledMessage
from app_storage import AppStorage


def raise_for_if_user_exist(user: User) -> None:
    if user.display_name in AppStorage.USER_STORAGE:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,
                            detail=f"user with display name {user.display_name} is already taken")


def raise_for_if_user_does_not_exist(user_display_name) -> None:
    if user_display_name not in AppStorage.USER_STORAGE:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,
                            detail=f"user with display name {user_display_name} does not exist")


def raise_for_if_user_does_have_messages(user_display_name) -> None:
    if user_display_name not in AppStorage.MESSAGES_STORGE:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,
                            detail=f"user {user_display_name} does not have any messages")


def raise_for_if_message_receiver_does_not_exist(message: [Message, ScheduledMessage]) -> None:
    if message.receiver_display_name not in AppStorage.USER_STORAGE:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,
                            detail=f"The user {message.receiver_display_name} which you are trying to send the message "
                                   f"does not exist")
