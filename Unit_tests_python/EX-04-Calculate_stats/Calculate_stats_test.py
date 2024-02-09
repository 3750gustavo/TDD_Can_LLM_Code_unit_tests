import pytest
from ChatGPT import calculate_stats as ChatGPT
from CodeLLama import calculate_stats as CodeLLama
from Copilot import calculate_stats as Copilot
    
# Define the implementations with their names
implementations = [
    (ChatGPT, 'ChatGPT'),
    (CodeLLama, 'CodeLLama'),
    (Copilot, 'Copilot')
]

# Define the 3 input lists with 3 types of levels of variation in the data

# List 1: Low variation
list1 = [10,9,11,10,8,12,11,9,10,11]
# List 2: Same, but with a few anomalies
list2 = [3,9,11,10,8,12,11,9,10,23]
# List 3: High variation, almost random
list3 = [1,19,9,5,2,18,13,7,4,6]

# Define the expected results
expected_results = {
    'mean_list1': 10.1, 'stddev_list1': 1.1357816691601,
    'mean_list2': 10.6, 'stddev_list2': 4.7581509013481,
    'mean_list3': 8.4, 'stddev_list3': 6.0033324079215
}

@pytest.fixture(params=implementations, ids=[impl[1] for impl in implementations])
def implementation(request):
    impl, _ = request.param
    return impl

def test_calculate_stats(implementation):
    # Call the implementation to get the results dictionary
    results = implementation(list1, list2, list3)
    # Check the results
    try:
        for key, value in expected_results.items():
            assert results[key] == value, (
                f"Test failed for {implementation.__name__}. "
                f"Expected {key}: {value}, got: {results[key]}"
            )
    except AssertionError as ae:
        print(f"Test failed for {implementation.__name__}. Output dictionary: {results}")
        raise ae
    except Exception as e:
        pytest.fail(f"An error occurred during testing: {str(e)}")
        
# To execute this test, run the following command:
# pytest -v -s F:\TFG\TDD_Can_LLM_Code_unit_tests\Unit_tests_python\EX-04-Calculate_stats\Calculate_stats_test.py
# -v: verbose
# -s: print statements