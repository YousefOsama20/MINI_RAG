from pydantic import BaseModel , Field , validator
from bson.objectid import ObjectId
from typing import Optional

class DataChunk(BaseModel):
    
    _id : Optional[ObjectId]
    chunk_text : str = Field(..., min_length=1)
    chunk_metadata:  dict   
    chunk_order: int = Field(..., min_length=1)
    chnk_projcet_id: ObjectId

    class Config:
        arbitrary_types_allowed = True    
