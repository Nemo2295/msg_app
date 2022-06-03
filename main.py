from fastapi import FastAPI, HTTPException, Path
from user_model import User
from messages_models import Message
import data_storage

msg_app = FastAPI()  # uvicorn main:msg_app --reload

users_dict = data_storage.users_dict
messages_dict = data_storage.messages_dict


@msg_app.get("/")
def home_page():
    return "welcome to our messaging app! please register to start enjoying it"


@msg_app.get("/users")
def get_all_users() -> dict:
    return users_dict


@msg_app.post("/users")
def create_user(user: User) -> [str, HTTPException]:
    if user.display_name in users_dict:
        raise HTTPException(status_code=403, detail=f"Sorry display name {user.display_name} is already taken")
    users_dict[user.display_name] = user
    return f"user {user.display_name} registration was successful"


@msg_app.delete("/users/{user_display_name}")
def delete_user_by_display_name(user_display_name: str) -> [str, HTTPException]:
    if user_display_name not in users_dict:
        raise HTTPException(status_code=403, detail=f"user {user_display_name} does not exist")
    users_dict.pop(user_display_name)
    return f"user {user_display_name} deletion was successful"


@msg_app.get("/messages/{user_display_name}/{msg_quantity}")
def get_my_messages(user_display_name: str, msg_quantity: int = Path(None, gt=0)) -> [list[dict], HTTPException]:
    if user_display_name not in users_dict:
        return HTTPException(status_code=403, detail=f"Sorry user {user_display_name} does not exist")
    if user_display_name not in messages_dict:
        return HTTPException(status_code=403, detail=f"Sorry user {user_display_name} does not have any messages")
    if msg_quantity > len(messages_dict[user_display_name]):
        return HTTPException(status_code=403, detail=f"Sorry you have less messages than {msg_quantity}"
                                                     f" please ask for less messages")
    return messages_dict[user_display_name][-msg_quantity:]


@msg_app.post("/messages")
def send_message(message: Message) -> [str, HTTPException]:
    if message.receiver not in users_dict:
        raise HTTPException(status_code=403, detail=f"user {message.receiver} does not exist")
    messages_dict[message.receiver].append({"message id": message.message_id,
                                            "sender": message.sender,
                                            "content": message.content})
    return f"message {message.content} was sent to {message.receiver} successfully"
