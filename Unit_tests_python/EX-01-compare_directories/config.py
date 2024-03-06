import os,datetime,subprocess
try:
    from pyfakefs.fake_filesystem_unittest import Patcher
except ImportError:
    subprocess.run(['pip', 'install', 'pyfakefs'])
    from pyfakefs.fake_filesystem_unittest import Patcher
# Import implementations
from Copilot import compare_directories as Copilot
from ChatGPT import compare_directories as ChatGPT
from CodeLLama import compare_directories as CodeLLama
from Bard import compare_directories as Bard
from Claude import compare_directories as Claude
# from Perplexity import compare_directories as Perplexity

# Define the implementations with their names
implementations = [
    (Copilot, 'Copilot'),
    (ChatGPT, 'ChatGPT'),
    (CodeLLama, 'CodeLLama'),
    (Bard, 'Bard'),
    (Claude, 'Claude')
    # (Perplexity, 'Perplexity')
]

# Folders paths
dir1 = os.path.join(os.getcwd(), 'test_folder1')
dir2 = os.path.join(os.getcwd(), 'test_folder2')

def get_implementations():
    return implementations

def get_folders_paths():
    '''Return the paths of the two folders'''
    return dir1, dir2

# Function to set the modification date of a file
def set_date(file_path,date=datetime.datetime(2021, 1, 1)):
    os.utime(file_path, (date.timestamp(), date.timestamp()))

# Function to create files in the folders, all with the same modification dates of 2021-01-01
def create_files_all_same_date(dir1=dir1, dir2=dir2):
    for i in range(5):
        file_content = f'This is file {i} content'
        modification_time = datetime.datetime(2021, 1, 1)
        for directory in [dir1, dir2]:
            file_path = os.path.join(directory, f'file{i}.txt')
            with open(file_path, 'w') as file:
                file.write(file_content)
            # Set modification date to 2021-01-01
            set_date(file_path)

# Function to create files in the folders with some differences
def create_files_with_differences(dir1=dir1, dir2=dir2):
    # Create two files with the same content and modification date in both folders
    for i in range(2):
        file_content = f'This is file {i} content'
        modification_time = datetime.datetime(2021, 1, 1)
        for directory in [dir1, dir2]:
            file_path = os.path.join(directory, f'file{i}.txt')
            with open(file_path, 'w') as file:
                file.write(file_content)
            # Set modification date to 2021-01-01
            set_date(file_path)
    # Create two files with same content but different modification date in both folders (current date in dir2)
    for i in range(2, 4):
        # same content for both files
        file_content = f'This is file {i} content'
        # base modification date
        modification_time = datetime.datetime(2021, 1, 1)
        # create file in dir1
        file_path = os.path.join(dir1, f'file{i}.txt')
        with open(file_path, 'w') as file:
            file.write(file_content)
        # Set modification date to 2021-01-01
        set_date(file_path)
        # create file in dir2
        file_path = os.path.join(dir2, f'file{i}.txt')
        with open(file_path, 'w') as file:
            file.write(file_content)
        
    # Create one additional file in dir2
    additional_file_content = "This is file 5 content"
    additional_file_path = os.path.join(dir2, 'file5.txt')
    with open(additional_file_path, 'w') as file:
        file.write(additional_file_content)
    # Set modification date to 2021-01-01
    set_date(additional_file_path)

# Function to delete all files from the folders
def delete_files(dir1=dir1, dir2=dir2):
    for directory in [dir1, dir2]:
        for filename in os.listdir(directory):
            file_path = os.path.join(directory, filename)
            os.remove(file_path)

def check_make_dirs(dir1=dir1, dir2=dir2):
    for directory in [dir1, dir2]:
        if not os.path.exists(directory):
            os.makedirs(directory)

def setup_folders(dir1=dir1, dir2=dir2):
    '''Create the folders if they do not exist and create the files inside them'''
    check_make_dirs()
    create_files_all_same_date()
    create_files_with_differences()
    # returns false if the folders any folder is empty at the end of the setup
    return not (not os.listdir(dir1) or not os.listdir(dir2))

def reset_folders(dir1=dir1, dir2=dir2):
    '''Delete all files from the folders'''
    delete_files()

def generate_big_o_test_folders_n():
    '''Generate two folders with n files each with half same date and half different date using pyfakefs'''
    
    def generate(n):
        with Patcher() as patcher:
            # Create directories in the fake file system
            patcher.fs.create_dir(dir1)
            patcher.fs.create_dir(dir2)
            
            for i in range(n):
                file_content = f'This is file {i} content'
                for directory in [dir1, dir2]:
                    file_path = os.path.join(directory, f'file{i}.txt')
                    # Use pyfakefs to create and write to the file
                    patcher.fs.create_file(file_path, contents=file_content)
                    # Simulate setting the modification date to 2021-01-01
                    set_date(file_path, datetime.datetime(2021, 1, 1))
            
            for i in range(n // 2, n):
                file_content = f'This is file {i} content'
                for directory in [dir1, dir2]:
                    file_path = os.path.join(directory, f'file{i}.txt')
                    # Files are already created, just updating content for demonstration
                    patcher.fs.create_file(file_path, contents=file_content, modify=True)
                    # For dir2, simulate a different modification date if necessary

    return lambda n: generate(n)