from enum import Enum

class VectorDBEnums(Enum):
    QDRANT = "Qdrant"

class DistanceMetricsEnum(Enum):
    COSINE = "cosine"
    DOT = "dot"
    