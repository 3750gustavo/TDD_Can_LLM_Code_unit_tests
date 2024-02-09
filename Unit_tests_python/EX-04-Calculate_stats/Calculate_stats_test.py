import pytest
from ChatGPT import calculate_stats as ChatGPT
from CodeLLama import calculate_stats as CodeLLama

# Define the implementations with their names
implementations = [
    (ChatGPT, 'ChatGPT'),
    (CodeLLama, 'CodeLLama')
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
    'mean_list1': 10.0, 'stddev_list1': 1.0,
    'mean_list2': 10.3, 'stddev_list2': 4.0,
    'mean_list3': 9.4, 'stddev_list3': 6.0
}

@pytest.fixture(params=implementations, ids=[impl[1] for impl in implementations])
def implementation(request):
    impl, _ = request.param
    return impl

def test_calculate_stats(implementation):
    # Calculate the stats
    stats = implementation(list1, list2, list3)
    # Check the mean and standard deviation for each list
    assert stats['mean_list1'] == expected_results['mean_list1'], f"Test failed for {implementation.__name__}. Mean for list1 mismatch. Expected: {expected_results['mean_list1']}, got: {stats['mean_list1']}"
    assert stats['stddev_list1'] == expected_results['stddev_list1'], f"Test failed for {implementation.__name__}. Stddev for list1 mismatch. Expected: {expected_results['stddev_list1']}, got: {stats['stddev_list1']}"
    assert stats['mean_list2'] == expected_results['mean_list2'], f"Test failed for {implementation.__name__}. Mean for list2 mismatch. Expected: {expected_results['mean_list2']}, got: {stats['mean_list2']}"
    assert stats['stddev_list2'] == expected_results['stddev_list2'], f"Test failed for {implementation.__name__}. Stddev for list2 mismatch. Expected: {expected_results['stddev_list2']}, got: {stats['stddev_list2']}"
    assert stats['mean_list3'] == expected_results['mean_list3'], f"Test failed for {implementation.__name__}. Mean for list3 mismatch. Expected: {expected_results['mean_list3']}, got: {stats['mean_list3']}"
    assert stats['stddev_list3'] == expected_results['stddev_list3'], f"Test failed for {implementation.__name__}. Stddev for list3 mismatch. Expected: {expected_results['stddev_list3']}, got: {stats['stddev_list3']}"

# To execute this test, run the following command:
# pytest -v -s F:\TFG\TDD_Can_LLM_Code_unit_tests\Unit_tests_python\EX-04-Calculate_stats\Calculate_stats_test.py
# -v: verbose
# -s: print statements