from statistics import mean, stddev

def calculate_stats(list1, list2, list3):
    means = [mean(list1), mean(list2), mean(list3)]
    stddevs = [stddev(list1), stddev(list2), stddev(list3)]
    return {'mean': means, 'stddev': stddevs}