import re

# Read the content of the file
with open('shakes.txt', 'r') as file:
    text = file.read()

# Define a regular expression to find words containing "."
pattern = r'\b\w*\.\w*\b'

# Find all matching words in the text
matching_words = re.findall(pattern, text)

# Calculate the length of each word
word_lengths = [len(word) for word in matching_words]

# Print the results
print("Words containing '.' :", matching_words)
print("Length of each word containing '.':", word_lengths)
