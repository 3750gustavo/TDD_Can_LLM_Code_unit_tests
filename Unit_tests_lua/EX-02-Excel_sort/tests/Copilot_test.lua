function excel_sort(file_path, column_index)
    -- Load the Excel file and extract the data
    local excel_data = load_excel_data(file_path)
    
    -- Sort the data based on the specified column index
    table.sort(excel_data, function(a, b)
        local value_a = a[column_index]
        local value_b = b[column_index]
        
        -- Handle different data types for comparison
        if type(value_a) == "number" and type(value_b) == "number" then
            return value_a > value_b
        elseif type(value_a) == "string" and type(value_b) == "string" then
            return value_a > value_b
        elseif type(value_a) == "table" and type(value_b) == "table" then
            -- Handle date comparison
            return compare_dates(value_a, value_b)
        else
            -- Handle mixed data types
            return tostring(value_a) > tostring(value_b)
        end
    end)
    
    -- Save the sorted data to a temporary file
    local temp_file_path = save_sorted_data(excel_data)
    
    -- Return the path to the temporary file
    return temp_file_path
end

-- Add LuaRocks paths
local user = "gusta"
package.path = package.path .. ";C:/Users/" .. user .. "/AppData/Roaming/luarocks/share/lua/5.4/?.lua"
package.cpath = package.cpath .. ";C:/Users/" .. user .. "/AppData/Roaming/luarocks/lib/lua/5.4/?.dll" 
local lfs = require("lfs")
-- Test setup:
local excel_file = [[F:\TFG\TDD_Can_LLM_Code_unit_tests\Unit_tests_lua\EX-02-Excel_sort\tests\test.xlsx]]
local column_index = 1
local expected_results_file = [[Unit_tests_lua/EX-02-Excel_sort/tests/expected_results.txt]]
local temp_file = excel_sort(excel_file, column_index)
-- check if was sorted correctly for index 1

function parse_expected_results(file_path, column_index)
  local results = {}
  local current_section
  for line in io.lines(file_path) do
      if line:match("For column (%d):") then
          current_section = tonumber(line:match("For column (%d):"))
          results[current_section] = {}
      elseif line:match("%d+%s+%w+") and current_section == column_index then
          table.insert(results[current_section], line)
      end
  end
  return results[column_index]
end

function compare_results(temp_file, expected_results)
  local excel = require("luaxlsx")
  local workbook = excel.load(temp_file)
  local sheet = workbook.sheets[1]
  local data = {}
  for i, row in ipairs(sheet.rows) do
      -- Assuming the first column is the index, second is Name, third is Age, and fourth is City
      local line = string.format("%d   %s   %s        %s", row[1], row[2], row[3], row[4])
      table.insert(data, line)
  end
  for i, line in ipairs(data) do
      if line ~= expected_results[i] then
          return false, string.format("Mismatch at line %d: expected %s, got %s", i, expected_results[i], line)
      end
  end
  return true
end

-- Continue with the existing setup
local expected_results = parse_expected_results(expected_results_file, column_index)
local comparison_result, error_message = compare_results(temp_file, expected_results)

if comparison_result then
  print("The sorting results match the expected output.")
else
  print("The sorting results do not match the expected output.", error_message)
end

-- Test fails due to xlsx module being unsupported in Lua 5.4 (requires Lua 5.1 or 5.2)

-- to run this code, you can use the following command:
-- lua "Unit_tests_lua\EX-02-Excel_sort\tests\Copilot_test.lua"