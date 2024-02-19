import numpy as np

def calculate_stats(lists_of_numbers):
    stats_dict = {}

    for list_of_numbers in lists_of_numbers:
        mean = np.mean(list_of_numbers)
        variance = np.var(list_of_numbers, ddof=0)  # Population standard deviation formula
        stddev = np.sqrt(variance)

        stats_dict[f'mean_{list_of_numbers[0]}'] = [mean]
        stats_dict[f'stddev_{list_of_numbers[0]}'] = [stddev]

    return stats_dict