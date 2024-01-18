-- Helper function to split a string into words
function split_words(text)
    local words = {}
    for word in text:gmatch("%w+") do
        table.insert(words, word)
    end
    return words
end

-- Main function to apply Zipf's Law
function zipfs_law(input_string)
    -- Convert the input string to lowercase and remove punctuation
    input_string = input_string:lower():gsub("[%p%c]", " ")

    -- Split the string into words
    local words = split_words(input_string)

    -- Create a table to store word frequencies
    local word_count = {}

    -- Count the frequency of each word
    for _, word in ipairs(words) do
        if word_count[word] then
            word_count[word] = word_count[word] + 1
        else
            word_count[word] = 1
        end
    end

    -- Create a table to store word-frequency pairs
    local word_frequency = {}

    -- Convert the word-count table into a word-frequency table
    for word, count in pairs(word_count) do
        table.insert(word_frequency, {word = word, frequency = count})
    end

    -- Sort the word-frequency table by frequency in descending order
    table.sort(word_frequency, function(a, b)
        return a.frequency > b.frequency
    end)

    -- Extract the top 10 most frequent words
    local top_10_words = {}
    for i = 1, math.min(10, #word_frequency) do
        table.insert(top_10_words, word_frequency[i].word)
    end

    return top_10_words
end