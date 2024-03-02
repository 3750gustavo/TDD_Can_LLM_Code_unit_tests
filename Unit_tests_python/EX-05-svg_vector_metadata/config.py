import os
# Import the implementations
from Perplexity import svg_dot_product as Perplexity
from Copilot import svg_dot_product as Copilot
from CodeLLama import svg_dot_product as CodeLLama
from Claude import svg_dot_product as Claude
from ChatGPT import svg_dot_product as ChatGPT
from Bard import svg_dot_product as Bard

# Define the implementations with their names
implementations = [
    (Perplexity, 'Perplexity'),
    (Copilot, 'Copilot'),
    (CodeLLama, 'CodeLLama'),
    (Claude, 'Claude'),
    (ChatGPT, 'ChatGPT'),
    (Bard, 'Bard')
]

# SVG relative file path
svg_file_path = os.path.join(os.path.dirname(__file__), "test.svg")

# Define the expected results
dot_product = 32

def get_implementations():
    return implementations

def get_svg_file_path():
    return svg_file_path