function svg_dot_product(svg_path)
    -- Load the SVG file using LuaXML
    local xml = require("LuaXML")
    local parsed_xml = xml.load(svg_path)
   
    -- Find the <metadata> element
    local metadata = parsed_xml:find("//metadata")
    if not metadata then
      return -1  -- Metadata not found
    end
   
    -- Extract the vectors from <vector> elements
    local vectors = {}
    for vector_element in metadata:children("vector") do
      local vector_text = vector_element:text()
      local numbers = {}
      for number_str in vector_text:gmatch("%d+%.?%d*") do  -- Match numbers with optional decimals
        table.insert(numbers, tonumber(number_str))
      end
      if #numbers > 0 then
        table.insert(vectors, numbers)
      end
    end
   
    if #vectors < 2 then
      return -1  -- Fewer than two vectors found
    end
   
    -- Calculate the dot product
    local v1 = vectors[1]
    local v2 = vectors[2]
    local dot_product = 0
    for i = 1, #v1 do
      dot_product = dot_product + v1[i] * v2[i]
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
-- lua "Unit_tests_lua\EX-05-svg_vector_metadata\Test_files\Bard_test.lua"