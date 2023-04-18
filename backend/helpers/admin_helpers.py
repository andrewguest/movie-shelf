import os

from fastapi import File, UploadFile, Response


VALID_FILE_EXTENSIONS = [".csv"]
MB = 1024 * 1024  # 1MB in bytes


async def validate_uploaded_file(uploaded_file: UploadFile = File(...)):
    """Validate the the uploaded file meets the following criteria:
        - size is 50MB or less
        - file extension is in the VALID_FILE_EXTENSIONS list

    Args:
        uploaded_file (UploadFile, optional): Uploaded file. Defaults to File(...).
    """

    file_extension = os.path.splitext(uploaded_file.filename)[1]

    if file_extension in VALID_FILE_EXTENSIONS and (
        (uploaded_file.size / 1000000) <= 50 * MB
    ):
        return True, {}
    elif file_extension not in VALID_FILE_EXTENSIONS:
        return False, {
            "Error": "Invalid file type",
            "Message": f"Invalid file extension: {file_extension}",
        }
    elif (uploaded_file.size / 1000000) > 50 * MB:
        return False, {
            "Error": "File too large",
            "Message": "The file size limit is 50MB",
        }
    else:
        return False, {
            "Error": "Uncaught validation error",
            "Message": "An uncaught error has occurred",
        }
