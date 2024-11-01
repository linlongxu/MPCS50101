#Problem 6
P_6 = True
while P_6:
    try:
        word_phrase = input("Please enter a word or phrase: ")
        clean_word_phrase = word_phrase.lower()

        if any(char.isdigit() or char.isspace() for char in word_phrase):
            raise ValueError("Input contains numbers or spaces, which are not allowed.")

        i = 0
        n = len(clean_word_phrase) - 1

        is_palindromes = True

        while i < n:
            if clean_word_phrase[i] != clean_word_phrase[n]:
                is_palindromes = False
                break
            i += 1
            n -= 1

        if is_palindromes:
            print ("It is palindrome.")
        else:
            print ("It isn't palindrome.")

    except Exception:
        print("Please enter a valid word or phrase.")