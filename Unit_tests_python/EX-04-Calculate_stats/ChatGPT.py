import statistics

def calculate_stats(list1, list2, list3):
    stats_dict = {}
    
    # Calculate mean and standard deviation for list1
    mean1 = statistics.mean(list1)
    stddev1 = statistics.stdev(list1)
    stats_dict['mean_list1'] = mean1
    stats_dict['stddev_list1'] = stddev1
    
    # Calculate mean and standard deviation for list2
    mean2 = statistics.mean(list2)
    stddev2 = statistics.stdev(list2)
    stats_dict['mean_list2'] = mean2
    stats_dict['stddev_list2'] = stddev2
    
    # Calculate mean and standard deviation for list3
    mean3 = statistics.mean(list3)
    stddev3 = statistics.stdev(list3)
    stats_dict['mean_list3'] = mean3
    stats_dict['stddev_list3'] = stddev3
    
    return stats_dict