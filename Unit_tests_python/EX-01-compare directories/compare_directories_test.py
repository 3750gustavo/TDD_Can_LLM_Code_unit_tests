import pytest
import os

# import implementations
from Perplexity import compare_directories as Perplexity
from Copilot import compare_directories as Copilot

# Define the implementations with their names
implementations = [
    (Perplexity, 'Perplexity'),
    (Copilot, 'Copilot')
]

# Define the expected results


@pytest.fixture(params=implementations, ids=[impl[1] for impl in implementations])
def implementation(request):
    impl, _ = request.param
    return impl