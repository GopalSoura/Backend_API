from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional
import mysql.connector

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "User API is running"}

@app.get("/health")
def health_check():
    return {"status": "ok"}

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

@app.get("/users")
def get_users():
    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)
    cursor.execute("SELECT * FROM users")
    users = cursor.fetchall()
    cursor.close()
    connection.close()
    return users

@app.get("/user/{user_id}")
def get_user(user_id: int):
    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)
    cursor.execute("SELECT * FROM users WHERE user_id = %s", (user_id,))
    user = cursor.fetchone()
    cursor.close()
    connection.close()
    if user is None:
        return {"error": "User not found"}
    return user

@app.put("/user/{user_id}")
def update_user(user_id: int, updated_user: User):
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute(
        "UPDATE users SET name = %s, email = %s, age = %s WHERE user_id = %s",
        (updated_user.name, updated_user.email, updated_user.age, user_id)
    )
    connection.commit()
    rowcount = cursor.rowcount
    cursor.close()
    connection.close()
    if rowcount == 0:
        return {"error": "User not found"}
    return {"message": "User updated", "user_id": user_id}

@app.delete("/user/{user_id}")
def delete_user(user_id: int):
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute("DELETE FROM users WHERE user_id = %s", (user_id,))
    connection.commit()
    rowcount = cursor.rowcount
    cursor.close()
    connection.close()
    if rowcount == 0:
        return {"error": "User not found"}
    return {"message": "User deleted", "user_id": user_id}