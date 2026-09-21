from enum import Enum

class VectorDBEnums(Enum):
    QDRANT = "QDRANT"

class DistanceMetricsEnum(Enum):
    COSINE = "cosine"
    DOT = "dot"
    