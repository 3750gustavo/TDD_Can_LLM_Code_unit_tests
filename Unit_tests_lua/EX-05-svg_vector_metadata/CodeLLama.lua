function svg_dot_product(svg_file_path)
    -- Open the SVG file and read its contents
    local svg_file = io.open(svg_file_path, "r")
    local svg_contents = svg_file:read("*a")
    svg_file:close()
  
    -- Find the <metadata> element in the SVG contents
    local metadata_start, metadata_end = string.find(svg_contents, "<metadata>")
    if not metadata_start then
      return -1
    end
  
    -- Find the <vector> elements in the metadata
    local vector1_start, vector1_end = string.find(svg_contents, "<vector>", metadata_start)
    local vector2_start, vector2_end = string.find(svg_contents, "<vector>", vector1_end)
    if not vector1_start or not vector2_start then
      return -1
    end
  
    -- Extract the text content of the <vector> elements
    local vector1_text = string.sub(svg_contents, vector1_start + 1, vector1_end - 1)
    local vector2_text = string.sub(svg_contents, vector2_start + 1, vector2_end - 1)
  
    -- Parse the text content as vectors
    local vector1 = {}
    local vector2 = {}
    for i, value in ipairs(string.split(vector1_text, ",")) do
      vector1[i] = tonumber(value)
    end
    for i, value in ipairs(string.split(vector2_text, ",")) do
      vector2[i] = tonumber(value)
    end
  
    -- Calculate the dot product of the vectors
    local dot_product = 0
    for i = 1, #vector1 do
      dot_product = dot_product + vector1[i] * vector2[i]
    end
  
    return dot_product
  end