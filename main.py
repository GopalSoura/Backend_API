from fastapi import FastAPI
from pydantic import BaseModel
from typing import List, Optional
import mysql.connector

app = FastAPI()

class User(BaseModel):
    name: str
    email: str
    age: Optional[int] = None

class UserOut(User):
    user_id: int

DB_CONFIG = {
    "host": "localhost",
    "user": "root",
    "password": "password",
    "database": "user_db"
}

def get_db_connection():
    return mysql.connector.connect(**DB_CONFIG)

def create_table():
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            user_id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(100) NOT NULL,
            email VARCHAR(100) NOT NULL,
            age INT
        )
    """)
    connection.commit()
    cursor.close()
    connection.close()

create_table()

@app.post("/user")
def create_user(user: User):
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute(
        "INSERT INTO users (name, email, age) VALUES (%s, %s, %s)",
        (user.name, user.email, user.age)
    )
    connection.commit()
    user_id = cursor.lastrowid
    cursor.close()
    connection.close()
    return {"message": "User created", "user_id": user_id}