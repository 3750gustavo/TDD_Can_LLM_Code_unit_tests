import pytest
import os
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