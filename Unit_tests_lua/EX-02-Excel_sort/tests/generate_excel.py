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
    
def calculate_expected_results(file_path, column_index):
    try:
        # Read the data from the Excel file
        data = pd.read_excel(file_path)
        # Sort the data by the column at the given index
        sorted_data = data.sort_values(by=data.columns[column_index])
        return sorted_data
    except Exception as e:
        print(f"An error occurred during calculating the expected results: {str(e)}")

def main():
    # Change the current working directory
    os.chdir(r'F:\TFG\TDD_Can_LLM_Code_unit_tests\Unit_tests_lua\EX-02-Excel_sort\tests')

    print("Current working directory:", os.getcwd())
    # generate excel and save it on disk
    file_path = generate_excel()
    print("Excel file generated at:", file_path)
    extras = input('Do you want to calculate the expected results for the generated excel file? y or n: ')
    if extras.lower() == 'y':
        results = []
        for column_index in range(3):  # Assuming you want to sort by the first three columns
            sorted_data = calculate_expected_results(file_path, column_index)
            results.append(sorted_data)
        
        texts = []
        for i, result in enumerate(results):
            text = f'For column {i+1}:\n{result}'
            print(text)
            texts.append(text)
        
        with open('expected_results.txt', 'w') as file:
            file.write('\n'.join(texts))

if __name__ == "__main__":
    main()