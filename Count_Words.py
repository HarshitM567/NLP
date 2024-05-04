import re

def count_total_words(file_path):
    with open(file_path, 'r') as file:
        text = file.read()
        words = re.findall(r'\b\w+\b', text)
        return len(words)

def count_word(file_path, word):
    with open(file_path, 'r') as file:
        text = file.read()
        occurrences = re.findall(r'\b{}\b'.format(word), text)
        return len(occurrences)

def count_word_followed_by(file_path, word, following_word, following_pos):
    with open(file_path, 'r') as file:
        text = file.read()
        pattern = r'\b{}\b {} {}'.format(word, following_word, following_pos)
        occurrences = re.findall(pattern, text)
        return len(occurrences)

def calculate_probability(count, total_words):
    return count / total_words

def main():
    file_path = 'shakes.txt'
    total_words = count_total_words(file_path)
    word = 'race'
    w_count = count_word(file_path, word)
    w_probability = calculate_probability(w_count, total_words)

    w1 = 'NN'
    w_followed_by_w1_count = count_word_followed_by(file_path, word, w1, following_pos='NN')
    w_followed_by_w1_probability = calculate_probability(w_followed_by_w1_count, total_words)

    w2 = 'VB'
    w_followed_by_w2_count = count_word_followed_by(file_path, word, w2, following_pos='VB')
    w_followed_by_w2_probability = calculate_probability(w_followed_by_w2_count, total_words)

    print("Total number of words:", total_words)
    print("Count of word '{}':".format(word), w_count)
    print("Probability of word '{}':".format(word), w_probability)
    print("Count of '{}' followed by '{}':".format(word, w1), w_followed_by_w1_count)
    print("Probability of '{}' followed by '{}':".format(word, w1), w_followed_by_w1_probability)
    print("Count of '{}' followed by '{}':".format(word, w2), w_followed_by_w2_count)
    print("Probability of '{}' followed by '{}':".format(word, w2), w_followed_by_w2_probability)

if __name__ == "__main__":
    main()