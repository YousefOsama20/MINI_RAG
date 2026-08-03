from fastapi import FastAPI , APIRouter
from routes import base ,data

print("MAIN.PY LOADED")

app = FastAPI()
app.include_router(base.base_router)
app.include_router(data.data_router)

