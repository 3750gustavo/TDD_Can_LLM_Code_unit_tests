from collections import Counter

def zipfs_law(text):
 """
 Finds the top 10 most frequent words in a text using Zipf's Law.

 Args:
     text: A string containing the text to analyze.

 Returns:
     A list of the top 10 most frequent words in the text, ordered by decreasing frequency.
 """

 # Lowercase the text and remove punctuation.
 text = text.lower()
 text = "".join(char for char in text if char.isalnum() or char.isspace())

 # Split the text into words.
 words = text.split()

 # Count the frequency of each word.
 word_counts = Counter(words)

 # Sort the word counts by frequency in descending order.
 most_frequent_words = word_counts.most_common(10)

 # Extract the words from the tuples.
 top_10_words = [word for word, _ in most_frequent_words]

 return top_10_words