# wk-8-database
# QUESTION 2
## 📝 Task Manager CRUD API
A simple and efficient Task Manager API built with FastAPI, SQLAlchemy, and MySQL. This application supports full CRUD (Create, Read, Update, Delete) operations for managing users and their associated tasks.

## 📋 Table of Contents
Features

Tech Stack

Setup Instructions

API Endpoints

Testing the API

Project Structure



## ✅ Features
User Management: Create, retrieve, update, and delete user profiles.

Task Management: Assign tasks to users with the ability to create, retrieve, update, and delete tasks.

Relational Database: Utilizes MySQL for data storage with SQLAlchemy ORM for database interactions.

Interactive Documentation: Automatically generated Swagger UI for easy API exploration and testing.

## 🛠 Tech Stack
Backend Framework: FastAPI

Database: MySQL

ORM: SQLAlchemy

Data Validation: Pydantic

Server: Uvicorn

## 🚀 Setup Instructions
Prerequisites
- Python 3.7 or higher

- MySQL Server

- pip (Python package installer)

Installation Steps
1. Clone the Repository

bash
Copy
Edit
- git clone https://github.com/Ocheing/wk-8-database.git
- cd task-manager-api
2. Create a Virtual Environment

bash
Copy
Edit
python -m venv venv
3. Activate the Virtual Environment

On Windows:

bash
Copy
Edit
venv\Scripts\activate
On macOS/Linux:

bash
Copy
Edit
source venv/bin/activate
4. Install Dependencies

bash
Copy
Edit
pip install -r requirements.txt
5. Configure the Database

- Ensure MySQL server is running.

- Create a new database:

sql
Copy
Edit
CREATE DATABASE task_manager_db;
- Update the database.py file with your MySQL credentials:

python
Copy
Edit
SQLALCHEMY_DATABASE_URL = "mysql+mysqlconnector://username:password@localhost/task_manager_db"
6. Run the Application

bash
Copy
Edit
uvicorn main:app --reload
The API will be accessible at http://127.0.0.1:8000.

## 📚 API Endpoints
User Endpoints
- POST /users/ : Create a new user.

- GET /users/ : Retrieve all users.

- PUT /users/{user_id} : Update a user's information.

- DELETE /users/{user_id} : Delete a user.

Task Endpoints
- POST /tasks/ : Create a new task.

- GET /tasks/ : Retrieve all tasks.

- PUT /tasks/{task_id} : Update a task's details.

- DELETE /tasks/{task_id} : Delete a task.

## 🧪 Testing the API
##Using Swagger UI
 FastAPI provides an interactive documentation interface:

 1. Navigate to http://127.0.0.1:8000/docs in your browser.

 2. Explore and test each endpoint directly from the interface.



## 📁 Project Structure
pgsql
Copy
Edit
task-manager-api/
├── main.py
├── models.py
├── schemas.py
├── database.py
├── requirements.txt
└── README.md
- main.py : Contains the FastAPI application and route definitions.

- models.py : Defines the SQLAlchemy models for Users and Tasks.

- schemas.py : Contains Pydantic schemas for data validation.

- database.py : Handles the database connection and session management.

- requirements.txt : Lists all Python dependencies.

- README.md : Project documentation.

