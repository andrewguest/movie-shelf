import csv

from fastapi import APIRouter, File, Response, UploadFile

from helpers.admin_helpers import validate_uploaded_file


router = APIRouter(tags=["admin"])


@router.post("/admin/import")
async def import_from_csv(response: Response, file: UploadFile = File(...)):
    """Accept a file through a POST request of up to 50MB and
    with certain file extensions

    Args:
        response (Response): JSON response from route
        file (UploadFile, optional): File sent to this route. Max 50MB in size

    Returns:
        _type_: _description_
    """

    is_upload_file_valid, json_response_message = await validate_uploaded_file(
        uploaded_file=file
    )

    if is_upload_file_valid:
        file_contents = await file.read()
        decoded_file_contents = file_contents.decode("utf-8").splitlines()
        reader = csv.DictReader(decoded_file_contents)

        csv_row_count = len([row for row in reader])

        return {
            "Imported file": file.filename,
            "Rows imported from file": csv_row_count,
        }
    else:
        return json_response_message
