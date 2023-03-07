from . import api, decode
from .error import *


def check(data: dict) -> dict | str:

    if "token" not in data:
        return {"exit_code": MISSING_TOKEN, "error_message": "Missing session token! Please login first!"}

    if data["token"] != "12345678":
        return {"exit_code": INVALID_TOKEN, "error_message": "Invalid session token! Please login first!"}

    return data["token"]


@api.post("/login")
def login():

    success, data = decode()
    if not success:
        return data

    if "username" not in data:
        return {"exit_code": MISSING_USERNAME, "error_message": "Missing username!"}
    if "password" not in data:
        return {"exit_code": MISSING_PASSWORD, "error_message": "Missing password!"}

    if data["username"].lower() == "nikocraft" and data["password"] == "1234":

        print(f"New session for '{data['username']}' with token '12345678'.")

        return {"exit_code": 0, "token": "12345678"}

    return {"exit_code": INVALID_USERNAME_OR_PASSWORD, "error_message": "Invalid username or password!"}


@api.post("/logout")
def logout():

    success, data = decode()
    if not success:
        return data

    token = check(data)
    if isinstance(token, dict):
        return token

    print(f"Close session for '{'#TODO'}' with token '{token}'.")

    return {"exit_code": 0}
