import numpy as np

def calculate_stats(list1, list2, list3):
    """
    Calculate the mean and standard deviation for each list of numbers.

    Args:
        list1, list2, list3: Lists of numbers.

    Returns:
        A dictionary with keys 'mean' and 'stddev' containing the mean and standard deviation for each list.
    """
    means = [np.mean(list1), np.mean(list2), np.mean(list3)]
    stddevs = [np.std(list1), np.std(list2), np.std(list3)]
    return {'mean': means, 'stddev': stddevs}