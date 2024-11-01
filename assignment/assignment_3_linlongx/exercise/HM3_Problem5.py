# Define the alphabet
alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

# Function to encrypt a message
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

# Function to decrypt a message
def caesar_decrypt(key, message):
    """Decrypt a message"""
    user_decrypt = ''
    for char in message.upper():
        if char in alphabet:
            new_decrypt = (alphabet.index(char) - key) % 26
            user_decrypt += alphabet[new_decrypt]
        else:
            user_decrypt += char
    return user_decrypt

# Function to crack the Caesar Cipher
def crack_caesar_cipher(ciphertext):
    for key in range(1, 26):  # Try all possible shifts from 1 to 25
        decrypted_message = caesar_decrypt(key, ciphertext)
        print(f"Shift {key}: {decrypted_message}")

# Encrypted message
ciphertext = "mpwtpgp jzf nly lyo jzf lcp slwqhlj espcp"

# Crack the cipher
print("Cracking the Caesar Cipher:")
crack_caesar_cipher(ciphertext)