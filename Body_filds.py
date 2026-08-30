from typing import Annotated

from fastapi import Body, FastAPI,Path,Query
from pydantic import BaseModel, Field

app = FastAPI()


class Item(BaseModel):
    name: str
    description: str | None = Field(
        default=None, title="The description of the item", max_length=300
    )
    price: float = Field(gt=0, description="The price must be greater than zero")
    tax: float | None = None


@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Annotated[Item, Body(embed=True)]):
    results = {"item_id": item_id, "item": item}
    return results


# implementing path and query at the same time 
@app.get("/items_search/{item_id}")
async def get_items(item_id:Annotated[int|None,Path(
    title="The id of the item",
    description="Put the item id",
    gt=0,le=1000)],

    item_name:Annotated[str|None,Query(
    title="the name of the item",
    description="Put the name of the iten")
    ]
    ):
    print(item_id,item_name)
    result={"item_id":item_id,"item_name":item_name}
    return result