from .Provider import QdrantDB
from .VectorDBEnums import VectorDBEnums
from controllers.BassController import BassController


class VectorDBProviderFactory:

    def __init__(self, config):
        self.config = config
        self.base_controller = BassController()

    def create(self, provider: str):
        
        if provider == VectorDBEnums.QDRANT.value:

            database_path = self.base_controller.get_database_path(db_name = self.config.VECTOR_DB_PATH)

            return QdrantDB(
                db_path = database_path,
                distance_method = self.config.VECTOR_DB_DISTANCE_METHOD
            )
        
        else:
            raise ValueError(f"Unknown database type: {provider}")
