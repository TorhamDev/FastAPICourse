from uuid import UUID

from pydantic import BaseModel


class RegisterOutput(BaseModel):
    username: str
    id: UUID
