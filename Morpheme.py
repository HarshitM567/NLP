#Harshit Mittal
#21BAI10058
import re

# Read the file
with open('shakes.txt', 'r', encoding='utf-8') as file:
    text = file.read()

# Define regular expressions for inflectional morphemes
s_pattern = r'\b\w+s\b'
es_pattern = r'\b\w+es\b'
ing_pattern = r'\b\w+ing\b'
ed_pattern = r'\b\w+ed\b'

# Find words with each inflectional morpheme
s_words = re.findall(s_pattern, text)
es_words = re.findall(es_pattern, text)
ing_words = re.findall(ing_pattern, text)
ed_words = re.findall(ed_pattern, text)

# Print the words found with each inflectional morpheme
print("Words with inflectional morpheme 's':", s_words)
print("Words with inflectional morpheme 'es':", es_words)
print("Words with inflectional morpheme 'ing':", ing_words)
print("Words with inflectional morpheme 'ed':", ed_words)