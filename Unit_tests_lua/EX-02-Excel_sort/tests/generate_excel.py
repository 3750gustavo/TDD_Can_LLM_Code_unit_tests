'''Generates a static excel file for testing purposes with predifined data'''
import pandas as pd
import os

def generate_excel():
    try:
        # Create a DataFrame
        data = {
            'Name': ['Tom', 'Jerry', 'Mickey', 'Minnie', 'Donald', 'Daffy'],
            'Age': [20, 21, 19, 20, 22, 21],
            'City': ['New York', 'Los Angeles', 'San Francisco', 'Chicago', 'Houston', 'Phoenix']
        }
        df = pd.DataFrame(data)

        # Save the DataFrame as an Excel file
        file_path = os.path.join(os.getcwd(), "test.xlsx")
        df.to_excel(file_path, index=False)

        return file_path
    except Exception as e:
        print(f"An error occurred during generating the excel: {str(e)}")
        return None

def main():
    # Change the current working directory
    os.chdir(r'F:\TFG\TDD_Can_LLM_Code_unit_tests\Unit_tests_lua\EX-02-Excel_sort\tests')

    print("Current working directory:", os.getcwd())
    # generate excel and save it on disk
    file_path = generate_excel()
    print("Excel file generated at:", file_path)


if __name__ == "__main__":
    main()