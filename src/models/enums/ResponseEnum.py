from enum import Enum

class ResponseSignal(Enum):

    FILE_VALIDATED_SUCCESS = "file_validate_successfully"
    FILE_SIZE_EXCEEDED = "failed to upload file, file size exceeds limit"
    FILE_TYPE_NOT_ALLOWED = "failed to upload file, file type not allowed"
    FILE_UPLOAD_SUCCESS = "successfully uploaded file"
    FILE_UPLOAD_FAILED = "failed to upload file"
    FILE_PROCESS_SUCCESS = "successfully processed file"
    FILE_PROCESS_FAILED = "failed to process file"
    No_FILES_ERORR = "not_found_files"
    PROJECT_NOT_FOUND = "project_not_found"
    INSERT_INTO_VECTORDB_ERROR = "insert_into_vectordb_error"
    INSERT_INTO_VECTORDB_SUCCESS = "insert_into_vectordb_success"
    VECTORDB_COLLECTION_RETRIEVED = "vectordb_collection_retrieved"
    VECTORDB_SEARCH_ERROR = "vectordb_search_error"
    VECTORDB_SEARCH_SUCCESS = "vectordb_search_success"
    RAG_ANSWER_ERROR = "rag_answer_error"
    RAG_ANSWER_SUCCESS = "rag_answer_success"
    