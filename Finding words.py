import re

def find_words_with_regex(file_path, pattern):
    with open(file_path, 'r') as file:
        text = file.read()
        matches = re.findall(pattern, text)
        return matches

file_path = "shakes.txt"

# Regular expressions for words ending with !, ?, %, and .
patterns = {
    'Exclamation': r'\b\w+!',
    'Question': r'\b\w+\?',
    'Percentage': r'\b\w+%',
    'Period': r'\b\w+\.'
}

for name, pattern in patterns.items():
    print(f"Words ending with {name}:")
    matches = find_words_with_regex(file_path, pattern)
    print(matches)
