local function display_text_file(file_path)
    -- Read the content of the provided .txt file
    local file = io.open(file_path, "r")
    if not file then
        print("Error: File not found")
        return false, nil
    end
    local content = file:read("*all")
    file:close()

    -- Parse the data into name-value pairs
    local data = {}
    for line in content:gmatch("[^\r\n]+") do
        local name, value = line:match("(.-):(.+)")
        if name and value then
            table.insert(data, {name = name, value = tonumber(value)})
        end
    end

    -- Sort the list of dictionaries in descending order based on the 'value' key
    table.sort(data, function(a, b)
        return a.value > b.value
    end)

    -- Create or overwrite the temporary .txt file
    local temp_file_path = "test.txt"
    local temp_file = io.open(temp_file_path, "w")
    if not temp_file then
        print("Error: Failed to create temporary file")
        return false, nil
    end
    for _, entry in ipairs(data) do
        temp_file:write(entry.name .. ":" .. entry.value .. "\n")
    end
    temp_file:close()

    -- Display the contents of the temporary .txt file in a window GUI
    -- (Code for displaying GUI is not provided as it depends on the specific Lua GUI library being used)

    -- Return the result
    return true, temp_file_path
end

-- Add LuaRocks paths
local user = "gusta"
package.path = package.path .. ";C:/Users/" .. user .. "/AppData/Roaming/luarocks/share/lua/5.4/?.lua"
package.cpath = package.cpath .. ";C:/Users/" .. user .. "/AppData/Roaming/luarocks/lib/lua/5.4/?.dll"
local lfs = require("lfs")

-- Test Case 1: Create test file with valid data and assess the function's return values (success = true, temp_file_path = valid)
local function test_case_1()
    local test_file_path = "test.txt"
    local file = io.open(test_file_path, "w")
    file:write("Leo: 10\nJoana: 20\nThomas: 15\n")
    file:close()
    local success, temp_file_path = display_text_file(test_file_path)
    if not success then
        print("Test 1: Failed - Expected success: true, got: false")
        return false
    end
    if not lfs.attributes(temp_file_path) then
        print("Test 1: Failed - Expected file path: ", temp_file_path, ", got: nil")
        return false
    end
    print("Test 1: Passed - Operation successful")
    return true
end

-- Test Case 2: Verify that the function returns false and nil for a non-existent file
local function test_case_2()
    local non_existent_file_path = "non_existent.txt"
    local success, temp_file_path = display_text_file(non_existent_file_path)
    if success then
        print("Test 2: Failed - Expected success: false, got: true")
        return false
    end
    if temp_file_path ~= nil then
        print("Test 2: Failed - Expected file path: nil, got: ", temp_file_path)
        return false
    end
    print("Test 2: Passed")
    return true
end

-- Test Case 3: Verify that values are correctly sorted in descending order
local function test_case_3()
    local test_file_path = "test_sorting.txt"
    local file = io.open(test_file_path, "w")
    file:write("Last: 10\nFirst: 20\nSecond: 15\n")
    file:close()
    local success, temp_file_path = display_text_file(test_file_path)
    local expected_sorted_data = { { "First", 20 }, { "Second", 15 }, { "Last", 10 } }
    if not success then
        print("Test 3: Failed - Expected success: true, got: false")
        return false
    end
    if not lfs.attributes(temp_file_path) then
        print("Test 3: Failed - Expected file path: ", temp_file_path, ", got: nil")
        return false
    end
    file = io.open(temp_file_path, "r")
    local content = file:read("*all")
    file:close()
    local lines = {}
    for line in content:gmatch("[^\n]+") do
        table.insert(lines, line)
    end
    if #lines ~= 3 then
        print("Test 3: Failed - Expected 3 lines, got: ", #lines)
        return false
    end
    local data = {}
    for _, line in ipairs(lines) do
        local name, value = line:match("([^:]+):([^:]+)")
        table.insert(data, { name, tonumber(value) })
    end
    -- Custom function to compare the contents of the tables
    local function compare_tables(t1, t2)
        if #t1 ~= #t2 then
            return false
        end
        for i = 1, #t1 do
            if t1[i][1] ~= t2[i][1] or t1[i][2] ~= t2[i][2] then
                return false
            end
        end
        return true
    end
    if compare_tables(data, expected_sorted_data) then
        print("Test 3: Passed - Name-value pairs are sorted in descending order")
        return true
    else
        print("Test 3: Failed - Expected: ", expected_sorted_data, ", got: ", data)
        return false
    end
end

-- Performance test (optional)
local file_path_performance_test_file = [[F:\TFG\TDD_Can_LLM_Code_unit_tests\Unit_tests_lua\EX-06-display_text_file_gui\tests\test.txt]]
local function performance_test(num_iterations)
    -- warm-up
    for i = 1, 50 do
        display_text_file(file_path_performance_test_file)
    end
    -- Actual test
    local start_time = os.clock()
    for i = 1, num_iterations do
        display_text_file(file_path_performance_test_file)
    end
    local end_time = os.clock()
    -- Calculate average runtime in milliseconds
    local elapsed_time = end_time - start_time
    local avg_time_per_iteration = elapsed_time / num_iterations * 1000
    print("Performance test results:")
    print("Number of iterations: ", num_iterations)
    print("Average time per iteration: ", avg_time_per_iteration, " ms")
end

-- Run the tests and store the results
local test1_result = test_case_1()
local test2_result = test_case_2()
local test3_result = test_case_3()

-- Print the summary
print("Summary:")
print("Test 1: ", test1_result and "Passed" or "Failed")
print("Test 2: ", test2_result and "Passed" or "Failed")
print("Test 3: ", test3_result and "Passed" or "Failed")
-- Run the performance test
io.write("Do you want to run the performance test? (y/n): ")
local run_performance_test = io.read()
if run_performance_test == "y" then
    performance_test(1000)
end

-- To run this code, you can use the following command:
-- lua "Unit_tests_lua\EX-06-display_text_file_gui\tests\Copilot_test.lua"