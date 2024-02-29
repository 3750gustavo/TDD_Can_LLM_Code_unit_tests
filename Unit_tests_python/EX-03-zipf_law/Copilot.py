import string

def zipfs_law(text):
    # Remove punctuation and convert to lowercase
    text = text.translate(str.maketrans('', '', string.punctuation)).lower()
    
    # Split the text into words
    words = text.split()
    
    # Count the frequency of each word
    word_counts = {}
    for word in words:
        if word in word_counts:
            word_counts[word] += 1
        else:
            word_counts[word] = 1
    
    # Sort the words by frequency in descending order
    sorted_words = sorted(word_counts, key=word_counts.get, reverse=True)
    
    # Return the top 10 most frequent words
    return sorted_words[:10]