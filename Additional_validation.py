'''
from typing import Annotated

from fastapi import FastAPI, Query

app = FastAPI()


@app.get("/items/")
async def read_items(q: Annotated[str | None, Query(max_length=50)] = None):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    for i, j in results.items():
        print(i)
        print(j)
    return results

'''


from typing import Annotated

from fastapi import FastAPI, Query

app = FastAPI()

# Additional string validator to validate the length and pattern of the Query in string using annotated lib and quer
'''
@app.get("/items/")
async def read_items(
    q: Annotated[
        str | None, Query(min_length=3, max_length=50, pattern="\\b[A-Za-z]*\\b")
    ] = None,
):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
        print(results)
    return results
'''
# added fixedquery as default query using annotated lib and query
@app.get("/items/")
async def read_items(q: Annotated[str, Query(min_length=3)] = "fixedquery"):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
        print(results)
    return results

# declared NONE as default parameter in query (NO query required just keep it blank, q can be none)
@app.get("/items_default/")
async def read_items(q: Annotated[str | None, Query()]=None):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
        print(results)
    return results
# Query should be present any how or else it will show error
@app.get("/items_required_parameter/")
async def read_items(q: Annotated[str | None, Query(min_length=3)]):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
        print(results)
    return results