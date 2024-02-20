import xml.etree.ElementTree as ET
import numpy as np

def svg_dot_product(svg_path):
    try:
        tree = ET.parse(svg_path)
        root = tree.getroot()
        metadata = root.find('{http://www.w3.org/2000/svg}metadata')
        if metadata is None:
            return -1
        
        vectors = metadata.findall('{http://www.w3.org/2000/svg}vector')
        if len(vectors) < 2:
            return -1
        
        vec1 = [float(x) for x in vectors[0].text.split(',')] 
        vec2 = [float(x) for x in vectors[1].text.split(',')]
        
        return np.dot(vec1, vec2)
        
    except:
        return -1