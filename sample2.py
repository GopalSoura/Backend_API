from fastapi import Request
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

#Request library is a class that is used to get multiple values from the end point dynamically without creating individual parameters 
@app.get("/show")
def argument_request(request:Request=None):
    request=dict(request.query_params)
    print(request)
    return "How are you today" if request.get("name")==None else f"Hii {request.get("name")} How are you doing today Your age must be : {request.get("age")}"
