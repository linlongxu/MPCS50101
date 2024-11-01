alphabet = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

# First function to encrypt a message
def caesar_encrypt(key, message):
    """Encrypt a message"""
    user_encrypt = ''
    for char in message.upper():
        if char in alphabet:
            new_encrypt = (alphabet.index(char) + key) % 26
            user_encrypt += alphabet[new_encrypt]
        else:
            user_encrypt += char
    return user_encrypt

# Second function to decrypt a message
def caesar_decrypt(key, message):
    """Decrypt a messaage"""
    user_decrypt = ''
    for char in message.upper():
        if char in alphabet:
            new_decrypt = (alphabet.index(char) - key) % 26
            user_decrypt += alphabet[new_decrypt]
        else:
            user_decrypt += char
    return user_decrypt

#Example
key = 12
message = "Experience is the teacher of all things"
encrypt_message = caesar_encrypt(key, message)
decrypt_message = caesar_decrypt(key, message)
print(f"The encrypted is: {encrypt_message}")
print(f"The decrypted is: {decrypt_message}")