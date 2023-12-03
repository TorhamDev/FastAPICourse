from pydantic import BaseModel


class UserInput(BaseModel):
    username: str
    password: str


class UpdateUserProfileInput(BaseModel):
    old_username: str
    new_username: str


class DeleteUserAccountInput(BaseModel):
    username: str
    password: str
