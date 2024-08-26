from sqlalchemy import Column, String
from sqlalchemy.orm import relationship

from app.models.model_base import Base


class User(Base):
    __tablename__  = "users"
    name = Column(String, nullable=False)
    email = Column(String, unique=True, index=True)
    password = Column(String(255), nullable=False)
    categories = relationship("Category")