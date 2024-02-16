-- Import necessary math functions
local math = require("math")

-- Function to calculate mean
local function mean(numbers)
    local sum = 0
    for _, num in ipairs(numbers) do
        sum = sum + num
    end
    return sum / #numbers
end

-- Function to calculate standard deviation
local function stddev(numbers, mean_value)
    local sum_deviation = 0
    for _, num in ipairs(numbers) do
        sum_deviation = sum_deviation + (num - mean_value) ^ 2
    end
    return math.sqrt(sum_deviation / #numbers)
end

-- Main function to calculate stats
local function calculate_stats(list1, list2, list3)
    local stats = {}

    -- Calculate mean and standard deviation for each list
    stats.mean = {mean(list1), mean(list2), mean(list3)}
    stats.stddev = {stddev(list1, stats.mean[1]), stddev(list2, stats.mean[2]), stddev(list3, stats.mean[3])}

    return stats
end