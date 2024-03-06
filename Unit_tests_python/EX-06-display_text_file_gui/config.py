import random, string, os,string
from CodeLLama import display_text_file as CodeLLama
from ChatGPT import display_text_file as ChatGPT
from Bard import display_text_file as Bard
from Claude import display_text_file as Claude
from Perplexity import display_text_file as Perplexity
from Copilot import display_text_file as Copilot

# Define the implementations with their names
implementations = [
    (CodeLLama, 'CodeLLama'),
    (ChatGPT, 'ChatGPT'),
    (Bard, 'Bard'),
    (Claude, 'Claude'),
    (Perplexity, 'Perplexity'),
    (Copilot, 'Copilot')
]

# Test .txt file path
txt_file_path = os.path.join(os.path.dirname(__file__), "test.txt")

def get_implementations():
    return implementations

def get_txt_file_path():
    return txt_file_path

def setup_txt_file():
    try:
        if not os.path.exists(txt_file_path):
            with open(txt_file_path, 'w') as file:
                file.write("Leo: 10\nJoana: 20\nThomas: 15\n")
        else:
            with open(txt_file_path, 'r+') as file:
                if file.read().strip() != "":
                    file.truncate(0)
                file.write("Leo: 10\nJoana: 20\nThomas: 15\n")
    except Exception as e:
        print(f"An error occurred while setting up the .txt file: {e}")
        return False
    return True

def generate_random_name():
    return ''.join(random.choice(string.ascii_letters) for _ in range(10))

def txt_file_generator():
    '''Big O generator for generating .txt files with n lines of text'''
    append = lambda n: generate_random_name() + ": " + str(random.randint(1, 100)) + "\n"
    def generate(n):
        with open(txt_file_path, 'w') as file:
            for _ in range(n):
                file.write(append(n))
    return generate

def cleanup_txt_file():
    try:
        if os.path.exists(txt_file_path):
            os.remove(txt_file_path)
    except Exception as e:
        print(f"An error occurred while cleaning up the .txt file: {e}")
        return False
    return True