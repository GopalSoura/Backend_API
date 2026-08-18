from pydantic import BaseModel
from fastapi import FastAPI
from data import products
app=FastAPI()

class Items(BaseModel):
    id:int=None
    name:str=None
    price:float=None
    rating:float=None

@app.delete("/delete_items")
def delete_items(item:Items,id:int):
    if item==None :
        return "Product dict is empty" 
    if id==None:
        return "Please enter the product_ID"
    for index,product in enumerate(products):
        print(product,index)
        if product.get("id")==id:
            removed=products.pop(index)
            print(removed)
            return f"product removed {removed}"
    return " item not found"