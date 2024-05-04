import nltk
from collections import Counter
from nltk.corpus import stopwords
import string

nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
nltk.download('stopwords')


# Function to preprocess text
def preprocess_text(text):
    # Tokenize the text into words
    words = nltk.word_tokenize(text.lower())

    # Remove stopwords and punctuation
    stop_words = set(stopwords.words('english'))
    words = [word for word in words if word not in stop_words and word not in string.punctuation]

    return words


# Function to calculate the probability of an n-gram being a noun or a verb
def calculate_probabilities(n_gram):
    tagged_ngram = nltk.pos_tag(n_gram)
    noun_count = 0
    verb_count = 0

    for word, tag in tagged_ngram:
        if tag.startswith('N'):
            noun_count += 1
        elif tag.startswith('V'):
            verb_count += 1

    total_count = noun_count + verb_count
    noun_probability = noun_count / total_count if total_count > 0 else 0
    verb_probability = verb_count / total_count if total_count > 0 else 0

    return noun_probability, verb_probability


# Function to find the most likely POS tag for an n-gram
def most_likely_pos(n_gram):
    tagged_ngram = nltk.pos_tag(n_gram)
    tag_counts = Counter(tag for word, tag in tagged_ngram)
    most_common_tag = tag_counts.most_common(1)
    return most_common_tag[0][0] if most_common_tag else None


# Function to read text from file
def read_text_from_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    return text


# Main function
def main():
    file_path = input("Enter the path to the input file: ")
    text = read_text_from_file('shakes.txt')

    n = int(input("Enter the value of n for n-gram: "))
    text_words = preprocess_text(text)

    n_grams = [text_words[i:i + n] for i in range(len(text_words) - n + 1)]

    for n_gram in n_grams:
        noun_probability, verb_probability = calculate_probabilities(n_gram)
        most_likely = most_likely_pos(n_gram)
        print(
            f"{' '.join(n_gram)} - Noun Probability: {noun_probability:.2f}, Verb Probability: {verb_probability:.2f}, Most Likely POS: {most_likely}")


if __name__ == "__main__":
    main()
