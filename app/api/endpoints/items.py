from fastapi import APIRouter, HTTPException
from typing import List
from app.schemas.item import ItemCreate, ItemResponse

router = APIRouter()

# In-memory storage for example
items = []

@router.post("/", response_model=ItemResponse)
async def create_item(item: ItemCreate):
    new_item = {**item.dict(), "id": len(items) + 1}
    items.append(new_item)
    return new_item

@router.get("/", response_model=List[ItemResponse])
async def get_items():
    return items

@router.get("/{item_id}", response_model=ItemResponse)
async def get_item(item_id: int):
    if item_id <= 0 or item_id > len(items):
        raise HTTPException(status_code=404, detail="Item not found")
    return items[item_id - 1]
