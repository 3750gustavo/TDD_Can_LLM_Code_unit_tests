function excel_sort(file_path, column_index)
    -- Load the Excel file
    local excel = require("luaxlsx")
    local workbook = excel.load(file_path)
  
    -- Get the specified column
    local column = workbook.sheets[1].columns[column_index]
  
    -- Sort the column in descending order
    column:sort(function(a, b)
      -- Handle mixed data types
      if type(a) == "number" and type(b) == "number" then
        return a > b
      elseif type(a) == "string" and type(b) == "string" then
        return a > b
      elseif type(a) == "date" and type(b) == "date" then
        return a > b
      else
        return false
      end
    end)
  
    -- Save the sorted data to a temporary file
    local temp_file = os.tmpname()
    workbook:save(temp_file)
  
    -- Return the path to the temporary file
    return temp_file
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
-- lua "Unit_tests_lua\EX-02-Excel_sort\tests\CodeLLama_test.lua"