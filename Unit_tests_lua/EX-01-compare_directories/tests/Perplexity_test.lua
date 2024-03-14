function compare_directories(dir1, dir2)
    local report = {
        Passed = true,
        Failed_Count = 0,
        Failed_Tests = {}
    }

    local files1 = {}
    local files2 = {}

    for file in io.popen('ls -1 "'..dir1..'"'):lines() do
        files1[file] = lfs.attributes(dir1..'/'..file, 'modification')
    end

    for file in io.popen('ls -1 "'..dir2..'"'):lines() do
        files2[file] = lfs.attributes(dir2..'/'..file, 'modification')
    end

    for file, mod_date in pairs(files1) do
        if files2[file] then
            if mod_date < files2[file] then
                report.Passed = false
                report.Failed_Count = report.Failed_Count + 1
                table.insert(report.Failed_Tests, {Failed_Files={file}, Failure_Location='dir1'})
            elseif mod_date > files2[file] then
                report.Passed = false
                report.Failed_Count = report.Failed_Count + 1
                table.insert(report.Failed_Tests, {Failed_Files={file}, Failure_Location='dir2'})
            end
        else
            report.Passed = false
            report.Failed_Count = report.Failed_Count + 1
            table.insert(report.Failed_Tests, {Failed_Files={file}, Failure_Location='dir2'})
        end
    end

    for file, mod_date in pairs(files2) do
        if not files1[file] then
            report.Passed = false
            report.Failed_Count = report.Failed_Count + 1
            table.insert(report.Failed_Tests, {Failed_Files={file}, Failure_Location='dir1'})
        end
    end

    return report
end

-- Add LuaRocks paths
local user = "gusta"
package.path = package.path .. ";C:/Users/" .. user .. "/AppData/Roaming/luarocks/share/lua/5.4/?.lua"
package.cpath = package.cpath .. ";C:/Users/" .. user .. "/AppData/Roaming/luarocks/lib/lua/5.4/?.dll" 
local lfs = require("lfs")
-- tests:

-- Test Setup: Create necessary directories and files for testing
local TestSetup = {}

function TestSetup.create_directory_if_not_exists(directory)
    if not lfs.attributes(directory, "mode") then
        lfs.mkdir(directory)
    end
end

function TestSetup.set_date(file_path, date)
    -- Convert the date string to a format that Lua can interpret (e.g., "YYYY-MM-DD hh:mm:ss")
    local year, month, day, hour, min, sec = date:match("(%d+)-(%d+)-(%d+) (%d+):(%d+):(%d+)")
    if year and month and day and hour and min and sec then
        local timestamp = os.time({year = year, month = month, day = day, hour = hour, min = min, sec = sec})
        -- Use the lfs.touch function to set the modification time
        local success, err = lfs.touch(file_path, timestamp)
        if not success then
            print("Error setting date: " .. err)
        end
    else
        print("Error: date string is not in the expected format (YYYY-MM-DD hh:mm:ss)")
    end
end

function TestSetup.create_files(directory, filenames, content, modification_time)
    -- Ensure modification_time is a string
    modification_time = tostring(modification_time)
    for _, filename in ipairs(filenames) do
        local file_path = directory .. "/" .. filename
        local file = io.open(file_path, "w")
        file:write(content)
        file:close()
        TestSetup.set_date(file_path, modification_time)
         -- Get the actual modification time of the file for confirmation
         local attributes = lfs.attributes(file_path)
         local actual_modification_time = os.date("%Y-%m-%d %H:%M:%S", attributes.modification)
        print("File created: " .. filename .. " in " .. directory .. " with modification time " .. actual_modification_time)
    end
end

function TestSetup.prepare_directories(current_dir)
    local dir1 = current_dir .. "/test_folder1"
    local dir2 = current_dir .. "/test_folder2"

    local directories = {dir1, dir2}
    for _, directory in ipairs(directories) do
        TestSetup.create_directory_if_not_exists(directory)
    end

    return dir1, dir2
end

function TestSetup.GetDirectories()
    local current_dir = io.popen("cd"):read("*l")
    local dir1, dir2 = TestSetup.prepare_directories(current_dir)
    return dir1, dir2
end

-- Test Execution

local content = "This is file content"
local modification_time_standard = "2021-01-01 00:00:00"
-- Function to create files in the folders, all with the same modification dates of 2021-01-01
local function create_files_all_same_date(dir1, dir2)
    local filenames = {"file1.txt", "file2.txt", "file3.txt", "file4.txt", "file5.txt"}
    TestSetup.create_files(dir1, filenames, content, modification_time_standard)
    TestSetup.create_files(dir2, filenames, content, modification_time_standard)
end

-- Function to create files in the folders with some differences
local function create_files_with_differences(dir1, dir2)
    -- Create the files 1 and 4 with the same content and modification date in both folders
    TestSetup.create_files(dir1, {"file1.txt", "file4.txt"}, content, modification_time_standard)
    TestSetup.create_files(dir2, {"file1.txt", "file4.txt"}, content, modification_time_standard)
    -- file 2 and 3 same content but different current_time on dir 1
    local current_time = os.date("%Y-%m-%d %H:%M:%S")
    TestSetup.create_files(dir1, {"file2.txt", "file3.txt"}, content, current_time)
    TestSetup.create_files(dir2, {"file2.txt", "file3.txt"}, content, modification_time_standard)
    -- Create one additional file in dir2 (file5) as a way to test the case where files are not in both directories (it should ignore those)
    TestSetup.create_files(dir2, {"file5.txt"}, content, current_time)
