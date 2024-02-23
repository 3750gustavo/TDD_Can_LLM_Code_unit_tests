function zipfs_law(input_string)
    -- Remove punctuation and convert to lowercase
    local cleaned_string = input_string:gsub("[%p%c%s]+", " "):lower()
    
    -- Create a table to count word frequencies
    local word_count = {}
    
    -- Iterate through each word in the cleaned string
    for word in cleaned_string:gmatch("%S+") do
        -- Increment word count in the table
        word_count[word] = (word_count[word] or 0) + 1
    end
    
    -- Create a list of words and their frequencies
    local word_list = {}
    for word, count in pairs(word_count) do
        table.insert(word_list, {word = word, count = count})
    end
    
    -- Sort the list by word frequency in descending order
    table.sort(word_list, function(a, b) return a.count > b.count end)
    
    -- Extract the top 10 words
    local top_words = {}
    for i = 1, math.min(10, #word_list) do
        table.insert(top_words, word_list[i].word)
    end
    
    -- Return the list of top 10 words
    return top_words
end

-- Example usage:
local input_string = "Example input string, with some words repeating. This is an example string."
local top_words = zipfs_law(input_string)
for i, word in ipairs(top_words) do
    print(i, word)
end