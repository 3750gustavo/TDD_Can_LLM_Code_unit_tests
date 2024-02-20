import xml.etree.ElementTree as ET

def svg_dot_product(svg_file_path):
    tree = ET.parse(svg_file_path)
    root = tree.getroot()
    metadata = root.find('metadata')
    vectors = metadata.findall('vector')
    if len(vectors) < 2:
        return -1
    vector1 = vectors[0].text.split(',')
    vector2 = vectors[1].text.split(',')
    dot_product = 0
    for i in range(len(vector1)):
        dot_product += int(vector1[i]) * int(vector2[i])
    return dot_product