-- Import the math library for mathematical functions
require("math")

-- Define the calculate_stats function
function calculate_stats(list1, list2, list3)
    -- Function to calculate the mean of a list
    local function mean(list)
        local sum = 0
        for i = 1, #list do
            sum = sum + list[i]
        end
        return sum / #list
    end

    -- Function to calculate the standard deviation of a list
    local function stddev(list)
        local m = mean(list)
        local sum_squares = 0
        for i = 1, #list do
            sum_squares = sum_squares + (list[i] - m) ^ 2
        end
        return math.sqrt(sum_squares / #list)
    end

    -- Calculate the mean and standard deviation for each list
    local stats = {
        {
            mean(list1),
            stddev(list1)
        },
        {
            mean(list2),
            stddev(list2)
        },
        {
            mean(list3),
            stddev(list3)
        }
    }

    -- Return the calculated statistics as a dictionary
    return {
        mean = {stats[1][1], stats[2][1], stats[3][1]},
        stddev = {stats[1][2], stats[2][2], stats[3][2]}
    }
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

-- Performance related tests:

-- warm up the function to get a more accurate performance benchmark
    for i=1,1000 do
        calculate_stats(list1, list2, list3)
    end
    -- avg performance benchmark for 100k iterations (in milliseconds)
    -- execute the performance test 5 times to be sure and avg the averages
    local results = {}
    for j=1,5 do
        local start = os.clock()
        for i=1,100000 do
            calculate_stats(list1, list2, list3)
        end
        local elapsed = os.clock() - start
        local avg = elapsed * 1000 / 100000
        table.insert(results, avg)
    end
    -- calculate the average of the averages
    local avg = 0
    for i, v in ipairs(results) do
        avg = avg + v
    end
    avg = avg / #results
    print("Average time for 100k iterations: " .. avg .. "ms")

-- To run this code, you can use the following command:
-- lua "Unit_tests_lua\EX-04-Calculate_stats\Test_files\Perplexity_test.lua"