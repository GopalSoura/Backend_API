from typing import Annotated

from fastapi import FastAPI, Query

app = FastAPI()


@app.get("/items/")
async def read_items(
    q: Annotated[str | None,Query(title="Query String",min_length=3)] = None,):
    
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results

#passing a list in query with multiple values (Adding items one by one )
@app.get("/items_list/")
async def read_items(q: Annotated[list[str] | None, Query()] = None):
    query_items = {"q": q}
    return query_items


# default list of values 
@app.get("/items_deafault_list /")
async def read_items(q: Annotated[list[str], Query()] = ["foo", "bar"]):
    query_items = {"q": q}
    return query_items

#using list directly 
@app.get("/items_list2/")
async def read_items(q: Annotated[list, Query()] = []):
    query_items = {"q": q}
    return query_items