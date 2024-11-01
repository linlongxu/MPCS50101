def check_email(user_email):
    for index, char in enumerate(user_email):
        if char == "@":
            return f"Valid email, find @ at {index}."
    return f"Invalid email, please include @"
        
user_email = input("Please enter your email: ")
print(check_email(user_email))