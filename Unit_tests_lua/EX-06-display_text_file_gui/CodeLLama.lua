function display_text_file(file_path)
    -- Check if the file exists
    if not file_path or not file_path:is_file() then
      return false, nil, "File does not exist"
    end
  
    -- Read the content of the file
    local file = io.open(file_path, "r")
    local content = file:read("*a")
    file:close()
  
    -- Parse the content into name-value pairs
    local name_value_pairs = {}
    for line in content:gmatch("([^:]+):([^:]+)") do
      name_value_pairs[line[1]] = line[2]
    end
  
    -- Sort the name-value pairs in descending order based on the 'value' key
    table.sort(name_value_pairs, function(a, b) return a.value > b.value end)
  
    -- Check if the temporary file exists
    local temp_file_path = "test.txt"
    if not temp_file_path:is_file() then
      -- Create a temporary file
      local temp_file = io.open(temp_file_path, "w")
      temp_file:write(table.concat(name_value_pairs, "\n"))
      temp_file:close()
    else
      -- Overwrite the temporary file
      local temp_file = io.open(temp_file_path, "w")
      temp_file:write(table.concat(name_value_pairs, "\n"))
      temp_file:close()
    end
  
    -- Display the contents of the temporary file in a window GUI
    local window = display.newWindow("Text File Viewer")
    window:setSize(800, 600)
    window:setPosition(display.getCenter())
    window:setBackgroundColor(0xFF, 0xFF, 0xFF)
    window:setTitle("Text File Viewer")
  
    local text_view = display.newText(name_value_pairs, 10, 10, 780, 580)
    text_view:setFontSize(14)
    text_view:setFontColor(0x00, 0x00, 0x00)
    text_view:setBackgroundColor(0xFF, 0xFF, 0xFF)
    text_view:setPosition(10, 10)
    window:addChild(text_view)
  
    -- Return a tuple containing a boolean value indicating whether the operation was successful and the absolute path to the temporary .txt file
    return true, temp_file_path
  end