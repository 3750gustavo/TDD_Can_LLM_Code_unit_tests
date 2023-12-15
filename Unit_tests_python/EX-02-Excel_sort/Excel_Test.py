import tempfile
import pandas as pd
import os
import pytest
from pathlib import Path
from ChatGPT import excel_sort as ChatGPT
from CodeLLama import excel_sort as CodeLLama
from Bard import excel_sort as Bard

implementations = [ChatGPT, CodeLLama, Bard]

@pytest.fixture(params=implementations, ids=[impl.__name__ for impl in implementations])
def implementation(request):
    return request.param

@pytest.fixture
def file_path():
    return os.path.join(os.path.dirname(__file__), 'GPUs.xlsx')

def test_excel_sort(implementation, file_path):
    column_index = 1
    try:
        result = implementation(file_path, column_index)

        if isinstance(result, str) and Path(result).suffix == '.xlsx':
            df_temp = pd.read_excel(result)
        elif isinstance(result, bytes):
            with tempfile.NamedTemporaryFile(suffix='.xlsx', delete=True) as temp:
                temp.write(result)
                temp.seek(0)
                df_temp = pd.read_excel(temp.name)
        else:
            pytest.fail(f"Invalid return type from {implementation.__name__}")

        assert df_temp.iloc[:, column_index].is_monotonic_decreasing, \
            f"DataFrame is not sorted correctly in {implementation.__name__}"
    except Exception as e:
        pytest.fail(f"Test failed for {implementation.__name__}: {str(e)}")

if __name__ == "__main__":
    pytest.main()