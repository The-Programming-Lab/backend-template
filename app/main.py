from fastapi import FastAPI
from app.api.endpoints import example

app = FastAPI()

# add router from api/endpoints/example.py
app.include_router(example.router)