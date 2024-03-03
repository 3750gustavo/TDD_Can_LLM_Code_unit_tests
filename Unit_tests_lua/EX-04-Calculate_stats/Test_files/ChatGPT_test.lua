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

-- Test cases implemented and working:
local list1 = {10,9,11,10,8,12,11,9,10,11}
local list2 = {3,9,11,10,8,12,11,9,10,23}
local list3 = {1,19,9,5,2,18,13,7,4,6}
local result = calculate_stats(list1, list2, list3)
-- Define the expected result table
local expected_results = {
    mean = {10.1, 10.6, 8.4},
    stddev = {1.1357816691601,4.7581509013481,6.0033324079215}
}

-- Compare the expected result with the actual result
local mean_passed = true
local stddev_passed = true

-- Test mean calculation
for i, v in ipairs(expected_results.mean) do
    if math.abs(result.mean[i] - v) >= 0.0001 then
        mean_passed = false
        break
    end
end

-- Test standard deviation calculation
for i, v in ipairs(expected_results.stddev) do
    if math.abs(result.stddev[i] - v) >= 0.0001 then
        stddev_passed = false
        break
    end
end

-- Print test results
if mean_passed then
    print("Test passed for mean")
else
    for i, v in ipairs(expected_results.mean) do
        print("Test failed for mean at index " .. i .. " - Expected: " .. v .. ", Got: " .. result.mean[i])
    end
end

if stddev_passed then
    print("Test passed for standard deviation")
else
    for i, v in ipairs(expected_results.stddev) do
        print("Test failed for stddev at index " .. i .. " - Expected: " .. v .. ", Got: " .. result.stddev[i])
    end
end

-- To run this code, you can use the following command:
-- lua "Unit_tests_lua\EX-04-Calculate_stats\Test_files\ChatGPT_test.lua" 