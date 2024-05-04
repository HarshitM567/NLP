

import nltk

# Download the 'punkt' tokenizer data
nltk.download('punkt')
import random
from nltk.tokenize import word_tokenize

# Read Buckeye Corpus
with open("The_Buckeye_corpus_of_conversational_spe.txt", "r") as file:
    sentences = file.readlines()

# Select 50 random sentences
selected_sentences = random.sample(sentences, 50)

# Define a function to tokenize and transcribe words to ARPAbet
def transcribe_to_arpabet(word):
    # Write your code to transcribe word to ARPAbet here
    # You can use CMU Pronouncing Dictionary or any other resource
    # Return the ARPAbet transcription
    pass

unique_words = set()
arpabet_transcriptions = {}

# Process each selected sentence
for sentence in selected_sentences:
    words = word_tokenize(sentence)
    for word in words:
        # Ignore punctuation and special characters
        if word.isalpha():
            unique_words.add(word.lower())

# Transcribe unique words to ARPAbet
for word in unique_words:
    arpabet_transcriptions[word] = transcribe_to_arpabet(word)

# Print ARPAbet transcriptions
for word, arpabet in arpabet_transcriptions.items():
    print(f"{word}: {arpabet}")