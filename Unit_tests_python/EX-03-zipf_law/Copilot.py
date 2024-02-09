import re
from collections import Counter

def zipfs_law(string):
    # Remove punctuation and convert to lowercase
    string = re.sub(r'[^\w\s]', '', string.lower())
    
    # Count the frequency of each word
    word_counts = Counter(string.split())
    
    # Get the top 10 most frequent words
    top_10_words = [word for word, count in word_counts.most_common(10)]
    
    return top_10_words