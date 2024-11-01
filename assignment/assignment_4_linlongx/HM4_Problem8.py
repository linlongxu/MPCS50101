import random

def select_random_word():
    with open("/Users/simpson/Desktop/MPCS/assignment/assignment_4_linlongx/common_words.txt") as file:
        words = [line.strip() for line in file]
    return random.choice(words).upper()

def display_progress(word, guesses):
    return " ".join([letter if letter in guesses else "_" for letter in word])

def play_hangman():
    word = select_random_word()
    guesses = set()
    attempts = 5

    print("Let's Play Hangman")

    while attempts > 0:
        print(display_progress(word, guesses))
        guess = input("Guess a letter: ").upper()

        if guess in guesses:
            print("You already guessed that letter.")
            continue

        guesses.add(guess)

        if guess in word:
            print(f"{guess} is in the word.")
            if set(word).issubset(guesses):
                print(f"Congratulations! The word was {word}.")
                return
        else:
            attempts -= 1
            print(f"{guess} is not in the word. You have {attempts} guesses remaining.")

    print(f"You've run out of guesses. The word was {word}.")

play_hangman()