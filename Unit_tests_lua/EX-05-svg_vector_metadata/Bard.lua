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