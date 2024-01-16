import re
from collections import Counter

def zipfs_law(input_string):
    # Tokenize the input string into words
    words = re.findall(r'\b\w+\b', input_string.lower())
    
    # Count the frequency of each word
    word_count = Counter(words)
    
    # Sort the words by their frequency in descending order
    sorted_words = sorted(word_count.items(), key=lambda x: x[1], reverse=True)
    
    # Get the top 10 words
    top_10_words = [word for word, frequency in sorted_words[:10]]
    
    return top_10_words