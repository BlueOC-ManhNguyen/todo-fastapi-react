from sqlalchemy import Column, String, Boolean, DateTime

from app.models.model_base import BareBaseModel
from app.helpers.enums import UserRole


class User(BareBaseModel):
    name = Column(String, index=True)
    role = Column(String, default=UserRole.USER)
