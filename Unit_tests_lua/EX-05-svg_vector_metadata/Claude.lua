function svg_dot_product(filepath)
    local svg = io.open(filepath, "r")
    if not svg then return -1 end
    
    local metadata = {}
    local in_metadata = false
    for line in svg:lines() do
      if line:match("<metadata>") then
        in_metadata = true
      elseif line:match("</metadata>") then
        in_metadata = false
      elseif in_metadata then
        table.insert(metadata, line) 
      end
    end
    
    local vectors = {}
    for _, line in ipairs(metadata) do
      if line:match "<vector>(.+)</vector>" then
        local vector = {}
        for n in line:match("<vector>(.-)</vector>"):gmatch("([^,%s]+)") do
          table.insert(vector, tonumber(n))
        end
        table.insert(vectors, vector)
      end
    end
    
    if #vectors < 2 then
      return -1
    else
      local dot_product = 0
      for i=1,#vectors[1] do
        dot_product = dot_product + vectors[1][i]*vectors[2][i]
      end
      return dot_product
    end
  end