end

local function delete_files(dir1, dir2)
    -- Iterate through directories and delete files
    for _, directory in ipairs({dir1, dir2}) do
        for filename in lfs.dir(directory) do
            if filename ~= "." and filename ~= ".." then
                local file_path = directory .. "/" .. filename
                os.remove(file_path)
            end
        end
    end
end


-- Expected result for the first test where all files have the same modification date
local expected_result_all_same_date = {
  Passed = true,
  Failed_Count = 0,
  Failed_Tests = {}
}

-- Expected result for the test where three files differ, but only two of them are in both folders
local expected_result_with_differences = {
  Passed = false,
  Failed_Count = 2,
  Failed_Tests = {
      {
          Failed_Files = {"file2.txt", "file3.txt"},
          Failure_Location = "dir2"
      }
  }
}

-- Helper function to compare two tables (arrays) for the same elements regardless of order
local function compare_unordered_lists(list1, list2)
        if #list1 ~= #list2 then return false end
        local count = {}
        for _, value in ipairs(list1) do
            count[value] = (count[value] or 0) + 1
        end
        for _, value in ipairs(list2) do
            if not count[value] then return false end
            count[value] = count[value] - 1
            if count[value] < 0 then return false end
        end
        return true
    end

local function check_test_results(result, expected_result, implementation_name)
        local string_result = "The test case with " .. implementation_name .. " has"
        local string_reasons_for_failures = "\nThe test failed because of the following reasons:"
        local passed = result["Passed"] == expected_result["Passed"]
        if not passed then
            string_reasons_for_failures = string_reasons_for_failures .. "\nPassed = " .. tostring(result["Passed"]) .. " but expected " .. tostring(expected_result["Passed"])
        end
        local failed_count_match = result["Failed_Count"] == expected_result["Failed_Count"]
        if not failed_count_match then
            string_reasons_for_failures = string_reasons_for_failures .. "\nFailed_Count = " .. tostring(result["Failed_Count"]) .. " but expected " .. tostring(expected_result["Failed_Count"])
        end
        local failed_tests_match = true
        if #expected_result["Failed_Tests"] > 0 then
            for i, failed_test in ipairs(expected_result["Failed_Tests"]) do
                if #result["Failed_Tests"] >= i then
                    local result_failed_test = result["Failed_Tests"][i]
                    local files_match = true
                    local location_match = true
                    if failed_test["Failed_Files"] and result_failed_test["Failed_Files"] then
                        files_match = compare_unordered_lists(failed_test["Failed_Files"], result_failed_test["Failed_Files"])
                    end
                    if failed_test["Failure_Location"] and result_failed_test["Failure_Location"] then
                        location_match = failed_test["Failure_Location"] == result_failed_test["Failure_Location"]
                    end
                    failed_tests_match = files_match and location_match
                    if not files_match or not location_match then
                        string_reasons_for_failures = string_reasons_for_failures .. "\nFailed_Tests[" .. i .. "] mismatch in either Failed_Files or Failure_Location."
                        break
                    end
                else
                    failed_tests_match = false
                    string_reasons_for_failures = string_reasons_for_failures .. "\nFailed_Tests table is empty but expected at least " .. tostring(#expected_result["Failed_Tests"]) .. " entries."
                    break
                end
            end
        else
            failed_tests_match = #result["Failed_Tests"] == 0
        end
        if passed and failed_count_match and failed_tests_match then
            string_result = string_result .. " passed."
        else
            string_result = string_result .. " failed." .. string_reasons_for_failures
        end
        return string_result
    end

    local function run_test(create_files_func, compare_func, expected_result, implementation_name)
        local current_dir = io.popen("cd"):read("*l")
        local dir1, dir2 = TestSetup.prepare_directories(current_dir)
        create_files_func(dir1, dir2) -- Calls the passed function to create files
        local result = compare_func(dir1, dir2)
        return check_test_results(result, expected_result, implementation_name)
    end

-- Example Test Execution
local dir1 , dir2 = TestSetup.GetDirectories()
local test1_summary = run_test(create_files_all_same_date, compare_directories, expected_result_all_same_date, "all_same_date")
delete_files(dir1, dir2)
local test2_summary = run_test(create_files_with_differences, compare_directories, expected_result_with_differences, "with_differences")
print("Test Summary:\n------------\n" .. test1_summary .. "\n" .. test2_summary)
create_files_all_same_date(dir1, dir2)
local function performanceTest()
    -- warmup
    for i = 1, 1000 do
        -- Assume dir1 and dir2 are set up and contain the necessary test files
        compare_directories(dir1, dir2)
    end
    local start_time = os.clock()
    for i = 1, 1000 do
        -- Assume dir1 and dir2 are set up and contain the necessary test files
        compare_directories(dir1, dir2)
    end
    local end_time = os.clock()
    local elapsed_time = (end_time - start_time) * 1000 -- Convert to milliseconds
    local average_time = elapsed_time / 1000
    print("Average execution time: " .. average_time .. " ms")
end

performanceTest()
-- Clean up the directories
delete_files(dir1, dir2)
-- to run this code, you can use the following command:
-- lua "Unit_tests_lua\EX-01-compare_directories\tests\perplexity_test.lua"