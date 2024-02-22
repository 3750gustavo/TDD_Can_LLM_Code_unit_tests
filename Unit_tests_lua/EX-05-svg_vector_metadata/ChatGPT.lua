function svg_dot_product(svg_path)
    local f = io.open(svg_path, "r")
    if not f then
        return -1 -- Failed to open file
    end
    
    local content = f:read("*all")
    f:close()
    
    -- Extract vectors from metadata
    local vector1, vector2 = content:match("<metadata>.-<vector>(.-)</vector>.-<vector>(.-)</vector>.-</metadata>")
    
    -- Check if both vectors were found
    if not vector1 or not vector2 then
        return -1 -- Less than two vectors found
    end
    
    -- Parse vectors into tables
    local vec1 = {}
    for num in vector1:gmatch("[^,]+") do
        table.insert(vec1, tonumber(num))
    end
    
    local vec2 = {}
    for num in vector2:gmatch("[^,]+") do
        table.insert(vec2, tonumber(num))
    end
    
    -- Check if vectors have three components
    if #vec1 ~= 3 or #vec2 ~= 3 then
        return -1 -- Vectors cannot be parsed
    end
    
    -- Compute dot product
    local dot_product = 0
    for i = 1, 3 do
        dot_product = dot_product + vec1[i] * vec2[i]
    end
    
    return dot_product
end

local result = svg_dot_product("path/to/svg_file.svg")
print(result)