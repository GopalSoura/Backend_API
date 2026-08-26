from typing import Annotated

from fastapi import FastAPI, Path, Query

app = FastAPI()


@app.get("/items/{item_id}")
async def read_items(
    item_id: int= Path(title="The id of the item to get"),
    q: str | None=Query(alias="item-query")
):
    results = {"item_id": item_id}
    if q:
        results.update({"q": q})
        print(results)
    return results
