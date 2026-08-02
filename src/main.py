from fastapi import FastAPI , APIRouter
from dotenv import load_dotenv
load_dotenv()

from routes import base

app=APIRouter()
app.include_router(base.base_router)
 