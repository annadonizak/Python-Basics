university = "Krakow University of Economics"

# Split the university name into words
words = university.split()

# List of words to skip (e.g., "of", "the", "and", etc.)
skip_words = {"of", "the", "and", "in", "for"}

# Create an abbreviation by taking the first letter of each word, skipping certain words
abbreviation = ''.join([word[0].upper() for word in words if word.lower() not in skip_words])

# Print the abbreviation
print(abbreviation)


