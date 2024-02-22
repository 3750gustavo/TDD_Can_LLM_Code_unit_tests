function svg_dot_product(svg_path)
    local file = io.open(svg_path, "r")
    if not file then
        return -1
    end
    
    local metadata = ""
    for line in file:lines() do
        if line:find("<metadata>") then
            metadata = line
            break
        end
    end
    
    file:close()
    
    local vectors = {}
    for vector in metadata:gmatch("<vector>(.-)</vector>") do
        local x, y, z = vector:match("([^,]+),([^,]+),([^,]+)")
        if x and y and z then
            table.insert(vectors, {x = tonumber(x), y = tonumber(y), z = tonumber(z)})
        end
    end
    
    if #vectors < 2 then
        return -1
    end
    
    local dot_product = vectors[1].x * vectors[2].x + vectors[1].y * vectors[2].y + vectors[1].z * vectors[2].z
    return dot_product
end
