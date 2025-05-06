# schemas.py

from pydantic import BaseModel
from typing import Optional
from datetime import date
from models import TaskStatus

class UserBase(BaseModel):
    username: Optional[str] = None
    email: Optional[str] = None

class UserCreate(UserBase):
    username: str
    email: str

class UserUpdate(UserBase):
    pass

class User(UserBase):
    user_id: int

    class Config:
        orm_mode = True

class TaskBase(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    status: Optional[TaskStatus] = None
    due_date: Optional[date] = None

class TaskCreate(TaskBase):
    title: str

class TaskUpdate(TaskBase):
    pass

class Task(TaskBase):
    task_id: int
    user_id: int

    class Config:
        orm_mode = True
