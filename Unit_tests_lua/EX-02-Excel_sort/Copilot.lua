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