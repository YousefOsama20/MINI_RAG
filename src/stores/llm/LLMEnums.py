from enum import Enum

class LLMEnums(Enum):

    OPENAI = "OPENAI"
    COHERE = "COHERE"
 

class OpenAIEnums(Enum):
    SYSTEM = "system"
    USER = "user"
    ASSISTANT = "assistant"

class CohereEnums(Enum):
    SYSTEM = "SYSTEM"
    USER = "USER"
    ASSISTANT = "CHATBOT" 

    # Embed
    QUERY = "search_query"
    DOCUMENT = "search_document"
    
class DocumentTypeEnum(Enum):
    DOCUMENT = "document"
    QUERY = "query"