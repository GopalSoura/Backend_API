from typing import Annotated

from fastapi import FastAPI, Path, Query

app = FastAPI()

#path : path is used to provide the additional information (meta data) for path paramter in api endpoint to see it in openapi documentation (openapi.json)
@app.get("/items/{item_id}")
async def read_items(
    item_id: int= Path(title="The id of the item to get"),# Here i have not decalred the none value for this parameter so it is mandatory to pass the value of it 
    q: str | None=Query(alias="item-query")# Here i have decalered the none value so it is optional to pass the query in run time 
    ):
    print(item_id)
    results = {"item_id": item_id}
    if q:
        results.update({"q": q})
        print(results)
    return results
'''
If you want to:

declare the q query parameter without a Query nor any default value
declare the path parameter item_id using Path
have them in a different order
not use Annotated
...Python has a little special syntax for that.

Pass *, as the first parameter of the function.

Python won't do anything with that *, but it will know that all the following 
parameters should be called as keyword arguments (key-value pairs), 
also known as kwargs. Even if they don't have a default value.
'''

'''
#passing * as default parameter
@app.get("/item/{item_id}")
async def read_items(*, item_id: int = Path(title="The ID of the item to get"), q: str=None):
    results = {"item_id": item_id}
    if q:
        results.update({"q": q})
    return 
'''


# setting min value 1 using ge  ( g=greator than ,e= equal to ,le=less than equal to ,gt=greator than  ,lt=less than equal to)

@app.get("/item/{item_id}")
async def read_items(
    item_id: Annotated[int, Path(title="The ID of the item to get", ge=1)], q: str
):
    results = {"item_id": item_id}
    if q:
        results.update({"q": q})
    return results