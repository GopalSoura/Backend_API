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


@app.get("/item/{item_id}")
async def read_items(*, item_id: int = Path(title="The ID of the item to get"), q: str):
    results = {"item_id": item_id}
    if q:
        results.update({"q": q})
    return results