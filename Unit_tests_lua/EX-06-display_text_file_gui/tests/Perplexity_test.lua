-- Add LuaRocks paths
local user = "gusta"
package.path = package.path .. ";C:/Users/" .. user .. "/AppData/Roaming/luarocks/share/lua/5.4/?.lua"
package.cpath = package.cpath .. ";C:/Users/" .. user .. "/AppData/Roaming/luarocks/lib/lua/5.4/?.dll"
local lfs = require("lfs")


local table_sort = table.sort
local json = require("json") -- For converting tables to JSON strings
local tween = require("hump.easing").linear -- Optional dependency for smooth animation (GUI)
local love = _G.love or nil -- Love2D framework (for creating GUI window)

-- Function to check if file exists
local function fileExists(path)
    local ok, err = pcall(function()
        io.open(path, "r")
    end)
    return ok and not err
end

-- Function to read text file and convert lines to name-value pairs
local function parseFileToDicts(filename)
    local dictList = {}
    
    for line in io.lines(filename) do -- Iterate through file lines
        local parts = string.split(line, ":", { plain = true }) -- Split at colon
        
        if #parts == 2 then -- Ensure two parts (key and value)
            table.insert(dictList, { name = parts[1], value = tonumber(parts[2]) or parts[2] }) -- Convert values to numbers when possible
        end
    end

    return dictList
end

-- Function to sort dictionary list by value
local function sortByValue(list)
    table_sort(list, function(a, b)
        return a.value > b.value
    end)
end

-- Function to write dictionary list to temp file
local function writeTempFile(tempFilename, dictList)
    local f = assert(io.open(tempFilename, "w")) -- Open or create temp file
    for _, dict in ipairs(dictList) do
        f:write(string.format("%s:%s\n", dict.name, dict.value)) -- Write each pair to file
    end
    f:close()
end

-- Main function
local function display_text_file(inputFilePath)
    local success, tempFileName = false, ""

    -- Check input file existence
    if not fileExists(inputFilePath) then
        print("Error: File '" .. inputFilePath .. "' does not exist.")
        return false, "", nil
    end

    -- Parse input file
    local dictList = parseFileToDicts(inputFilePath)
    sortByValue(dictList)

    -- Create temp filename
    local tempDir = lfs.dirname(inputFilePath) -- Get directory from input file
    tempFileName = tempDir .. "/test.tmp" -- Construct temp filename

    -- Check if test.txt already exists, replace if so
    if fileExists(tempFileName) then
        os.remove(tempFileName) -- Delete existing temp file
    end

    -- Write sorted dict list to temp file
    writeTempFile(tempFileName, dictList)

    -- Attempt to show GUI window (optional)
    if love ~= nil then
        local winWidth, winHeight = 300, 600
        local fontSize = 20
        local guiFont = love.graphics.newFont(fontSize)
        local window = love.window.create("Display Text File")

        local function drawContent()
            love.graphics.setFont(guiFont)
            
            local yPos = 50
            for _, dict in ipairs(dictList) do
                love.graphics.print(dict.name .. ": " .. dict.value, 25, yPos)
                yPos = yPos + fontSize * 1.2
            end
        end

        local function closeWindow()
            love.event.quit()
        end

        local function update(dt)
            -- Animate closing window after some delay (optional)
            if dt >= 1 then
                love.event.push("quit")
            end
        end

        local function resize(w, h)
            love.graphics.setCanvas({ width = w, height = h })
            love.graphics.clear()
            drawContent()
            love.graphics.setCanvas()
        end

        love.window.setMode(winWidth, winHeight)
        love.window.setTitle("Display Text File")
        love.window.setResizable(false)
        love.graphics.setBackgroundColor(255 / 255, 255 / 255, 255 / 255)
        love.graphics.setDefaultFilter("nearest", "nearest")
        love.mouse.setVisible(true)

        while love.update(dt) do
            if love.keyboard.isDown("escape") then
                closeWindow()
            elseif love.keypressed("return") then
                love.event.push("quit")
            end

            love.draw()
            resize(love.graphics.getDimensions())
            drawContent()
            love.timer.sleep(1 / 60) -- Cap FPS at 60
            update(dt)
        end

        love.window.close()
    end

    -- Return result
    success, tempFileName = true, tempFileName

    return success, tempFileName
end

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
-- lua "Unit_tests_lua\EX-06-display_text_file_gui\tests\Perplexity_test.lua"