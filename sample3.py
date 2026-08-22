#HTTPS methods :- GET,POST,PUT,DELETE,PATCH

#GET :- read the resource  (READ)
#POST :- create the resource and send something to server  (CREATE)
#PUT :- update the resource completely (UPDATE)
#DELETE :- delete the resource (DELETE)
#PATCH :- partially update the resource (PARIIALLY UPDATE)

# for POST method  -> client send data alongwith the path parameter {No need of data_ID}
# for PUT method  -> client send data and data_ID alongwith the path parameter {need of data_ID}
# for DELETE method -> client send  only data_ID alongwith the path parameter {need of data_ID}

from fastapi import FastAPI
from data import products

app=FastAPI()
@app.post("/create items ") # method to create the items with query parameters 
def create_item(id:int=None,name:str=None,price:float=None,rating:float=None):
    if id==None or name==None or price==None or rating==None:
        return "Please enter all the fields"
    
    products.append({"id":id,"name":name,"price":price,"rating":rating})
    print(products[id-1])
    return f"Item  created successfully on index {id-1}"
