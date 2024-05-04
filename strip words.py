import re

# Step 1: Read the content of the file
with open('shakes_sorted.txt', 'r') as file:
    text = file.read()

# Step 2: Identify words ending with "ing" having vowels before "ing"
pattern = r'\b(\w*?[aeiouAEIOU])ing\b'

# Step 3: Strip "ing" from words
modified_text = re.sub(pattern, r'\1', text)

# Step 4: Write the modified text back to the file
with open('shakes_stripped.txt', 'w') as file:
    file.write(modified_text)
