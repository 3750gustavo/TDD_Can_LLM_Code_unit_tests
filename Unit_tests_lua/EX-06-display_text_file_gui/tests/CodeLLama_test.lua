local function display_text_file(file_path)
    -- Check if the file exists
    if not file_path or not file_path:is_file() then
      return false, nil, "File does not exist"
    end
  
    -- Read the content of the file
    local file = io.open(file_path, "r")
    local content = file:read("*a")
    file:close()
  
    -- Parse the content into name-value pairs
    local name_value_pairs = {}
    for line in content:gmatch("([^:]+):([^:]+)") do
      name_value_pairs[line[1]] = line[2]
    end
  
    -- Sort the name-value pairs in descending order based on the 'value' key
    table.sort(name_value_pairs, function(a, b) return a.value > b.value end)
  
    -- Check if the temporary file exists
    local temp_file_path = "test.txt"
    if not temp_file_path:is_file() then
      -- Create a temporary file
      local temp_file = io.open(temp_file_path, "w")
      temp_file:write(table.concat(name_value_pairs, "\n"))
      temp_file:close()
    else
      -- Overwrite the temporary file
      local temp_file = io.open(temp_file_path, "w")
      temp_file:write(table.concat(name_value_pairs, "\n"))
      temp_file:close()
    end
  
    -- Display the contents of the temporary file in a window GUI
    local window = display.newWindow("Text File Viewer")
    window:setSize(800, 600)
    window:setPosition(display.getCenter())
    window:setBackgroundColor(0xFF, 0xFF, 0xFF)
    window:setTitle("Text File Viewer")
  
    local text_view = display.newText(name_value_pairs, 10, 10, 780, 580)
    text_view:setFontSize(14)
    text_view:setFontColor(0x00, 0x00, 0x00)
    text_view:setBackgroundColor(0xFF, 0xFF, 0xFF)
    text_view:setPosition(10, 10)
    window:addChild(text_view)
  
    -- Return a tuple containing a boolean value indicating whether the operation was successful and the absolute path to the temporary .txt file
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
-- lua "Unit_tests_lua\EX-06-display_text_file_gui\tests\CodeLLama_test.lua"