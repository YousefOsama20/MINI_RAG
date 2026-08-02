from fastapi import FastAPI,APIRouter
from dotenv import load_dotenv
import os

load_dotenv()

base_router=APIRouter(
    prefix="/api/v1",
    tags =["api_v1"]
)

@base_router.get("/")
async def welcome():
    app_name = os.getenv("APP_NAME")
    app_version = os.getenv("APP_VERSION")

    return {
        "message": app_name,
        "version": app_version
    }