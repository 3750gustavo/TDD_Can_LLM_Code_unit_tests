import re
from collections import Counter

def zipfs_law(text):
    # Remove punctuation and convert to lowercase
    text = re.sub(r'[^\w\s]', '', text.lower())
    
    # Tokenize the text into words
    words = text.split()

    # Use Counter to count word frequencies
    word_counts = Counter(words)

    # Get the top 10 most common words
    top_10_words = [word for word, _ in word_counts.most_common(10)]

    return top_10_words