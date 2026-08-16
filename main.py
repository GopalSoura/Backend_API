from fastapi import FastAPI
from pydantic import BaseModel
from typing import List, Optional
import mysql.connector

app = FastAPI()

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