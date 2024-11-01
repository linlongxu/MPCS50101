def check_email(email, index=0):
    if index >= len(email):
        return "Invalid email! Did not find @."
    elif email[index] == "@":
        return f"Valid email! Found @ at index {index}."
    else:
        return check_email(email, index + 1)

# Main
email = input("Enter an email: ")
print(check_email(email))
