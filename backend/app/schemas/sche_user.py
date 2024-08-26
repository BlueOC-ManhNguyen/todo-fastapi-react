from pydantic import BaseModel

from app.helpers.enums import UserRole


class UserResponse(BaseModel):
    id: int
    name: str
    role: UserRole

    class Config:
        from_attributes = True
