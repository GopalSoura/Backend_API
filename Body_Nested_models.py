from fastapi import FastAPI,Path
from typing import Annotated
from pydantic import BaseModel,Field

app = FastAPI()


class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None
    tags: list[str] = []


@app.get("/items/{item_id}")
async def update_item(item_id: int, item: Item):
    results = {"item_id": item_id, "item": item}
    print(results)
    return results

# validator as value type in  body and list of string in field
@app.put("/item/{item_id}")
async def update_item(item_id: int, item: Item):
    results = {"item_id": item_id, "item": item}
    return results

#Nested Basemodel with pydantic for image urls 
'''
class Image(BaseModel):
    url:str
    name:str

class Data(BaseModel):
    id:Annotated[int,Field(title="Student Id",ge=0,description="Enter the id of the student")]
    name:str|None=None
    description:str|None=None
    Rollno:str|None=None
    address:str|None=None
    image:Image|None=None

@app.put("/Studnets/{id}")
async def update_student_id(id:int,data:Data):
    data.id=id
    result={"id":id,"data":data}
    return result


'''

# validating image with pydantic HttpUrl
'''
from pydantic import HttpUrl
class Image(BaseModel):
    url:HttpUrl
    name:str

class Data(BaseModel):
    id:Annotated[int,Field(title="Student Id",ge=0,description="Enter the id of the student")]
    name:str|None=None
    description:str|None=None
    Rollno:str|None=None
    address:str|None=None
    image:Image|None=None

@app.put("/Studnets/{id}")
async def update_student_id(id:int,data:Data):
    data.id=id
    result={"id":id,"data":data}
    return result
'''
# decalring the image as list in body so that Image basemodel class provide validation and metadata for each image inside the list in the form of dictionary 
'''
images": [
        {
            "url": "http://example.com/baz.jpg",
            "name": "The Foo live"
        },
        {
            "url": "http://example.com/dave.jpg",
            "name": "The Baz"
        }
'''
'''
from pydantic import HttpUrl
class Image(BaseModel):
    url:HttpUrl
    name:str

class Data(BaseModel):
    id:Annotated[int,Field(title="Student Id",ge=0,le=100,description="Enter the id of the student")]
    name:str|None=None
    description:str|None=None
    Rollno:str|None=None
    address:str|None=None
    image:list[Image]|None=None

@app.put("/Studnets/{id}")
async def update_student_id(id:int,data:Data):
    data.id=id
    result={"id":id,"data":data}
    return result
'''
#deep nested loop using 3 BaseModel classes Offer,Item,Image in single query or function 
from pydantic import HttpUrl
class Image(BaseModel):
    url: HttpUrl
    name: str


class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None
    tags: set[str] = set()
    images: list[Image] | None = None


class Offer(BaseModel):
    name: str
    description: str | None = None
    price: float
    items: list[Item]


@app.post("/offers/")
async def create_offer(offer: Offer):
    return offer

# declaring the type in the parameter of the function, the same as in Pydantic models:
# Here i am setting the image as a list of BaseModel class
@app.post("/images/multiple/")
async def create_multiple_images(images: list[Image]):
    print(images,type(images))
    return images

#Declared body in parameter of the function to simplify it 
@app.post("/index-weights/")
async def create_index_weights(weights: dict[int, float]):
    print(weights,type(weights))
    return weights