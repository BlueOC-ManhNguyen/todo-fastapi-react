from sqlalchemy import Column, String, Integer, ForeignKey, DateTime
from sqlalchemy.orm import relationship

from app.models.model_base import Base


class Task(Base):
    __tablename__ = "tasks"
    category_id = Column(Integer, ForeignKey('categories.id'), nullable=False)
    title = Column(String, nullable=False)
    description = Column(String, default='')
    status = Column(Integer, default=0)
    due_date = Column(DateTime, nullable=False)
    category = relationship("Category", foreign_keys=category_id, back_populates="tasks")