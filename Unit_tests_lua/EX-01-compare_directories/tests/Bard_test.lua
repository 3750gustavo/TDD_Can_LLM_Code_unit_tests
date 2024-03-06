function compare_directories(dir1, dir2)
    local report = {
      Passed = true,
      Failed_Count = 0,
      Failed_Tests = {},
    }
  
    -- Check if both directories exist
    if not io.dir(dir1) or not io.dir(dir2) then
      report.Passed = false
      report.Failed_Count = report.Failed_Count + 1
      table.insert(report.Failed_Tests, {
        Failed_Files = {"Both directories"},
        Failure_Location = "N/A",
      })
      return report
    end
  
    -- Helper function to compare file details
    local function compare_files(file1, file2)
      local stat1 = io.stat(dir1 .. "/" .. file1)
      local stat2 = io.stat(dir2 .. "/" .. file2)
  
      -- Check if files exist
      if not stat1 or not stat2 then
        report.Passed = false
        report.Failed_Count = report.Failed_Count + 1
        table.insert(report.Failed_Tests, {
          Failed_Files = {file1},
          Failure_Location = stat1 and "dir2" or "dir1",
        })
        return
      end
  
      -- Check file content
      if not io.open(dir1 .. "/" .. file1, "rb") or not io.open(dir2 .. "/" .. file2, "rb") then
        report.Passed = false
        report.Failed_Count = report.Failed_Count + 1
        table.insert(report.Failed_Tests, {
          Failed_Files = {file1},
          Failure_Location = "Error reading file content",
        })
        return
      end
      local content1 = io.read("*a")
      local content2 = io.read("*a")
      io.close()
      if content1 ~= content2 then
        report.Passed = false
        report.Failed_Count = report.Failed_Count + 1
        table.insert(report.Failed_Tests, {
          Failed_Files = {file1},
          Failure_Location = "Content mismatch",
        })
      end
  
      -- Check file modification dates
      if stat1.mtime ~= stat2.mtime then
        local failure_location = stat1.mtime < stat2.mtime and "dir1" or "dir2"
        report.Passed = false
        report.Failed_Count = report.Failed_Count + 1
        table.insert(report.Failed_Tests, {
          Failed_Files = {file1},
          Failure_Location = failure_location .. " has older modification date",
        })
      end
    end
  
    -- Iterate over files in dir1
    for filename in io.dir(dir1) do
      if filename ~= "." and filename ~= ".." then
        compare_files(filename, filename)
      end
    end
  
    return report
  end

-- tests

-- Add LuaRocks paths
local user = "gusta"
package.path = package.path .. ";C:/Users/" .. user .. "/AppData/Roaming/luarocks/share/lua/5.4/?.lua"
package.cpath = package.cpath .. ";C:/Users/" .. user .. "/AppData/Roaming/luarocks/lib/lua/5.4/?.dll"

lfs = require("lfs")
-- Define the current working directory
current_dir = io.popen("cd"):read("*l")

-- Define the directories to compare
dir1 = current_dir .. "/test_folder1"
dir2 = current_dir .. "/test_folder2"

-- Define a function to create directories if they don't exist
  function create_directory_if_not_exists(directory)
    if not lfs.attributes(directory, "mode") then
        lfs.mkdir(directory)
    end
end

-- ensure the directories exist
directories = {dir1, dir2}
for _, directory in ipairs(directories) do
    create_directory_if_not_exists(directory)
end

-- Function to set the modification date of a file to 2021-01-01
function set_date(file_path)
  -- This implementation assumes the use of the 'touch' command, which might not be available on all systems
  os.execute("touch -t 202101010000 " .. file_path)
end

-- Function to create files in the folders, all with the same modification dates of 2021-01-01
function create_files_all_same_date()
  -- Define the file content and modification date
  local file_content = "This is file content"
  local modification_time = os.time({year=2021, month=1, day=1})
  
  -- Iterate through directories and create files
  for i = 1, 5 do
      for _, directory in ipairs(directories) do
          local file_path = directory .. "/file" .. i .. ".txt"
          local file = io.open(file_path, "w")
          file:write(file_content)
          file:close()
          
          -- Set modification date to 2021-01-01
          os.setmod(file_path, modification_time, modification_time)
      end
  end
end

