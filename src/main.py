from fastapi import FastAPI , APIRouter
from routes import base ,data, nlp
from motor.motor_asyncio import AsyncIOMotorClient
from helpers.config import get_settings
from stores.llm.LLMProviderFactory import LLMProviderFactory
from stores.vectordb.VectorDBProviderFactory import VectorDBProviderFactory    

print("MAIN.PY LOADED")

app = FastAPI()

@app.on_event("startup")
async def startup_db_client():
    setting = get_settings()
    
    app.mongodb_conn = AsyncIOMotorClient(setting.MONGODB_URL)
    app.db_client = app.mongodb_conn[setting.MONGODB_DATABASE] 

    llm_provider_factory = LLMProviderFactory(setting)
    vectordb_provider_factory = VectorDBProviderFactory(setting)

    #generation client
    app.generation_client = llm_provider_factory.create(provider = setting.GENERATION_BACKEND)
    app.generation_client.set_generation_model(model_id = setting.GENERATION_MODEL_ID)

    #embedding client
    app.embedding_client = llm_provider_factory.create(provider = setting.EMBEDDING_BACKEND)
    app.embedding_client.set_embedding_model(model_id = setting.EMBEDDING_MODEL_ID,
                                            embedding_size = setting.EMBEDDING_MODEL_SIZE)    

    # vector db client
    app.vectordb_client = vectordb_provider_factory.create(
        provider=setting.VECTOR_DB_BACKEND
    )
    app.vectordb_client.connect()      

@app.on_event("shutdown")
async def shutdown_db_client():
    app.mongodb_conn.close()
    app.vectordb_client.disconnect()

app.include_router(base.base_router)
app.include_router(data.data_router)
app.include_router(nlp.nlp_router)
 