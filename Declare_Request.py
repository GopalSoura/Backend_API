# Additional information for Json Schema and OpenApi Schema with time,description,example,information
from time import time
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None

    model_config = {
        "json_schema_extra": {
            "description":"Request Body",
            "time":str(time()),
            "examples": [
                {
                    "name": "Foo",
                    "description": "A very nice Item",
                    "price": 35.4,
                    "tax": 3.2,
                }
            ]
        }
    }


@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Item):
    results = {"item_id": item_id, "item": item}
    return results

# Output
'''
"Item": {
    "properties": {
        "name": {"type": "string"},
        "description": {"type": "string / null"},
        "price": {"type": "number"},
        "tax": {"type": "number / null"}
    },
    "required": ["name", "price"]
}
'''