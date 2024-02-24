-- Import the necessary modules
local math = require("math")

-- Function to calculate mean
local function calculate_mean(list)
    local sum = 0
    for _, value in ipairs(list) do
        sum = sum + value
    end
    return sum / #list
end

-- Function to calculate standard deviation
local function calculate_stddev(list, mean)
    local sum = 0
    for _, value in ipairs(list) do
        sum = sum + (value - mean) ^ 2
    end
    return math.sqrt(sum / #list)
end

-- Main function to calculate stats
local function calculate_stats(list1, list2, list3)
    local stats = {}
    stats.mean = {
        calculate_mean(list1),
        calculate_mean(list2),
        calculate_mean(list3)
    }
    stats.stddev = {
        calculate_stddev(list1, stats.mean[1]),
        calculate_stddev(list2, stats.mean[2]),
        calculate_stddev(list3, stats.mean[3])
    }
    return stats
end
    
return calculate_stats