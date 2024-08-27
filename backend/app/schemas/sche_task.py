from datetime import datetime

from pydantic import BaseModel, ConfigDict


class TaskBase(BaseModel):
    category_id: int
    title: str
    description: str
    status: int
    due_date: datetime


class TaskResponse(TaskBase):
    id: int
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)
