import re

# Read the contents of the file
with open('shakes.txt', 'r') as file:
    text = file.read()

# Define a regular expression pattern to match sentences starting with "with."
pattern = r'\bwith\.\s+[A-Z]'

# Find all matches
matches = re.findall(pattern, text)

# Total number of sentences in the text
total_sentences = len(re.findall(r'[A-Z][^.!?]*[.!?]', text))

# Number of sentences starting with "with."
sentences_with_with = len(matches)

# Probability calculation
if total_sentences > 0:
    probability = sentences_with_with / total_sentences
else:
    probability = 0

print("Total Sentences:", total_sentences)
print("Sentences starting with 'with.':", sentences_with_with)
print("Probability:", probability)
