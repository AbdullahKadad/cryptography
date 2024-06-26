def encrypt(text, key):
    """
    Encrypts the given text using a simple Caesar cipher.
    
    :param text: The plaintext string to encrypt.
    :param key: The integer key for the Caesar cipher.
    :return: The encrypted ciphertext.
    """
    encrypted_text = ''.join(chr((ord(char) + key - 65) % 26 + 65) if char.isupper() else chr((ord(char) + key - 97) % 26 + 97) for char in text)
    return encrypted_text

def decrypt(text, key):
    """
    Decrypts the given text using a simple Caesar cipher.
    
    :param text: The ciphertext string to decrypt.
    :param key: The integer key for the Caesar cipher.
    :return: The decrypted plaintext.
    """
    decrypted_text = ''.join(chr((ord(char) - key - 65) % 26 + 65) if char.isupper() else chr((ord(char) - key - 97) % 26 + 97) for char in text)
    return decrypted_text

if __name__ == "__main__":
    # Test encryption
    plaintext = "HelloWorld"
    key = 3
    encrypted_text = encrypt(plaintext, key)
    print(f"Encrypted Text: {encrypted_text}")  # Expected: "KhoorZruog"

    # Test decryption
    decrypted_text = decrypt(encrypted_text, key)
    print(f"Decrypted Text: {decrypted_text}")  # Expected: "HelloWorld"