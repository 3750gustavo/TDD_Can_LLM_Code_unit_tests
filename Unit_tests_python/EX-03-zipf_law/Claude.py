import re
from collections import Counter

def zipfs_law(text):
    # Remove punctuation and make lowercase
    text = re.sub(r'[^\w\s]', '', text.lower())
    
    # Split into words
    words = text.split()
    
    # Count word frequencies
    word_counts = Counter(words)
    
    # Get top 10 words
    top_10 = word_counts.most_common(10)
    
    # Extract the words only
    top_10_words = [word for word, count in top_10]
    
    return top_10_words