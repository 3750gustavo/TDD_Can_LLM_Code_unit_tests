-- Import the necessary libraries
local math = require("math")

-- Define the function
local function calculate_stats(list1, list2, list3)
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

-- Test cases implemented and failed
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
-- lua "Unit_tests_lua/EX-04-Calculate_stats/Test_files/CodeLLama_test.lua"