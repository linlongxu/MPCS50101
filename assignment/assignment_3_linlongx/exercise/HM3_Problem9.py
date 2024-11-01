import string
from collections import Counter

def load_common_words(filename):
    with open(filename, 'r') as file:
        return set(word.strip().lower() for word in file.readlines())

def count_word_frequency(speech_filename, common_words_filename):
    # Load common words
    common_words = load_common_words(common_words_filename)

    # Read the speech file
    with open(speech_filename, 'r') as file:
        speech = file.read().lower()  # Convert to lowercase

    # Clean up text
    translator = str.maketrans('', '', string.punctuation)
    cleaned_speech = speech.translate(translator)

    # Split into words
    words = cleaned_speech.split()
    filtered_words = [word for word in words if word not in common_words]

    # Count frequencies
    word_count = Counter(filtered_words)

    # Get the 20 most common words
    most_common = word_count.most_common(20)

    # Print results
    for word, count in most_common:
        print(f"{word} - {count}")

    # Write the results
    with open('word_frequency_output.txt', 'w') as output_file:
        for word, count in most_common:
            output_file.write(f"{word} - {count}\n")

count_word_frequency('/Users/simpson/Desktop/MPCS/assignment/assignment_3_linlongx/exercise/speech.txt', 
                     '/Users/simpson/Desktop/MPCS/assignment/assignment_3_linlongx/exercise/common_words.txt')