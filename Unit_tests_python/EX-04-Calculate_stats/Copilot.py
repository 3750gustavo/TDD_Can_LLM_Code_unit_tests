import statistics

def calculate_stats(list1, list2, list3):
    stats = {}
    stats['mean'] = [statistics.mean(list1), statistics.mean(list2), statistics.mean(list3)]
    stats['stddev'] = [statistics.stdev(list1), statistics.stdev(list2), statistics.stdev(list3)]
    return stats