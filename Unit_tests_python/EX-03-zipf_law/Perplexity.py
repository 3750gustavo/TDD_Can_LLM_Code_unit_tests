import re
from collections import Counter

def zipfs_law(text):
    # Remove punctuation and convert to lowercase
    text = re.sub(r'[^\w\s]', '', text).lower()

    # Split the text into words
    words = text.split()

    # Count the frequency of each word
    word_counts = Counter(words)

    # Get the top 10 most frequently used words
    top_10_words = word_counts.most_common(10)

    return [word[0] for word in top_10_words]