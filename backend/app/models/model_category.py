from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship

from app.models.model_base import Base


class Category(Base):
    __tablename__ = "categories"
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    name = Column(String, nullable=False)
    user = relationship("User", foreign_keys=user_id, back_populates="categories")
    tasks = relationship("Task")
