-- Import the necessary libraries
local math = require("math")

-- Define the function
function calculate_stats(list1, list2, list3)
  -- Calculate the mean for each list
  local mean1 = math.mean(list1)
  local mean2 = math.mean(list2)
  local mean3 = math.mean(list3)

  -- Calculate the standard deviation for each list
  local stddev1 = math.stddev(list1, mean1)
  local stddev2 = math.stddev(list2, mean2)
  local stddev3 = math.stddev(list3, mean3)

  -- Return the mean and standard deviation values as a dictionary
  return {
    mean = {mean1, mean2, mean3},
    stddev = {stddev1, stddev2, stddev3}
  }
end