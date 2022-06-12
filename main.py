from fastapi import FastAPI, Path
from user_model import User
from messages_models import Message, ScheduledMessage
from user_class import AppUser
from typing import Dict
from timing_functions import calculate_seconds_to_send_message
import validations
import app_storage

msg_app = FastAPI(title="Nemo messaging app",
                  description="This is an api for registering users and sending messages."
                              "This project is part of Nemo training in **LIBA TEAM**.",
                  version="0.0.1",
                  contact={"name": "nimrod segev", "email": "nimrodsegev10@gmail.com"}
                  )


@msg_app.get("/", tags=["Home page"])
async def home_page() -> Dict[str, str]:
    return {"message": "welcome to our messaging app! please register to start enjoying it"}


@msg_app.get("/users", tags=["Users"])
async def get_all_users() -> Dict[str, str]:
    return app_storage.users_storage


@msg_app.post("/users", tags=["Users"])
async def create_user(user: User) -> Dict[str, str]:
    validations.raise_for_if_user_exist(user)
    app_storage.users_storage[user.display_name] = AppUser(user)
    app_storage.messages_storage[user.display_name] = []
    app_storage.scheduled_messages_storage[user.display_name] = []
    return {"message": f"User {user.display_name} registration was successful"}


@msg_app.delete("/users/{user_display_name}", tags=["Users"])
async def delete_user(user_display_name) -> Dict[str, str]:
    validations.raise_for_if_user_does_not_exist(user_display_name)
    app_storage.users_storage.pop(user_display_name)
    return {"message": f"User {user_display_name} deletion was successful"}


@msg_app.get("/messages/{user_display_name}/{msg_quantity}", tags=["Messages"])
async def get_my_messages(user_display_name, msg_quantity: int = Path(None, gt=0)) -> [list[dict]]:
    validations.raise_for_if_user_does_not_exist(user_display_name)
    validations.raise_for_if_user_has_messages(user_display_name)
    return app_storage.messages_storage[user_display_name][-msg_quantity:]


@msg_app.post("/messages", tags=["Messages"])
async def send_message(message: Message) -> Dict[str, str]:
    validations.raise_for_if_message_receiver_does_not_exist(message)
    app_storage.messages_storage[message.receiver_display_name].append(message)
    return {"message": f"message {message.content} to {message.receiver_display_name} was sent successfully"}


@msg_app.post("/messages/scheduled", tags=["Scheduled Messages"])
async def send_message(scheduled_message: ScheduledMessage) -> Dict[str, str]:
    validations.raise_for_if_message_receiver_does_not_exist(scheduled_message)
    seconds_to_send_message = calculate_seconds_to_send_message(scheduled_message.future_date_to_send)
    app_storage.scheduled_messages_storage[scheduled_message.receiver_display_name].append(
        (scheduled_message, int(seconds_to_send_message)))
    return {"message": f"message {scheduled_message.content} to {scheduled_message.receiver_display_name}"
                       f" was accepted successfully, and will be sent at {scheduled_message.future_date_to_send}"}


@msg_app.get("/messages/scheduled/{user_display_name}/{msg_quantity}", tags=["Scheduled Messages"])
async def get_my_messages(user_display_name, msg_quantity: int = Path(None, gt=0)) -> [list[dict]]:
    validations.raise_for_if_user_does_not_exist(user_display_name)
    validations.raise_for_if_user_has_messages(user_display_name)
    return app_storage.scheduled_messages_storage[user_display_name][-msg_quantity:]
