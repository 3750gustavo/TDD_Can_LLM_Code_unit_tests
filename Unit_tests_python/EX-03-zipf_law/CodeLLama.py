import re

def zipfs_law(text):
    # Remove punctuation and convert to lowercase
    text = re.sub(r'[^\w\s]', '', text.lower())

    # Split the text into individual words
    words = text.split()

    # Calculate the frequency of each word
    freq = {}
    for word in words:
        if word not in freq:
            freq[word] = 0
        freq[word] += 1

    # Sort the words by frequency
    sorted_words = sorted(freq.items(), key=lambda x: x[1], reverse=True)

    # Return the top 10 most frequently used words
    return [word for word, _ in sorted_words[:10]]