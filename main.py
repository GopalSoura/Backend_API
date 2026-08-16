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