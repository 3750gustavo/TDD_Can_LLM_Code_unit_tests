function display_text_file(file_path)
    -- Check if file exists
    local file = io.open(file_path, "r")
    if not file then
        print("Error: File does not exist.")
        return false, nil
    end
    
    -- Read content of the file
    local content = file:read("*all")
    file:close()
    
    -- Parse data into name-value pairs
    local data = {}
    for line in content:gmatch("[^\n]+") do
        local name, value = line:match("([^:]+):([^:]+)")
        if name and value then
            table.insert(data, {name = name, value = tonumber(value)})
        else
            print("Error: Invalid data format.")
            return false, nil
        end
    end
    
    -- Sort data in descending order based on 'value' key
    table.sort(data, function(a, b) return a.value > b.value end)
    
    -- Write sorted data to temporary file
    local temp_file_path = "test.txt"
    local temp_file = io.open(temp_file_path, "w")
    if not temp_file then
        print("Error: Could not create temporary file.")
        return false, nil
    end
    for _, entry in ipairs(data) do
        temp_file:write(entry.name .. ":" .. entry.value .. "\n")
    end
    temp_file:close()
    
    -- Display contents of temporary file in GUI window
    -- GUI display code here...
    
    return true, temp_file_path
end

-- Example usage:
local success, temp_file_path = display_text_file("example.txt")
if success then
    print("Operation successful. Temporary file path:", temp_file_path)
else
    print("Operation failed.")
end