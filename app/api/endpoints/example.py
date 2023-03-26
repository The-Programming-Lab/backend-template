from fastapi import APIRouter
from app.api.config import hello_world

router = APIRouter(prefix="/user/braeden/api", tags=["example"])


@router.get("/example")
async def example():
    return {"message": hello_world}