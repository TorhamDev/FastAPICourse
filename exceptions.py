from fastapi import HTTPException


class UserNotFound(HTTPException):
    def __init__(self) -> None:
        self.status_code = 522
        self.detail = "user not found!"