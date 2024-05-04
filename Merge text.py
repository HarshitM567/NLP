import re

# Read the content of the file
with open('shakes_sorted.txt', 'r') as file:
    text = file.read()

# Extract words using regular expression
words = re.findall(r'\b\w+\b', text)

# Initialize a dictionary to store word frequencies
word_count = {}

# Count the occurrences of each word
for word in words:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1

# Print the merged and counted words
for word, count in word_count.items():
    print(f'{word}: {count}')
