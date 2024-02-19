import statistics

def calculate_stats(list1, list2, list3):
    mean1 = statistics.mean(list1)
    mean2 = statistics.mean(list2) 
    mean3 = statistics.mean(list3)
    
    stddev1 = statistics.pstdev(list1)
    stddev2 = statistics.pstdev(list2)
    stddev3 = statistics.pstdev(list3)
    
    means = [mean1, mean2, mean3]
    stddevs = [stddev1, stddev2, stddev3]
    
    stats = {'mean': means, 'stddev': stddevs}
    return stats