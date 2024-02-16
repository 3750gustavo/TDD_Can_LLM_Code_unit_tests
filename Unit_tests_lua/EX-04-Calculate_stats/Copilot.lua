-- Import the necessary modules
local math = require("math")

-- Function to calculate mean
local function calculate_mean(numbers)
    local sum = 0
    for _, num in ipairs(numbers) do
        sum = sum + num
    end
    return sum / #numbers
end

-- Function to calculate standard deviation
local function calculate_stddev(numbers, mean)
    local sum = 0
    for _, num in ipairs(numbers) do
        sum = sum + (num - mean) ^ 2
    end
    return math.sqrt(sum / #numbers)
end

-- Main function to calculate stats
local function calculate_stats(list1, list2, list3)
    local stats = {}
    stats.mean = {}
    stats.stddev = {}

    -- Calculate mean and standard deviation for each list
    stats.mean[1] = calculate_mean(list1)
    stats.mean[2] = calculate_mean(list2)
    stats.mean[3] = calculate_mean(list3)

    stats.stddev[1] = calculate_stddev(list1, stats.mean[1])
    stats.stddev[2] = calculate_stddev(list2, stats.mean[2])
    stats.stddev[3] = calculate_stddev(list3, stats.mean[3])

    return stats
end

return calculate_stats
