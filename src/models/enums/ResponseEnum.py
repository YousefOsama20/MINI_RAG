from enum import Enum

class ResponseSignal(Enum):

    FILE_VALIDATED_SUCCESS = "file_validate_successfully"
    FILE_SIZE_EXCEEDED = "failed to upload file, file size exceeds limit"
    FILE_TYPE_NOT_ALLOWED = "failed to upload file, file type not allowed"
    FILE_UPLOAD_SUCCESS = "successfully uploaded file"
    FILE_UPLOAD_FAILED = "failed to upload file"
