# we can declare the cookie parameters same as the Path and Query parameter
from fastapi import Response
from typing import Annotated

from fastapi import Cookie, FastAPI

app = FastAPI()

'''
@app.get("/items/")
async def read_items(ads_id: Annotated[str | None, Cookie()] = None):
    print(ads_id,type(ads_id))
    return {"ads_id": ads_id}

'''
#Storing cookie in the browser the user inout session_id
@app.get("/Items")
async def store_cookie(response:Response):
    response.set_cookie(key="Session_id",value="Value")
    return{"Message":"Cookie stored"}

# Reading the cookie from the browser stored in the above api 
@app.get("/show_cookies")
async def show_cookie(Session_id:Annotated[str|None ,Cookie()]=None):
    print(Session_id)
    return {"Session_id":Session_id}