import statistics

def calculate_stats(list1, list2, list3):
    stats = {}
    stats['mean'] = [statistics.mean(list1), statistics.mean(list2), statistics.mean(list3)]
    stats['stddev'] = [statistics.pstdev(list1), statistics.pstdev(list2), statistics.pstdev(list3)]
    return stats