from src import prep_data


def test_some_function():
    a, b = 1, 2
    actual_value = prep_data.some_function(a, b)
    expected_value = 3
    print("Testing 'some_function'")
    assert actual_value == expected_value
