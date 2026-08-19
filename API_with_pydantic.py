from data import products
from fastapi import FastAPI
from pydantic import BaseModel
from data import products as p

app=FastAPI()
class Items(BaseModel):
    id:int=None
    name:str=None
    price:float=None
    rating:float=None

@app.get("/home")
def home():
    return products 
    
    
@app.post("/create")  # method to create the item with request body
def create_items(item:Items):
    print(item.model_dump()) # convert the BaseModel class to dictonary
    products.append(item.model_dump())
    print(products)
    return item

@app.put("/update items") # method to update the items with request body and query paramter
def update_items(item:Items,id:int):
    if id ==None or item==None :
        return "something is wrong put the id again "
    for product in products:
        if product.get("id")==id:
            print(product)
            product.update({"name": item.name,"price": item.price,"rating": item.rating})
            print(product)
            return "Items updated sucessfully"
    return "Item not found"


# update the products in enumerate
@app.put("/update_products")
def update_products_enumerate(item:Items,id:int):
    if item==None :
        return "Product dict is empty" 
    if id==None:
        return "Please enter the product_ID"

    for index ,product in enumerate(products):
        if product.get("id")==id:
            products[index]=item.model_dump()
            print(type(product),product)
            return product
    return "Item not found"

# Delete the items present in the products dictionary using enumerate 
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

    

