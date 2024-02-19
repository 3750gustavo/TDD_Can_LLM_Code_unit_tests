import xml.etree.ElementTree as ET

def svg_dot_product(svg_file_path):
    # Parse the SVG file and extract the metadata
    tree = ET.parse(svg_file_path)
    root = tree.getroot()
    metadata = root.find('metadata')

    # Check if the metadata contains vectors
    if metadata is None or not metadata.find('vectors'):
        return -1

    # Extract the vectors from the metadata
    vectors = metadata.find('vectors').text.split(',')

    # Calculate the dot product of the vectors
    dot_product = 0
    for vector in vectors:
        dot_product += float(vector)

    return dot_product