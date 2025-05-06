from sqlalchemy import Column, Integer, String, Text, Date, Enum, ForeignKey, TIMESTAMP, func
from sqlalchemy.orm import relationship
from database import Base
import enum

class TaskStatus(str, enum.Enum):
    pending = "pending"
    in_progress = "in_progress"
    completed = "completed"

class User(Base):
    __tablename__ = "users"
    user_id = Column(Integer, primary_key=True, index=True)
    username = Column(String(50), unique=True, nullable=False)
    email = Column(String(100), unique=True, nullable=False)

    tasks = relationship("Task", back_populates="user")

class Task(Base):
    __tablename__ = "tasks"
    task_id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.user_id"))
    title = Column(String(255), nullable=False)
    description = Column(Text)
    status = Column(Enum(TaskStatus), default=TaskStatus.pending)
    due_date = Column(Date)
    created_at = Column(TIMESTAMP, server_default=func.now())

    user = relationship("User", back_populates="tasks")
