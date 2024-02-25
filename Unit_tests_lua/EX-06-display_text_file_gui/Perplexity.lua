local fs = require("fs") -- Load filesystem library for I/O operations
local table_sort = table.sort
local json = require("json") -- For converting tables to JSON strings
local tween = require("hump.easing").linear -- Optional dependency for smooth animation (GUI)
local love = _G.love or nil -- Love2D framework (for creating GUI window)

-- Function to check if file exists
function fileExists(path)
    local ok, err = pcall(function()
        io.open(path, "r")
    end)
    return ok and not err
end

-- Function to read text file and convert lines to name-value pairs
function parseFileToDicts(filename)
    local dictList = {}
    
    for line in io.lines(filename) do -- Iterate through file lines
        local parts = string.split(line, ":", { plain = true }) -- Split at colon
        
        if #parts == 2 then -- Ensure two parts (key and value)
            table.insert(dictList, { name = parts[1], value = tonumber(parts[2]) or parts[2] }) -- Convert values to numbers when possible
        end
    end

    return dictList
end

-- Function to sort dictionary list by value
function sortByValue(list)
    table_sort(list, function(a, b)
        return a.value > b.value
    end)
end

-- Function to write dictionary list to temp file
function writeTempFile(tempFilename, dictList)
    local f = assert(io.open(tempFilename, "w")) -- Open or create temp file
    for _, dict in ipairs(dictList) do
        f:write(string.format("%s:%s\n", dict.name, dict.value)) -- Write each pair to file
    end
    f:close()
end

-- Main function
function displayTextFile(inputFilePath)
    local success, tempFileName = false, ""

    -- Check input file existence
    if not fileExists(inputFilePath) then
        print("Error: File '" .. inputFilePath .. "' does not exist.")
        return false, "", nil
    end

    -- Parse input file
    local dictList = parseFileToDicts(inputFilePath)
    sortByValue(dictList)

    -- Create temp filename
    local tempDir = fs.dirname(inputFilePath) -- Get directory from input file
    tempFileName = tempDir .. "/test.tmp" -- Construct temp filename

    -- Check if test.txt already exists, replace if so
    if fileExists(tempFileName) then
        os.remove(tempFileName) -- Delete existing temp file
    end

    -- Write sorted dict list to temp file
    writeTempFile(tempFileName, dictList)

    -- Attempt to show GUI window (optional)
    if love ~= nil then
        local winWidth, winHeight = 300, 600
        local fontSize = 20
        local guiFont = love.graphics.newFont(fontSize)
        local window = love.window.create("Display Text File")

        local function drawContent()
            love.graphics.setFont(guiFont)
            
            local yPos = 50
            for _, dict in ipairs(dictList) do
                love.graphics.print(dict.name .. ": " .. dict.value, 25, yPos)
                yPos = yPos + fontSize * 1.2
            end
        end

        local function closeWindow()
            love.event.quit()
        end

        local function update(dt)
            -- Animate closing window after some delay (optional)
            if dt >= 1 then
                love.event.push("quit")
            end
        end

        local function resize(w, h)
            love.graphics.setCanvas({ width = w, height = h })
            love.graphics.clear()
            drawContent()
            love.graphics.setCanvas()
        end

        love.window.setMode(winWidth, winHeight)
        love.window.setTitle("Display Text File")
        love.window.setResizable(false)
        love.graphics.setBackgroundColor(255 / 255, 255 / 255, 255 / 255)
        love.graphics.setDefaultFilter("nearest", "nearest")
        love.mouse.setVisible(true)

        while love.update(dt) do
            if love.keyboard.isDown("escape") then
                closeWindow()
            elseif love.keypressed("return") then
                love.event.push("quit")
            end

            love.draw()
            resize(love.graphics.getDimensions())
            drawContent()
            love.timer.sleep(1 / 60) -- Cap FPS at 60
            update(dt)
        end

        love.window.close()
    end

    -- Return result
    success, tempFileName = true, tempFileName

    return success, tempFileName
end