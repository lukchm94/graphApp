from fastapi import APIRouter
from typing import Dict, Any
router = APIRouter()

@router.get("/")
async def read_root():
    return {"message": "Welcome to the FastAPI application!"}

@router.get("/items/{item_id}")
async def read_item(item_id: int) -> Dict[str, Any]:
    return {"item_id": item_id, "name": f"Item {item_id}"}

# Additional routes can be added here.