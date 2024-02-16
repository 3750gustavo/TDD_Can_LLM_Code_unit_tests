import math

def calculate_stats(list1, list2, list3):
    mean_list = [sum(list1) / len(list1), sum(list2) / len(list2), sum(list3) / len(list3)]
    stddev_list = [math.sqrt(sum((x - mean_list[0])**2 for x in list1) / len(list1)),
                   math.sqrt(sum((x - mean_list[1])**2 for x in list2) / len(list2)),
                   math.sqrt(sum((x - mean_list[2])**2 for x in list3) / len(list3))]
    return {'mean': mean_list, 'stddev': stddev_list}