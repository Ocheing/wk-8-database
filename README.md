# wk-8-database
#QUESTION ONE ASSIGNMENT
# 📦 Inventory Tracking System
## 📝 Overview
This project is a MySQL-based Inventory Tracking System designed to manage and monitor inventory levels across various categories, locations, and suppliers. It facilitates efficient tracking of products, their movements, and associated personnel.

## 🎯 Objectives
- Design a well-structured relational database using MySQL.

- Implement tables with appropriate constraints: PRIMARY KEY, FOREIGN KEY, NOT NULL, and UNIQUE.

- Establish relationships:

1. One-to-One (1:1)

2. One-to-Many (1:M)

3.Many-to-Many (M:N)

- Populate tables with sample data to demonstrate functionality.

## 🗄️ Database Schema
The database comprises the following tables:

- category: Stores product categories.

- employee: Contains employee details responsible for inventory transactions.

- inventory_transaction: Logs all inventory movements (IN/OUT).

- location: Details of storage locations.

- product: Information about products in inventory.

- product_supplier: Associates products with their suppliers (M:N relationship).

- supplier: Supplier contact information.

## 🔑 Table Relationships
- Each product belongs to one category and is stored in one location.

- Each inventory_transaction is linked to one product and may involve one employee.

- The product_supplier table establishes a many-to-many relationship between products and suppliers.

## 📂 Sample Data
The database is pre-populated with sample entries, including:

- Categories: Electronics, Groceries, Office Supplies

- Employees: Alice Mwangi, John Otieno

- Locations: Main Warehouse, Outlet Store

- Products: Laptop HP EliteBook, A4 Printing Paper, Sugar 1kg

- Suppliers: TechWorld Ltd, Stationery Hub

- Inventory Transactions: Initial stock entries and sales

## 📄 Deliverables
inventory_db.sql: Contains all CREATE TABLE statements and INSERT statements for sample data.

## 🛠️ Getting Started
- Import the SQL File:

- Use MySQL Workbench or the MySQL command-line tool to import inventory_db.sql into your MySQL server.

- Verify the Data:

- Run queries to ensure all tables are created and populated correctly.

## 🧾 Notes
Ensure MySQL Server version 8.0 or higher is installed.

Modify the inventory_db.sql file as needed to fit specific requirements or to add more data.
  
## 🔧 Suggested Enhancements
User Authentication: Implement user roles and permissions for enhanced security.

Inventory Alerts: Set up triggers or scheduled events to notify when stock levels are low.

Reporting Module: Generate reports on inventory movements, stock levels, and supplier performance.

Integration with Frontend: Develop a user interface for easier interaction with the database.



# QUESTION 2
## 📝 Task Manager CRUD API
A simple and efficient Task Manager API built with FastAPI, SQLAlchemy, and MySQL. This application supports full CRUD (Create, Read, Update, Delete) operations for managing users and their associated tasks.

## 📋 Table of Contents
- Features

- Tech Stack

- Setup Instructions

- API Endpoints

- Testing the API

- Project Structure



## ✅ Features
- User Management: Create, retrieve, update, and delete user profiles.

- Task Management: Assign tasks to users with the ability to create, retrieve, update, and delete tasks.

- Relational Database: Utilizes MySQL for data storage with SQLAlchemy ORM for database interactions.

- Interactive Documentation: Automatically generated Swagger UI for easy API exploration and testing.

## 🛠 Tech Stack
- Backend Framework: FastAPI

- Database: MySQL

- ORM: SQLAlchemy

- Data Validation: Pydantic

- Server: Uvicorn

## 🚀 Setup Instructions
Prerequisites
- Python 3.7 or higher

- MySQL Server

- pip (Python package installer)

Installation Steps
1. Clone the Repository

- git clone https://github.com/Ocheing/wk-8-database.git
- cd task-manager-api
  
2. Create a Virtual Environment

python -m venv venv

3. Activate the Virtual Environment

- On Windows:
  
venv\Scripts\activate

- On macOS/Linux:
  
source venv/bin/activate

4. Install Dependencies

pip install -r requirements.txt

5. Configure the Database

- Ensure MySQL server is running.

- Create a new database:

CREATE DATABASE task_manager_db;
- Update the database.py file with your MySQL credentials:
SQLALCHEMY_DATABASE_URL = "mysql+mysqlconnector://username:password@localhost/task_manager_db"

6. Run the Application

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

