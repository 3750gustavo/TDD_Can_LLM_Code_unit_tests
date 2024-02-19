import xml.etree.ElementTree as ET
import re
import math

def svg_dot_product(svg_file_path):
    # Parse the SVG file
    try:
        tree = ET.parse(svg_file_path)
    except:
        return -1
    
    # Find the metadata element
    metadata = tree.find('{http://www.w3.org/2000/svg}metadata')
    if metadata is None:
        return -1
    
    # Extract the vectors from the metadata
    vectors = re.findall(r'<vector x="(\d+)" y="(\d+)" />', metadata.text)
    if len(vectors) != 2:
        return -1
    
    # Calculate the dot product of the vectors
    dot_product = 0
    for i in range(2):
        dot_product += int(vectors[0][i]) * int(vectors[1][i])
    
    return dot_product