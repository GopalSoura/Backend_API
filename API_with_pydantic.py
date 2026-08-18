from data import products
from fastapi import FastAPI
from pydantic import BaseModel
from data import products as p

app=FastAPI()
class items(BaseModel):
    id:int=None
    name:str=None
    price:float=None
    rating:float=None
    
@app.post("/create")  # method to create the item with request body
def create_items(item:items):
    print(item.model_dump()) # convert the BaseModel class to dictonary
    products.append(item.model_dump())
    print(products)
    return item

@app.put("/update items") # method to update the items with request body and query paramter
def update_items(item:items,id:int):
    if id ==None or item==None :
        return "something is wrong put the id again "
    for product in products:
        if product.get("id")==id:
            print(product)
            product.update({"name": item.name,"price": item.price,"rating": item.rating})
            print(product)
            return "Items updated sucessfully"
    return "Item not found"

    

