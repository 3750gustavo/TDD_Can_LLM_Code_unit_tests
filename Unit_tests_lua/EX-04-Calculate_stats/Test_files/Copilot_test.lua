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
-- Test cases implemented and working:
    local list1 = {10,9,11,10,8,12,11,9,10,11}
    local list2 = {3,9,11,10,8,12,11,9,10,23}
    local list3 = {1,19,9,5,2,18,13,7,4,6}
    local result = calculate_stats(list1, list2, list3)
    
    -- Define the expected result table
    local expected_result = {
        mean = {10.1, 10.6, 8.4},
        stddev = {1.1357816691601,4.7581509013481,6.0033324079215}
    }
    
    -- Compare the expected result with the actual result
    for key, value in pairs(expected_result) do
        for i, v in ipairs(value) do
            if key == 'stddev' then
                local margin_of_error = 0.0001
                if math.abs(result[key][i] - v) <= margin_of_error then
                    print("Test passed for", key, "at index", i)
                else
                    print("Test failed for", key, "at index", i, "- Expected:", v, "Got:", result[key][i])
                end
            else
                if result[key][i] == v then
                    print("Test passed for", key, "at index", i)
                else
                    print("Test failed for", key, "at index", i, "- Expected:", v, "Got:", result[key][i])
                end
            end
        end
    end
    
    -- Print the result
    print("Mean:", table.unpack(result['mean']))
    print("Standard Deviation:", table.unpack(result['stddev']))
    
    -- To run this code, you can use the following command:
    -- lua "Unit_tests_lua/EX-04-Calculate_stats/Copilot.lua"
    
return calculate_stats