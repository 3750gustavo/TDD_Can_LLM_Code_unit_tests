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

-- Test
local svg_path = [[F:\TFG\TDD_Can_LLM_Code_unit_tests\Unit_tests_lua\EX-05-svg_vector_metadata\Test_files\test.svg]]
-- checks if the svg_path is actualy pointing to a .svg file
if not svg_path:match("%.svg$") then
    print("Something went wrong, the path is not pointing to a .svg file")
end

local dot_product = svg_dot_product(svg_path)

-- Check if dot_product is 32
if dot_product == 32 then
    print("Test passed")
else
    print("Test failed" .. " - Expected: " .. 32 .. ", Got: " .. dot_product)
end

-- To run this code, you can use the following command:
-- lua "Unit_tests_lua\EX-05-svg_vector_metadata\Test_files\ChatGPT_test.lua"