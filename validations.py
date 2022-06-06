from fastapi import HTTPException, status
from user_model import User
from messages_models import Message
from app_storage import users_storage, messages_storage


def check_if_user_exist(user: User) -> [None, HTTPException]:
    if user.display_name in users_storage:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,
                            detail=f"user with display name {user.display_name} is already taken")


def check_if_user_does_not_exist(user_display_name) -> [None, HTTPException]:
    if user_display_name not in users_storage:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,
                            detail=f"user with display name {user_display_name} does not exist")


def check_if_user_has_messages(user_display_name) -> [None, HTTPException]:
    if user_display_name not in messages_storage:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,
                            detail=f"user {user_display_name} does not have any messages")


def check_if_message_receiver_exist(message: Message) -> [None, HTTPException]:
    if message.receiver_display_name not in users_storage:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,
                            detail=f"The user {message.receiver_display_name} which you are trying to send the message "
                                   f"does not exist")
