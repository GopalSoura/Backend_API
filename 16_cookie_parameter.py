# we can declare the cookie parameters same as the Path and Query parameter
from typing import Annotated

from fastapi import Cookie, FastAPI

app = FastAPI()


@app.get("/items/")
async def read_items(ads_id: Annotated[str | None, Cookie()] = None):
    print(ads_id,type(ads_id))
    return {"ads_id": ads_id}
