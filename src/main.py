from fastapi import FastAPI , APIRouter
from routes import base ,data
from motor.motor_asyncio import AsyncIOMotorClient
from helpers.config import get_settings

print("MAIN.PY LOADED")

app = FastAPI()

@app.on_event("startup")
async def startup_db_client():
    setting = get_settings()
    
    app.mongodb_conn = AsyncIOMotorClient(setting.MONGODB_URL)
    app.db_client = app.mongodb_conn[setting.MONGODB_DATABASE] 

@app.on_event("shutdown")
async def shutdown_db_client():
    app.mongodb_conn.close()

app.include_router(base.base_router)
app.include_router(data.data_router)

 