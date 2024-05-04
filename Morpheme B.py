#Harshit Mittal
#21BAI10058
import re

# Read the file
with open('shakes.txt', 'r') as file:
    text = file.read()

# Define a function to find morpheme pairs
def find_morpheme_pairs(text):
    # Define regex pattern for word pairs with the same root but different inflections
    pattern = r'\b(\w+)(\w{2,})-(\1)(\w{2,})\b'

    # Find all matches
    morpheme_pairs = re.findall(pattern, text)

    return morpheme_pairs

# Get morpheme pairs
morpheme_pairs = find_morpheme_pairs(text)

# Print the morpheme pairs found
for pair in morpheme_pairs:
    print(f"{pair[0]}{pair[1]}-{pair[2]}{pair[3]}")