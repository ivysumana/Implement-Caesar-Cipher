# Caesar Cipher implementation in Python

def caesar_encrypt(message, shift):
    """
    Encrypts a message using the Caesar Cipher algorithm.

    :param message: The message to encrypt
    :param shift: The shift value to use for encryption
    :return: The encrypted message
    """
    encrypted_message = ""
    for char in message:
        if char.isalpha():
            ascii_offset = 65 if char.isupper() else 97
            encrypted_char = chr((ord(char) - ascii_offset + shift) % 26 + ascii_offset)
            encrypted_message += encrypted_char
        else:
            encrypted_message += char
    return encrypted_message

def caesar_decrypt(encrypted_message, shift):
    """
    Decrypts an encrypted message using the Caesar Cipher algorithm.

    :param encrypted_message: The encrypted message to decrypt
    :param shift: The shift value used for encryption
    :return: The decrypted message
    """
    decrypted_message = ""
    for char in encrypted_message:
        if char.isalpha():
            ascii_offset = 65 if char.isupper() else 97
            decrypted_char = chr((ord(char) - ascii_offset - shift) % 26 + ascii_offset)
            decrypted_message += decrypted_char
        else:
            decrypted_message += char
    return decrypted_message

def main():
    print("Caesar Cipher Program")
    print("---------------------")

    while True:
        print("Options:")
        print("1. Encrypt a message")
        print("2. Decrypt a message")
        print("3. Quit")

        choice = input("Enter your choice: ")

        if choice == "1":
            message = input("Enter the message to encrypt: ")
            shift = int(input("Enter the shift value: "))
            encrypted_message = caesar_encrypt(message, shift)
            print(f"Encrypted message: {encrypted_message}")
        elif choice == "2":
            encrypted_message = input("Enter the encrypted message to decrypt: ")
            shift = int(input("Enter the shift value used for encryption: "))
            decrypted_message = caesar_decrypt(encrypted_message, shift)
            print(f"Decrypted message: {decrypted_message}")
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()