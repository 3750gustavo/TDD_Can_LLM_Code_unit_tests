local math = require('math')

function calculate_stats(list1, list2, list3)
  local means = {}
  local stddevs = {}
  
  for i, list in ipairs({list1, list2, list3}) do
    local sum = 0
    for _, x in ipairs(list) do
      sum = sum + x
    end
    local mn = sum / #list
    table.insert(means, mn)
    
    local var = 0
    for _, x in ipairs(list) do
      var = var + (x - mn)^2 
    end
    local std = math.sqrt(var / #list)
    table.insert(stddevs, std)
  end
  
  return {
    mean = means,
    stddev = stddevs
  }
end