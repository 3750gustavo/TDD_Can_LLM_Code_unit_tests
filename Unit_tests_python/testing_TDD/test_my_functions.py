import pytest
from source import my_functions

# Using pytest.mark.parametrize to test multiple scenarios.
# Each tuple in the list represents a test case with:
# (first_number, second_number, expected_sum)
@pytest.mark.parametrize("first_number, second_number, expected_sum", [
    (2, 2, 4),
    (1, 2, 3),
    (0, 0, 0),
    (-1, 2, 1),
    (-1, -1, -2),
    (1.1, 2.2, 3.3),
    ('Hello', ' World', pytest.raises(TypeError)),
])
def test_add_two_numbers(first_number, second_number, expected_sum):
    # Test if function returns correct sum or raises TypeError for invalid inputs.
    if isinstance(expected_sum, Exception):
        with expected_sum:
            my_functions.add_two_numbers(first_number, second_number)
    else:
        assert my_functions.add_two_numbers(first_number, second_number) == expected_sum

# Running the tests:
# Use the command 'pytest -v -s <path_to_test_file>' in the terminal.
# Options:
# -v (verbose): shows detailed test results.
# -s: displays print statements from the tests.
# Additional options:
# -x, --exitfirst: stops after the first failure.
# -k EXPRESSION: runs tests matching the substring expression.
# -m MARKEXPR: runs tests matching the given mark expression.