from src import prep_data
from src import variables

def test_run_prep_data():
    """
    Test the run_prep_data function to ensure it processes data correctly.
    """
    raw_data_path = variables.RAW_DATA_PATH
    dest_path = variables.TESTING_DATA

    # Run the prep_data function
    result = prep_data.run_prep_data(raw_data_path, dest_path)

    # Check if the result is True indicating successful execution
    assert result is True, "run_prep_data did not complete successfully"
