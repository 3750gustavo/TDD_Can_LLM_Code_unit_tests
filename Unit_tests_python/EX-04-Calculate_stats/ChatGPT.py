import math

def calculate_stats(list1, list2, list3):
    def mean(data):
        return sum(data) / len(data)

    def stddev(data):
        mu = mean(data)
        variance = sum((x - mu) ** 2 for x in data) / len(data)
        return math.sqrt(variance)

    stats_dict = {}
    stats_dict['mean'] = {'list1': mean(list1), 'list2': mean(list2), 'list3': mean(list3)}
    stats_dict['stddev'] = {'list1': stddev(list1), 'list2': stddev(list2), 'list3': stddev(list3)}
    
    return stats_dict