import pytest
from Perplexity import svg_dot_product as Perplexity

# Define the implementations with their names
implementations = [
    (Perplexity, 'Perplexity')
]

# SVG relative file path
svg_file_path = 'vector.svg'

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
