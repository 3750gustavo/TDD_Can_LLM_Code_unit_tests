import os
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
    '''Ensure the folders exist and return their paths'''
    for directory in [dir1, dir2]:
        if not os.path.exists(directory):
            os.makedirs(directory)
    return dir1, dir2