from pydantic import BaseModel


class RegisterInput(BaseModel):
    username: str
    password: str


class UpdateUserProfileInput(BaseModel):
    old_username: str
    new_username: str


class DeleteUserAccountInput(BaseModel):
    username: str
    password: str
