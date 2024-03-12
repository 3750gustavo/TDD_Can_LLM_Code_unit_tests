local xlsx = require("xlsx")

function excel_sort(filepath, column_index)
  local wb = xlsx.read(filepath)
  local ws = wb:sheet(1)

  table.sort(ws, function(row1, row2) 
    local value1 = row1[column_index]
    local value2 = row2[column_index]
    
    if type(value1) == "number" and type(value2) == "number" then
      return value1 > value2
    elseif type(value1) == "string" and type(value2) == "string" then
      return value1 > value2
    else
      return tostring(value1) > tostring(value2)
    end
  end)

  local tmp_filepath = os.tmpname() .. ".xlsx"
  xlsx.write(wb, tmp_filepath)

  return tmp_filepath
end

-- fails because xlsx does not exist
-- so, it is not testable N/A
