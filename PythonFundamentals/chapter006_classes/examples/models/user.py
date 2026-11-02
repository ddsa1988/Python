from uuid import UUID, uuid4

from pydantic import BaseModel, EmailStr


class User(BaseModel):
    id: UUID = uuid4()
    name: str
    email: EmailStr
