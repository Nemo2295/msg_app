from fastapi import FastAPI, HTTPException, Path
from app_storage import users_storage, messages_storage
from user_model import User
from messages_models import Message
from user_class import AppUser
import validations

# to run copy to terminal -> uvicorn main:msg_app --reload
msg_app = FastAPI(title="Nemo messaging app",
                  description="This is an api for registering users and sending messages."
                              "This project is part of Nemo training in **LIBA TEAM**.",
                  version="0.0.1",
                  contact={"name": "nimrod segev", "email": "nimrodsegev10@gmail.com"}
                  )


@msg_app.get("/", tags=["Home page"])
async def home_page() -> dict[str, str]:
    return {"message": "welcome to our messaging app! please register to start enjoying it"}


@msg_app.get("/users", tags=["Users"])
async def get_all_users() -> dict[str, str]:
    return users_storage


@msg_app.post("/users", tags=["Users"])
async def create_user(user: User) -> [dict[str, str], HTTPException]:
    validations.check_if_user_exist(user)
    users_storage[user.display_name] = AppUser(user)
    messages_storage[user.display_name] = []
    return {"message": f"User {user.display_name} registration was successful"}


@msg_app.delete("/users/{user_display_name}", tags=["Users"])
async def delete_user(user_display_name) -> [dict[str, str], HTTPException]:
    validations.check_if_user_does_not_exist(user_display_name)
    users_storage.pop(user_display_name)
    return {"message": f"User {user_display_name} deletion was successful"}


@msg_app.get("/messages/{user_display_name}/{msg_quantity}", tags=["Messages"])
async def get_my_messages(user_display_name, msg_quantity: int = Path(None, gt=0)) -> [list[dict], HTTPException]:
    validations.check_if_user_does_not_exist(user_display_name)
    validations.check_if_user_has_messages(user_display_name)
    return messages_storage[user_display_name][-msg_quantity:]


@msg_app.post("/messages", tags=["Messages"])
async def send_message(message: Message) -> [str, HTTPException]:
    validations.check_if_message_receiver_exist(message)
    messages_storage[message.receiver_display_name].append(message)
    return {"message": f"message {message.content} to {message.receiver_display_name} was sent successfully"}
