from fastapi import FastAPI, HTTPException, Path
from user_model import User
from messages_models import Message
import data_storage

# to run copy to terminal -> uvicorn main:msg_app --reload
msg_app = FastAPI(title="Nemo messaging app",
                  description="This is an api for registering users and sending messages."
                              "This project is part of Nemo training in **LIBA TEAM**.",
                  version="0.0.1",
                  contact={"name": "nimrod segev", "email": "nimrodsegev10@gmail.com"}
                  )

users_dict = data_storage.users_dict
messages_dict = data_storage.messages_dict


@msg_app.get("/", tags=["Home page"])
async def home_page():
    return "welcome to our messaging app! please register to start enjoying it"


@msg_app.get("/users", tags=["Users"])
async def get_all_users() -> dict:
    return users_dict


@msg_app.post("/users", tags=["Users"])
async def create_user(user: User) -> [str, HTTPException]:
    if user.display_name in users_dict:
        raise HTTPException(status_code=403, detail=f"Sorry display name {user.display_name} is already taken")
    users_dict[user.display_name] = user
    return f"user {user.display_name} registration was successful"


@msg_app.delete("/users/{user_display_name}", tags=["Users"])
async def delete_user_by_display_name(user_display_name: str) -> [str, HTTPException]:
    if user_display_name not in users_dict:
        raise HTTPException(status_code=403, detail=f"user {user_display_name} does not exist")
    users_dict.pop(user_display_name)
    return f"user {user_display_name} deletion was successful"


@msg_app.get("/messages/{user_display_name}/{msg_quantity}", tags=["Messages"])
async def get_my_messages(user_display_name: str = Path(None, description="Enter your display name"),
                          msg_quantity: int = Path(None, gt=0,
                                                   description="Enter the amount of messages you would like to receive"
                                                   )) -> [list[dict], HTTPException]:
    if user_display_name not in users_dict:
        return HTTPException(status_code=403, detail=f"Sorry user {user_display_name} does not exist")
    if user_display_name not in messages_dict:
        return HTTPException(status_code=403, detail=f"Sorry user {user_display_name} does not have any messages")
    if msg_quantity > len(messages_dict[user_display_name]):
        return HTTPException(status_code=403, detail=f"Sorry you have less messages than {msg_quantity}"
                                                     f" please ask for less messages")
    return messages_dict[user_display_name][-msg_quantity:]


@msg_app.post("/messages", tags=["Messages"])
async def send_message(message: Message) -> [str, HTTPException]:
    if message.receiver not in users_dict:
        raise HTTPException(status_code=403, detail=f"user {message.receiver} does not exist")
    messages_dict[message.receiver].append({"message id": message.message_id,
                                            "sender": message.sender,
                                            "content": message.content,
                                            "day": message.date.date(),
                                            "time": message.date.time()
                                            })
    return f"message {message.content} was sent to {message.receiver} successfully"
