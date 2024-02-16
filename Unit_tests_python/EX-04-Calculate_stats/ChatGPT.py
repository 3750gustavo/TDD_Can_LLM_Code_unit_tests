import math

def calculate_stats(list1, list2, list3):
    def calculate_mean(data):
        return sum(data) / len(data)

    def calculate_stddev(data):
        mean = calculate_mean(data)
        variance = sum((x - mean) ** 2 for x in data) / len(data)
        stddev = math.sqrt(variance)
        return stddev

    stats_dict = {}
    stats_dict['mean'] = [calculate_mean(list1), calculate_mean(list2), calculate_mean(list3)]
    stats_dict['stddev'] = [calculate_stddev(list1), calculate_stddev(list2), calculate_stddev(list3)]
    
    return stats_dict