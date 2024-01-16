import pytest
from ChatGPT import zipfs_law as ChatGPT
from CodeLLama import zipfs_law as CodeLLama
from Bard import zipfs_law as Bard

# Define the implementations with their names
implementations = [
    (ChatGPT, 'ChatGPT'),
    (CodeLLama, 'CodeLLama'),
    (Bard, 'Bard')
]

string_input = "test the pudim is test"

@pytest.fixture(params=implementations, ids=[impl[1] for impl in implementations])
def implementation(request):
    impl, _ = request.param
    return impl

def test_zipf_law(implementation):
    try:
        top_10_words = implementation(string_input)
        assert top_10_words == ['test', 'the', 'pudim', 'is'], "Data is not sorted correctly"
    except Exception as e:
        pytest.fail(f"An error occurred during testing: {str(e)}")

# To execute this test, run the following command:
# pytest -v -s F:\TFG\TDD_Can_LLM_Code_unit_tests\Unit_tests_python\EX-03-zipf_law\zipf_test.py
# -v: verbose
# -s: print statements