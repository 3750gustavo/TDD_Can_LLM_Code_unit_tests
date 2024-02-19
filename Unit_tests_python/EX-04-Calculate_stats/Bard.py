import numpy as np

def calculate_stats(list1, list2, list3):
  """
  Calculates the mean and standard deviation for three lists of numbers.

  Args:
      list1: The first list of numbers.
      list2: The second list of numbers.
      list3: The third list of numbers.

  Returns:
      A dictionary with two keys: 'mean' and 'stddev'. Each key corresponds to
      a list containing the mean and standard deviation values for the input lists,
      respectively.
  """

  stats = {}
  stats['mean'] = [np.mean(list1), np.mean(list2), np.mean(list3)]
  stats['stddev'] = [np.std(list1, ddof=1), np.std(list2, ddof=1), np.std(list3, ddof=1)]
  return stats