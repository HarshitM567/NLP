import re

# Read the content of the file
with open('shakes.txt', 'r') as file:
    text = file.read()

# Define the regular expression pattern
pattern = r'[^a-zA-Z\n]'

# Replace non-alphabetic characters with newlines
text_with_newlines = re.sub(pattern, '\n', text)

# Write the modified text back to the file
with open('shakes_modified.txt', 'w') as file:
    file.write(text_with_newlines)
