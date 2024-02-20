import xml.etree.ElementTree as ET

def svg_dot_product(file_path):
    try:
        tree = ET.parse(file_path)
        root = tree.getroot()
        
        metadata = root.find("{http://www.w3.org/2000/svg}metadata")
        vectors = metadata.findall("{http://www.w3.org/2000/svg}vector")
        
        if len(vectors) < 2:
            return -1
        
        vector1 = vectors[0].text
        vector2 = vectors[1].text
        
        vector1_values = [float(value) for value in vector1.split(",")]
        vector2_values = [float(value) for value in vector2.split(",")]
        
        dot_product = sum(a * b for a, b in zip(vector1_values, vector2_values))
        
        return dot_product
    except:
        return -1