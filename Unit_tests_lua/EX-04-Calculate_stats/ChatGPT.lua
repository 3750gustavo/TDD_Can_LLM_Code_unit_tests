-- Function to calculate mean and standard deviation
function calculate_stats(list1, list2, list3)
    -- Function to calculate mean of a list
    local function mean(list)
        local sum = 0
        for _, v in ipairs(list) do
            sum = sum + v
        end
        return sum / #list
    end
    
    -- Function to calculate standard deviation of a list
    local function stddev(list)
        local m = mean(list)
        local sum_squared_diff = 0
        for _, v in ipairs(list) do
            sum_squared_diff = sum_squared_diff + (v - m)^2
        end
        return math.sqrt(sum_squared_diff / #list)
    end
    
    -- Calculate mean and standard deviation for each list
    local stats = {}
    stats['mean'] = {mean(list1), mean(list2), mean(list3)}
    stats['stddev'] = {stddev(list1), stddev(list2), stddev(list3)}
    
    return stats
end

-- Test the function
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
-- lua "Unit_tests_lua/EX-04-Calculate_stats/ChatGPT.lua" 