-- Function to create files in the folders with some differences
function create_files_with_differences()
  -- Define the file content for the first two files
  local file_content_1_2 = "This is file content"
  
  -- Define the modification time for all files
  local modification_time = os.time({year=2021, month=1, day=1})
  
  -- Create two files with the same content and modification date in both folders
  for i = 1, 2 do
      for _, directory in ipairs(directories) do
          local file_path = directory .. "/file" .. i .. ".txt"
          local file = io.open(file_path, "w")
          file:write(file_content_1_2)
          file:close()
          
          -- Set modification date to 2021-01-01
          os.setmod(file_path, modification_time, modification_time)
      end
  end
  
  -- Define the file content for the next two files
  local file_content_3_4 = "This is file content with differences"
  
  -- Modify the modification time for the files in dir2 to the current date
  local current_time = os.time()
  
  -- Create two files with same content but different modification date in both folders
  for i = 3, 4 do
      local file_path = dir1 .. "/file" .. i .. ".txt"
      local file = io.open(file_path, "w")
      file:write(file_content_3_4)
      file:close()
      
      -- Set modification date to 2021-01-01
      os.setmod(file_path, modification_time, modification_time)
      
      -- Create file in dir2 with current date modification time
      file_path = dir2 .. "/file" .. i .. ".txt"
      file = io.open(file_path, "w")
      file:write(file_content_3_4)
      file:close()
  end
  
  -- Create one additional file in dir2
  local additional_file_content = "This is file 5 content"
  local additional_file_path = dir2 .. "/file5.txt"
  local file = io.open(additional_file_path, "w")
  file:write(additional_file_content)
  file:close()
  
  -- Set modification date to 2021-01-01
  os.setmod(additional_file_path, modification_time, modification_time)
end

-- Function to delete all files from the folders
function delete_files()
  -- Iterate through directories and delete files
  for _, directory in ipairs(directories) do
    for filename in lfs.dir(directory) do
        if filename ~= "." and filename ~= ".." then
            local file_path = directory .. "/" .. filename
            os.remove(file_path)
        end
    end
end
end

-- Expected result for the first test where all files have the same modification date
expected_result_all_same_date = {
  Passed = true,
  Failed_Count = 0,
  Failed_Tests = {}
}

-- Expected result for the test where three files differ, but only two of them are in both folders
expected_result_with_differences = {
  Passed = false,
  Failed_Count = 2,
  Failed_Tests = {
      {
          Failed_Files = {"file2.txt", "file3.txt"},
          Failure_Location = "dir2"
      }
  }
}

-- Function to check test results and print summary
function check_test_results(result, expected_result, implementation_name)
  -- Check if the test passed or failed
  local passed = result["Passed"] == expected_result["Passed"]
  local failed_count_match = result["Failed_Count"] == expected_result["Failed_Count"]
  
  -- Check if Failed_Tests is an empty list
  local failed_tests_match = true
  if #expected_result["Failed_Tests"] > 0 then
      for i, failed_test in ipairs(expected_result["Failed_Tests"]) do
          local result_failed_test = result["Failed_Tests"][i]
          if result_failed_test["Failed_Files"] ~= failed_test["Failed_Files"] or result_failed_test["Failure_Location"] ~= failed_test["Failure_Location"] then
              failed_tests_match = false
              break
          end
      end
  else
      failed_tests_match = #result["Failed_Tests"] == 0
  end
  
  -- Print test summary
  print("Test Summary:")
  print("------------")
  print("Implementation:", implementation_name)
  print("Passed:", passed)
  print("Failed Count Match:", failed_count_match)
  print("Failed Tests Match:", failed_tests_match)
  
  -- Determine overall test result
  local overall_result = passed and failed_count_match and failed_tests_match
  if overall_result then
      print("All tests passed!")
  else
      print("Some tests failed.")
  end
end

-- Run tests for all_same_date implementation
print("Running test for all_same_date implementation...")
local result_all_same_date = compare_directories(dir1, dir2)
check_test_results(result_all_same_date, expected_result_all_same_date, "all_same_date")

-- Run tests for with_differences implementation
print("\nRunning test for with_differences implementation...")
local result_with_differences = compare_directories(dir1, dir2)
check_test_results(result_with_differences, expected_result_with_differences, "with_differences")

-- Clean up the directories
delete_files()

-- to execute the test, run the following command:
-- lua "Unit_tests_lua\EX-01-compare_directories\tests\Bard_test.lua"