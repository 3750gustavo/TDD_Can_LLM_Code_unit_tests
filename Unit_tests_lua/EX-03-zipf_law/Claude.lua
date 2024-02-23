function zipfs_law(str)
    -- Remove punctuation and make lowercase
    str = string.gsub(string.lower(str), "%p", "")
    
    -- Split into words
    local words = {}
    for word in string.gmatch(str, "%w+") do
      table.insert(words, word) 
    end
    
    -- Count frequency of each word
    local freq = {}
    for _, word in ipairs(words) do
      freq[word] = (freq[word] or 0) + 1
    end
  
    -- Sort by frequency
    local sorted_freq = {}
    for word, count in pairs(freq) do
      table.insert(sorted_freq, {word, count})
    end
    table.sort(sorted_freq, function(a, b) return a[2] > b[2] end)
  
    -- Return top 10
    local top10 = {}
    for i = 1, math.min(10, #sorted_freq) do
      table.insert(top10, sorted_freq[i][1])
    end
    return top10
  end