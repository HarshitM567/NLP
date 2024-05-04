
#Harshit Mittal
#21BAI10058
# Define the prefixes to search for
prefixes = ["un", "re", "in", "pre", "ir"]

# Read the content of the file
with open("shakes.txt", "r") as file:
    content = file.read()

# Split the content into words
words = content.split()

# Initialize dictionaries to store words with specific prefixes
words_with_prefixes = {prefix: [] for prefix in prefixes}

# Iterate through each word and check for the specified prefixes
for word in words:
    for prefix in prefixes:
        if word.startswith(prefix):
            words_with_prefixes[prefix].append(word)

# Print the words starting with each prefix
for prefix, word_list in words_with_prefixes.items():
    print(f"Words starting with '{prefix}':")
    print(", ".join(word_list))
    print()