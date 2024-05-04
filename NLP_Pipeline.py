import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer, WordNetLemmatizer
import re
import os

nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')

# Function to tokenize and print the number of tokens
def tokenize_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
        tokens = word_tokenize(text)
        print("File:", os.path.basename(file_path))
        print("Number of tokens:", len(tokens))
        print("Tokens:", tokens)
        print()

# Function to filter words based on affixes
def filter_words(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
        tokens = word_tokenize(text)
        ed_ing_es_s = [word for word in tokens if word.endswith(('ed', 'ing', 'es', 's'))]
        un_in = [word for word in tokens if word.startswith(('un', 'in'))]
        print("File:", os.path.basename(file_path))
        print("Words ending with ed, ing, es, s:", ed_ing_es_s)
        print("Words starting with un, in:", un_in)
        print()

# Function to remove stop words
def remove_stopwords(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
        tokens = word_tokenize(text)
        print("File:", os.path.basename(file_path))
        print("Number of words before stopword removal:", len(tokens))
        filtered_tokens = [word for word in tokens if word.lower() not in stopwords.words('english')]
        print("Number of words after stopword removal:", len(filtered_tokens))
        print()

# Function to stem words
def stem_words(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
        tokens = word_tokenize(text)
        print("File:", os.path.basename(file_path))
        print("Number of words before stemming:", len(tokens))
        stemmer = PorterStemmer()
        stemmed_tokens = [stemmer.stem(word) for word in tokens]
        print("Number of words after stemming:", len(stemmed_tokens))
        print()

# Function to lemmatize words
def lemmatize_words(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
        tokens = word_tokenize(text)
        print("File:", os.path.basename(file_path))
        print("Number of words before lemmatization:", len(tokens))
        lemmatizer = WordNetLemmatizer()
        lemmatized_tokens = [lemmatizer.lemmatize(word) for word in tokens]
        print("Number of words after lemmatization:", len(lemmatized_tokens))
        print()

# Function to find and replace common abbreviations
def replace_abbreviations(file_path):
    abbreviations = {'i.e.': 'that is', 'e.g.': 'for example', 'u.s.': 'United States'}
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
        for abbreviation, replacement in abbreviations.items():
            matches = re.findall(r'\b' + re.escape(abbreviation) + r'\b', text, flags=re.IGNORECASE)
            if matches:
                print("Abbreviation:", abbreviation)
                print("Found in file:", os.path.basename(file_path))
                print()

# Function to find words with special symbols using regular expressions
def find_special_symbols(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
        special_symbols = re.findall(r'\b\S*[$%\'"#]+\S*\b', text)
        if special_symbols:
            print("Special symbols found in file:", os.path.basename(file_path))
            print("Special symbols:", special_symbols)
            print()

# Path to the directory containing BBC news dataset files
data_dir = r'D:\NLP\bbc_news.txt'  # Raw string literal

# Perform tasks on each file in the dataset
for file in os.listdir(data_dir):
    file_path = os.path.join(data_dir, file)
    tokenize_file(file_path)
    filter_words(file_path)
    remove_stopwords(file_path)
    stem_words(file_path)
    lemmatize_words(file_path)
    replace_abbreviations(file_path)
    find_special_symbols(file_path)

