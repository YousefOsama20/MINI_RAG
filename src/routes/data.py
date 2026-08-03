from fastapi import FastAPI, APIRouter, Depends, UploadFile, status
from fastapi.responses import JSONResponse
import os
from helpers.config import get_settings, Settings
from controllers import DataController
import logging
from controllers import DataController

logger = logging.getLogger('uvicorn.error')

data_router = APIRouter(
    prefix="/api/v1/data",
    tags=["api_v1", "data"],
)

@data_router.post("/upload/{project_id}")
async def upload_data(project_id: int, file: UploadFile,
                      app_settings: Settings = Depends(get_settings)):
        
    
    is_valid= DataController().validate_uploaded_file(file=file)

    return is_valid