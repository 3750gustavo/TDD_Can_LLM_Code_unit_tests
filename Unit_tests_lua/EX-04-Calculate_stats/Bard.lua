-- Import the math library for calculations
local math = require("math")

-- Function to calculate mean and standard deviation using population formula
function calculate_stats(list1, list2, list3)
  -- Initialize variables for means and standard deviations
  local means = {}
  local stddevs = {}

  -- Calculate mean and standard deviation for each list
  for i, list in ipairs({list1, list2, list3}) do
    -- Calculate the mean
    local mean = 0
    for _, value in ipairs(list) do
      mean = mean + value
    end
    mean = mean / #list

    -- Calculate the variance (using population standard deviation formula)
    local variance = 0
    for _, value in ipairs(list) do
      local deviation = value - mean
      variance = variance + deviation * deviation
    end
    variance = variance / #list

    -- Calculate the standard deviation (square root of variance)
    local stddev = math.sqrt(variance)

    -- Store the mean and standard deviation for the current list
    means[i] = mean
    stddevs[i] = stddev
  end

  -- Return the results as a dictionary
  return {
    mean = means,
    stddev = stddevs
  }
end