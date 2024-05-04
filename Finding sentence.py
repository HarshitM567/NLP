# Read content of the file
with open('shakes.txt', 'r') as file:
    text = file.read()

# Define punctuation marks to search for
punctuation_marks = ['!', '?', '%', '.']

# Function to find sentences ending with a specific punctuation mark
def find_sentences(text, ending):
    sentences = []
    sentence = ""
    for char in text:
        sentence += char
        if char in punctuation_marks:
            if char == ending:
                sentences.append(sentence.strip())
            sentence = ""
    return sentences

# Find and print sentences ending with each punctuation mark
for ending in punctuation_marks:
    sentences = find_sentences(text, ending)
    print(f"Sentences ending with '{ending}':")
    for sentence in sentences:
        print(sentence)
