import statistics

def calculate_stats(list1, list2, list3):
    stats_dict = {}
    
    # Calculate mean and standard deviation for each list
    mean_list1 = statistics.mean(list1)
    stddev_list1 = statistics.stdev(list1)
    
    mean_list2 = statistics.mean(list2)
    stddev_list2 = statistics.stdev(list2)
    
    mean_list3 = statistics.mean(list3)
    stddev_list3 = statistics.stdev(list3)
    
    # Populate the dictionary with calculated values
    stats_dict['mean'] = [mean_list1, mean_list2, mean_list3]
    stats_dict['stddev'] = [stddev_list1, stddev_list2, stddev_list3]
    
    return stats_dict