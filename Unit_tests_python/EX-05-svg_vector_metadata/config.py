import os,random,glob
import xml.etree.ElementTree as ET
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

def generate_svg_with_vectors(n, file_path):
    # Define SVG structure
    svg = ET.Element("svg", xmlns="http://www.w3.org/2000/svg")
    metadata = ET.SubElement(svg, "metadata")
    
    # Generate two vectors with 'n' elements
    for _ in range(2):
        vector = ET.SubElement(metadata, "vector")
        vector_values = [str(random.uniform(-10, 10)) for _ in range(n)]
        vector.text = ",".join(vector_values)
    
    # Convert to string
    tree = ET.ElementTree(svg)
    tree.write(file_path)

def svg_generator():
    def generator(n):
        # Temporary SVG file path
        file_path = f"temp_vector_{n}.svg"
        # Generate SVG file with 'n' elements in each vector
        generate_svg_with_vectors(n, file_path)
        return file_path
    return generator

def cleanup_temp_svg():
    for svg_file in glob.glob("temp_vector_*.svg"):
        os.remove(svg_file)