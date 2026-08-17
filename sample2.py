from fastapi import FastAPI
from data import products
app=FastAPI()

@app.get("/")
def home():
    return "My name is gopal"

#path parameter with dyanmic router argument
@app.get("/products/{id}")
def show_products(id:int):
    for product in products:
        if product.get("id")==id:
            return product["name"]

    return "Not present"

@app.get("/greet")
def greet(name:str=None):
    return "How are you today" if name==None else f"Hii {name} How are you doing today"
    