function zipfs_law(str)
    -- Remove punctuation and convert to lowercase
    str = str:gsub("[%p%c%s]", ""):lower()
    
    -- Create a table to store word frequencies
    local frequencies = {}
    
    -- Iterate over each word in the string
    for word in str:gmatch("%w+") do
        -- Increment the frequency count for the word
        frequencies[word] = (frequencies[word] or 0) + 1
    end
    
    -- Create a table to store the top 10 words
    local top_words = {}
    
    -- Sort the words by frequency in descending order
    for word, frequency in pairs(frequencies) do
        table.insert(top_words, {word = word, frequency = frequency})
    end
    table.sort(top_words, function(a, b) return a.frequency > b.frequency end)
    
    -- Extract the top 10 words
    local result = {}
    for i = 1, math.min(#top_words, 10) do
        table.insert(result, top_words[i].word)
    end
    
    return result
end
