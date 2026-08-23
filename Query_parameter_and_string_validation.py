from typing import Annotated

from fastapi import FastAPI, Query

app = FastAPI()

# providing meta data such as title
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

#using list directly without string or integer annotations
@app.get("/items_list2/")
async def read_items(q: Annotated[list, Query()] = []):
    query_items = {"q": q}
    return query_items

@app.get("/items_alias/")
async def read_items(q: Annotated[str | None, Query(alias="item-query")] = None):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results

# Deprecated query parameter: use an alias to expose a different parameter name
# to the frontend; deprecated=True marks the old parameter as temporarily supported.
@app.get("/items_depricated/")
async def read_items(
    q: Annotated[
        str | None,
        Query(
            alias="item-query",
            title="Query string",
            description="Query string for the items to search in the database that have a good match",
            min_length=3,
            max_length=50,
            pattern="^fixedquery$",
            deprecated=True,
        ),
    ] = None,
):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results