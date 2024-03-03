function zipfs_law(str)
    -- Remove punctuation and convert to lowercase
    str = str:gsub("%p", ""):lower()
  
    -- Split the string into individual words
    local words = str:split(" ")
  
    -- Count the frequency of each word
    local freq = {}
    for i, word in ipairs(words) do
      freq[word] = (freq[word] or 0) + 1
    end
  
    -- Sort the words by frequency in descending order
    local sorted_words = {}
    for word, count in pairs(freq) do
      table.insert(sorted_words, {word, count})
    end
    table.sort(sorted_words, function(a, b) return a[2] > b[2] end)
  
    -- Return the top 10 most frequently used words
    return sorted_words[1][1], sorted_words[2][1], sorted_words[3][1], sorted_words[4][1], sorted_words[5][1], sorted_words[6][1], sorted_words[7][1], sorted_words[8][1], sorted_words[9][1], sorted_words[10][1]
  end