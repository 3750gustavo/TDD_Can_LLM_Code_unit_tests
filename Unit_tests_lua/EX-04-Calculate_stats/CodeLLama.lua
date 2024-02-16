import math

def calculate_stats(list1, list2, list3):
    mean_list = [math.mean(list1), math.mean(list2), math.mean(list3)]
    stddev_list = [math.stddev(list1), math.stddev(list2), math.stddev(list3)]
    return {'mean': mean_list, 'stddev': stddev_list}