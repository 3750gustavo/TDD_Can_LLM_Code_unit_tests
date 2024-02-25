function display_text_file(file_path)
    -- Read the content of the provided .txt file
    local file = io.open(file_path, "r")
    if not file then
        print("Error: File not found")
        return false, nil
    end
    local content = file:read("*all")
    file:close()

    -- Parse the data into name-value pairs
    local data = {}
    for line in content:gmatch("[^\r\n]+") do
        local name, value = line:match("(.-):(.+)")
        if name and value then
            table.insert(data, {name = name, value = tonumber(value)})
        end
    end

    -- Sort the list of dictionaries in descending order based on the 'value' key
    table.sort(data, function(a, b)
        return a.value > b.value
    end)

    -- Create or overwrite the temporary .txt file
    local temp_file_path = "test.txt"
    local temp_file = io.open(temp_file_path, "w")
    if not temp_file then
        print("Error: Failed to create temporary file")
        return false, nil
    end
    for _, entry in ipairs(data) do
        temp_file:write(entry.name .. ":" .. entry.value .. "\n")
    end
    temp_file:close()

    -- Display the contents of the temporary .txt file in a window GUI
    -- (Code for displaying GUI is not provided as it depends on the specific Lua GUI library being used)

    -- Return the result
    return true, temp_file_path
end