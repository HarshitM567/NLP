import re
# Read the content of the file
with open('shakes_modified.txt', 'r') as file:
    text = file.read()

# Extract words using regular expression
words = re.findall(r'\b\w+\b', text)

# Sort the words alphabetically
sorted_words = sorted(words)

# Write the sorted words back to the file
with open('shakes_sorted.txt', 'w') as file:
    for word in sorted_words:
        file.write(word + '\n')
