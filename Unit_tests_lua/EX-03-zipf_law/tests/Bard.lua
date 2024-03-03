function zipfs_law(text)
    -- Remove punctuation and convert to lowercase
    local clean_text = string.gsub(text, "%p", "")
    clean_text = string.lower(clean_text)
  
    -- Split the text into words
    local words = string.split(clean_text)
  
    -- Create a table to store word counts
    local word_counts = {}
    for _, word in ipairs(words) do
      word_counts[word] = (word_counts[word] or 0) + 1
    end
  
    -- Sort the table by word count in descending order
    local sorted_words = {}
    for word, count in pairs(word_counts) do
      table.insert(sorted_words, {word = word, count = count})
    end
    table.sort(sorted_words, function(a, b) return b.count - a.count end)
  
    -- Return the top 10 most frequent words
    return table.sub(sorted_words, 1, 10)
  end  