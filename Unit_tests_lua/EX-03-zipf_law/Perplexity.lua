function zipfs_law(input_string)
    -- Remove punctuation and convert to lowercase
    local clean_string = input_string:gsub("[%p%c%s]", ""):lower()
    
    -- Create a table to store word frequencies
    local word_freq = {}
    
    -- Iterate over each word in the string
    for word in clean_string:gmatch("%w+") do
        if word_freq[word] then
            word_freq[word] = word_freq[word] + 1
        else
            word_freq[word] = 1
        end
    end
    
    -- Create a table to store words and their frequencies as pairs
    local freq_table = {}
    
    for word, freq in pairs(word_freq) do
        table.insert(freq_table, {word = word, freq = freq})
    end
    
    -- Sort the table based on frequency in descending order
    table.sort(freq_table, function(a, b) return a.freq > b.freq end)
    
    -- Extract the top 10 most frequent words
    local top_words = {}
    
    for i = 1, math.min(10, #freq_table) do
        table.insert(top_words, freq_table[i].word)
    end
    
    return top_words
end

-- Example usage:
local input_text = "Sample text for testing Zipf's Law. This is a sample text."
local top_words = zipfs_law(input_text)

for i, word in ipairs(top_words) do
    print(i .. ". " .. word)
end