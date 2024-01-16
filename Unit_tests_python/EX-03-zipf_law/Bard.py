import re

def zipfs_law(text):
 """Applies Zipf's Law to find the top 10 most frequently used words in a string.

 Args:
   text: The string to analyze.

 Returns:
   A list of the top 10 most frequently used words in descending order.
 """

 # Remove punctuation and convert to lowercase
 words = re.sub(r'[^\w\s]', '', text.lower()).split()

 # Create a word frequency dictionary
 word_counts = {}
 for word in words:
   word_counts[word] = word_counts.get(word, 0) + 1

 # Sort the words by frequency in descending order
 sorted_words = sorted(word_counts, key=word_counts.get, reverse=True)

 # Return the top 10 words
 return sorted_words[:10]