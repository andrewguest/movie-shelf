import io

from fastapi.testclient import TestClient

from app.main import app
from tests.data.mock_csv_data import mock_csv_rows


client = TestClient(app)


def test_import_from_csv():
    """POST a CSV file to `/admin/import`

    This data is mocked in `test/data/mock_csv_data`
        and POSTed to the API endpoints for tests.
    """

    # utf-8 encode the mock CSV data
    csv_file = io.BytesIO(mock_csv_rows.encode())

    # the name of the CSV file
    csv_filename = "import_mock_file.csv"

    # count of rows in the CSV file
    # subtract 1 for the header row
    csv_row_count = len(mock_csv_rows.splitlines()) - 1

    ###############################################
    # test that the route works with a valid file #
    ###############################################
    response = client.post(
        "/admin/import", files={"file": (csv_filename, csv_file, "text/csv")}
    )

    assert response.status_code == 200
    assert response.json() == {
        "Imported file": csv_filename,
        "Rows imported from file": csv_row_count,
    }

    #######################################
    # test with an invalid file extension #
    #######################################
    response = client.post(
        "/admin/import",
        files={"file": ("import_mock_file.badfile", csv_file, "text/csv")},
    )

    assert response.status_code == 400
    assert response.json() == {
        "Error": "Invalid file type",
        "Message": "Invalid file extension: .badfile",
    }
