from fastapi import APIRouter
from app.api.endpoints import health, items

router = APIRouter()

router.include_router(health.router, tags=["health"])
router.include_router(items.router, prefix="/items", tags=["items"])
