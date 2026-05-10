from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
app = FastAPI()

class Car(BaseModel):
    car_id: int
    name: str
    origin: str

car_model:list[Car]= []

@app.get("/")
def read_root():
    return {"message": "Welcome to my first FastAPI code with car"}

@app.get("/cars")
def get_cars():
    return car_model

@app.post("/cars")
def add_car(car: Car):
    car_model.append(car)
    return car

@app.put("/car/{car_id}")
def update_car(car_id: int, updated_car: Car):
    for index, existing_car in enumerate(car_model):
        if existing_car.car_id == car_id:
            car_model[index] = updated_car
            return updated_car

    return {"error": "Car not found"}

@app.delete("/car/{car_id}")
def delete_car(car_id: int):
    for index, car in enumerate(car_model):
        if car.car_id == car_id:
            deleted = car_model.pop(index)
            return deleted

    return {"error": "Car not deleted"}