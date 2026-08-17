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
    