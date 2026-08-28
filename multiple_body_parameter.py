from typing import Annotated

from fastapi import FastAPI, Path,Body
from pydantic import BaseModel

app = FastAPI()

#Multiple parameters with pydantic model 

class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None


class User(BaseModel):
    username: str
    full_name: str | None = None

@app.put("/item/{item_id}")
async def update_item(
    item_id: Annotated[int, Path(title="The ID of the item to get", ge=0, le=1000)],
    q: str | None = None,
    item: Item | None = None,
):
    results = {"item_id": item_id}
    if q:
        results.update({"q": q})
    if item:
        results.update({"item": item})
    return results
# here we are using non annotated pydantic model 
@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Item, user: User):
    results = {"item_id": item_id, "item": item, "user": user}
    return results


# created extended body for importance .
# Here we dont need to create an additional pydantic body for (importance ) .
# the Body() automatically detect the single parameter as a body .
@app.put("/items/{item_id}")
async def update_item( item_id: int, item: Item, user: User, importance: Annotated[int, Body()] ):
    results = {"item_id": item_id, "item": item, "user": user, "importance": importance}
    return results

@app.put("/item_1/{item_id}")
async def update_item(
    *,
    item_id: int,
    item: Item,
    user: User,
    importance: Annotated[int, Body(gt=0)],
    q: str | None = None,
):
    results = {"item_id": item_id, "item": item, "user": user, "importance": importance}
    if q:
        results.update({"q": q})
    return results
# Here the body is item only . and item is embeded in body . So no need to pass item as key values in respect key 
@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Annotated[Item, Body(embed=True)]):
    results = {"item_id": item_id, "item": item}
    return results
