#Problem 3

P_3 = True

while P_3:

    pass_word = input("Enter a password: ")

    if len(pass_word)>=12:

        has_digit = any(char.isdigit() for char in pass_word)
        has_letters = any(char.isalpha() for char in pass_word)

        special_characters = ["!", "@", "#", "$", "%"]
        has_special_characters = any(char in special_characters for char in pass_word)

        has_upper = any(char.isupper() for char in pass_word)
        has_lower = any(char.islower() for char in pass_word)

        if has_digit and has_letters and has_special_characters and has_upper and has_lower:
            print ("This is a strong password :)")

        else:
            print ("""
        This is not a strong password :)
        Please have at least 12 characters
        Contains both numbers and letters
        Contains at least one of the following characters: !,@,#,$,%
        Contains at least one capital letter and one lower-case letter
        """)

    else:
        print ("""
        This is not a strong password :)
        Please have at least 12 characters
        Contains both numbers and letters
        Contains at least one of the following characters: !,@,#,$,%
        Contains at least one capital letter and one lower-case letter
        """)