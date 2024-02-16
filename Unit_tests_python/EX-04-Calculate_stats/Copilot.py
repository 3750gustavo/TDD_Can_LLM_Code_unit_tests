import math

def calculate_stats(list1, list2, list3):
    stats = {}
    
    # Calculate mean
    mean1 = sum(list1) / len(list1)
    mean2 = sum(list2) / len(list2)
    mean3 = sum(list3) / len(list3)
    
    # Calculate standard deviation
    stddev1 = math.sqrt(sum((x - mean1) ** 2 for x in list1) / len(list1))
    stddev2 = math.sqrt(sum((x - mean2) ** 2 for x in list2) / len(list2))
    stddev3 = math.sqrt(sum((x - mean3) ** 2 for x in list3) / len(list3))
    
    # Add mean and standard deviation to dictionary
    stats['mean'] = [mean1, mean2, mean3]
    stats['stddev'] = [stddev1, stddev2, stddev3]
    
    return stats