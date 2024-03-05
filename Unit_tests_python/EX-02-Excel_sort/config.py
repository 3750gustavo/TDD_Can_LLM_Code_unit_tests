import random, string, os, pandas as pd,string, tempfile, big_o
from ChatGPT import excel_sort as ChatGPT
from CodeLLama import excel_sort as CodeLLama
from Bard import excel_sort as Bard
from Copilot import excel_sort as Copilot
from Claude import excel_sort as Claude
from Perplexity import excel_sort as Perplexity

# Define the implementations with their names
implementations = [
    (ChatGPT, 'ChatGPT'),
    (CodeLLama, 'CodeLLama'),
    (Bard, 'Bard'),
    (Copilot, 'Copilot'),
    (Claude, 'Claude'),
    (Perplexity, 'Perplexity')
]

def get_implementations():
    return implementations

def generate_random_string(n):
    return ''.join(random.choice(string.ascii_letters) for _ in range(n))

def string_generator():
    '''Big O generator for generating strings of length n'''
    return lambda n: generate_random_string(n)

def random_string(length=10):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(length))

def generate_random_dataframe(rows=100, columns=5):
    data = {'col_{}'.format(i): [random_string() for _ in range(rows)] for i in range(columns)}
    df = pd.DataFrame(data)
    return df

def dataframe_generator():
    '''Big O generator for generating dataframes with lambda with n rows and 5 columns and returning its path'''
    def generate(n):
        df = generate_random_dataframe(n)
        file_path = os.path.join(os.path.dirname(__file__), 'temp.xlsx')
        if os.path.exists(file_path):
            os.remove(file_path)
        df.to_excel(file_path, index=False)
        print(f"Generated file with {n} rows")
        return file_path
    return lambda n: generate(n)

def generate_random_excel_file(rows=100, columns=5):
    '''Generate a random Excel file with the given number of rows and columns for testing.'''
    # Generate a random DataFrame
    df = generate_random_dataframe(rows, columns)

    # Save the DataFrame as an Excel file
    file_path = os.path.join(os.path.dirname(__file__), f'temp_{rows}.xlsx')
    if os.path.exists(file_path):
        os.remove(file_path)
    df.to_excel(file_path, index=False)

    return file_path