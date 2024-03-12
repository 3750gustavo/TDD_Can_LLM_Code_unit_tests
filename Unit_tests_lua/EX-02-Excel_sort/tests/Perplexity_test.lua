local function excel_sort(file_path, column_index)
    local excel = require("luaxlsx")
    local workbook = excel.load(file_path)
    local sheet = workbook:getSheet(1)
    
    local data = {}
    for i = 1, sheet:rows() do
        local row = sheet:getRow(i)
        local value = row:getValue(column_index)
        table.insert(data, {row_index = i, value = value})
    end
    
    table.sort(data, function(a, b)
        if type(a.value) == type(b.value) then
            return a.value > b.value
        else
            return tostring(a.value) > tostring(b.value)
        end
    end)
    
    local temp_file_path = "sorted_temp_file.xlsx"
    local temp_workbook = excel.newWorkbook()
    local temp_sheet = temp_workbook:addSheet("Sorted Data")
    
    for i, entry in ipairs(data) do
        local original_row = sheet:getRow(entry.row_index)
        temp_sheet:setRow(i, original_row)
    end
    
    temp_workbook:save(temp_file_path)
    
    return temp_file_path
end

-- as stated on CodeLLama_test.lua, xlsx does not run on Lua 5.4
-- so it is not testable N/A