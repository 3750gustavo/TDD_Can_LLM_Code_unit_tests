function svg_dot_product(svg_path)
    -- Load the SVG file
    local f = io.open(svg_path, "r")
    local svg_content = f:read("*all")
    f:close()
  
    -- Extract the metadata from the SVG
    local metadata = svg_content:match("<metadata>(.-)</metadata>")
    if not metadata then
      return -1
    end
  
    -- Extract the vectors from the metadata
    local vectors = {}
    for vector_str in metadata:gmatch("<vector>(.-)</vector>") do
      local vector = {}
      for num_str in vector_str:gmatch("[-0-9.]+") do
        local num = tonumber(num_str)
        if not num then
          return -1
        end
        table.insert(vector, num)
      end
      if #vector ~= 3 then
        return -1
      end
      table.insert(vectors, vector)
    end
  
    -- Calculate the dot product of the vectors
    if #vectors < 2 then
      return -1
    end
    local dot_product = 0
    for i = 1, 3 do
      dot_product = dot_product + vectors[1][i] * vectors[2][i]
    end
    return dot_product
  end