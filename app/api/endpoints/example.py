from fastapi import APIRouter
from app.api.config import HELLO_WORLD

router = APIRouter(prefix='', tags=["example"])


@router.get("/example")
async def example():
    return {"message": HELLO_WORLD}