function display_text_file(file_path)
    local success, data = pcall(io.open, file_path)
    if not success then
      return false, nil, "Error opening file: " .. data
    end
   
    local lines = data:read("*all"):split("\n")
    local pairs = {}
   
    for _, line in ipairs(lines) do
      local name, value = line:match("([^:]+):([^:]+)")
      if name and value then
        table.insert(pairs, { name = name, value = tonumber(value) })
      end
    end
   
    table.sort(pairs, function(a, b) return a.value > b.value end)
   
    local temp_file = io.open("test.txt", "w")
    if not temp_file then
      data:close()
      return false, nil, "Error creating temporary file."
    end
   
    for _, pair in ipairs(pairs) do
      temp_file:write(pair.name .. ": " .. tostring(pair.value) .. "\n")
    end
   
    temp_file:close()
    data:close()
   
    -- Display the contents of the temporary file in a window GUI (replace with appropriate GUI calls)
    -- local gui_library = require("your_gui_library")
    -- gui_library.show_text_file("test.txt")
   
    return true, "test.txt"
   end   