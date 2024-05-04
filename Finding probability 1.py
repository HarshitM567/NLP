import re

# Read the contents of the file
with open('shakes.txt', 'r') as file:
    text = file.read()

# Define a regular expression pattern to find words ending with "."
pattern = r'\b\w+\.\b'

# Find all matches of the pattern in the text
matches = re.findall(pattern, text)

# Count the total number of words
total_words = len(re.findall(r'\b\w+\b', text))

# Count the number of words ending with "."
words_with_period = len(matches)

# Calculate the probability
probability = words_with_period / total_words

print("Total words:", total_words)
print("Words ending with '.':", words_with_period)
print("Probability:", probability)
