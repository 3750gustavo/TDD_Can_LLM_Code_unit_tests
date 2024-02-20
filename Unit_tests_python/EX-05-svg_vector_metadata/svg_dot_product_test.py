import pytest
# for path handling
import os
# Import the implementations
from Perplexity import svg_dot_product as Perplexity
from Copilot import svg_dot_product as Copilot
from CodeLLama import svg_dot_product as CodeLLama
from Claude import svg_dot_product as Claude
from ChatGPT import svg_dot_product as ChatGPT
from Bard import svg_dot_product as Bard

# Define the implementations with their names
implementations = [
    (Perplexity, 'Perplexity'),
    (Copilot, 'Copilot'),
    (CodeLLama, 'CodeLLama'),
    (Claude, 'Claude'),
    (ChatGPT, 'ChatGPT'),
    (Bard, 'Bard')
]

# SVG relative file path
svg_file_path = os.path.join(os.path.dirname(__file__), "test.svg")

# Define the expected results
dot_product = 32

@pytest.fixture(params=implementations, ids=[impl[1] for impl in implementations])
def implementation(request):
    impl, _ = request.param
    return impl

def test_svg_dot_product(implementation):
    # Call the implementation to get the result dot product of the given path
    result = implementation(svg_file_path)
    # Check the result
    try:
        assert result == dot_product, (
            f"Test failed for {implementation.__name__}. "
            f"Expected dot product: {dot_product}, got: {result}"
        )
    except AssertionError as ae:
        print(f"Test failed for {implementation.__name__}. Output dot product: {result}")
        raise ae
    except Exception as e:  
        pytest.fail(f"An error occurred during testing: {str(e)}")

# To execute this test, run the following command:
# pytest -v -s F:\TFG\TDD_Can_LLM_Code_unit_tests\Unit_tests_python\EX-05-svg_vector_metadata\svg_dot_product_test.py
