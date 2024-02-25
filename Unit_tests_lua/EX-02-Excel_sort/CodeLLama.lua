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