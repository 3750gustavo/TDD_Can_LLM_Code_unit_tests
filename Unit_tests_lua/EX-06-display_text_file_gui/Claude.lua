function display_text_file(filepath)

    local success = true
    local temp_filepath = nil

    local function sortByNameValue(t1, t2)
        return t1.value > t2.value
    end
    
    local function displayError(err)
        print(err)
        success = false
        temp_filepath = nil
    end

    -- Read file contents
    local file, err = io.open(filepath, "r")
    if err then 
        displayError("Unable to open file at "..filepath)
        return success, temp_filepath
    end
    
    local data = file:read("*a")
    io.close(file)

    -- Parse data into table
    local records = {}
    for line in string.gmatch(data, "[^\r\n]+") do
        local name, value = line:match("^([^:]+):(.*)$")
        if name and value then
            table.insert(records, {name=name, value=value}) 
        end
    end

    -- Sort records
    table.sort(records, sortByNameValue)
    
    -- Write records to temp file
    temp_filepath = "test.txt"
    local file = io.open(temp_filepath, "w")
    if file then
        for _, record in ipairs(records) do
            file:write(record.name .. ":" .. record.value .. "\n")
        end
        io.close(file)
    else
        displayError("Failed to open temporary file at "..temp_filepath)
        return success, temp_filepath
    end

    -- Display temp file contents
    local win = gg.newWindow(800, 600)
    win:showButtonPane(false)
    win:setTitle("Temporary Text File Contents")
    win:setPosition(100, 100)

    local text = ""
    local linenum = 1
    for _, record in ipairs(records) do
        text = text .. linenum .. ". " .. record.name .. ": " .. record.value .. " \\n\\n"
        linenum = linenum + 1
    end
    win:setText(text)
    win:show()

    return success, temp_filepath
end