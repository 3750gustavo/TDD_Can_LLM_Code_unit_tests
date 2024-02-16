import math

def calculate_stats(list1, list2, list3):
    mean1 = sum(list1) / len(list1)
    mean2 = sum(list2) / len(list2)
    mean3 = sum(list3) / len(list3)
    stddev1 = math.sqrt(sum((x - mean1)**2 for x in list1) / len(list1))
    stddev2 = math.sqrt(sum((x - mean2)**2 for x in list2) / len(list2))
    stddev3 = math.sqrt(sum((x - mean3)**2 for x in list3) / len(list3))
    return {'mean': [mean1, mean2, mean3], 'stddev': [stddev1, stddev2, stddev3]}