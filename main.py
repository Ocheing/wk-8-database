from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from database import SessionLocal, engine
import models, schemas

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# Root endpoint
@app.get("/")
def read_root():
    return {"message": "Welcome to the Task Manager API"}

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Create a User
@app.post("/users/", response_model=schemas.User)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = models.User(**user.dict())
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

# Get all users
@app.get("/users/", response_model=list[schemas.User])
def read_users(db: Session = Depends(get_db)):
    return db.query(models.User).all()

# Create a Task
@app.post("/tasks/", response_model=schemas.Task)
def create_task(task: schemas.TaskCreate, db: Session = Depends(get_db)):
    db_task = models.Task(**task.dict())
    db.add(db_task)
    db.commit()
    db.refresh(db_task)
    return db_task

# Get all Tasks
@app.get("/tasks/", response_model=list[schemas.Task])
def read_tasks(db: Session = Depends(get_db)):
    return db.query(models.Task).all()
