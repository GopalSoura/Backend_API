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

# validating image with pydantic url
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
