def caesar_cipher_encrypt(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():  # Check if character is an alphabet
            shifted = ord(char) + shift
            if char.islower():
                if shifted > ord('z'):
                    shifted = shifted - 26
                elif shifted < ord('a'):
                    shifted = shifted + 26
            elif char.isupper():
                if shifted > ord('Z'):
                    shifted = shifted - 26
                elif shifted < ord('A'):
                    shifted = shifted + 26
            encrypted_text += chr(shifted)
        else:
            encrypted_text += char  # Non-alphabet characters remain unchanged
    return encrypted_text

def caesar_cipher_decrypt(text, shift):
    return caesar_cipher_encrypt(text, -shift)  # Decryption is simply encryption with negative shift

def main():
    choice = input("Do you want to encrypt or decrypt? (encrypt/decrypt): ").lower()
    if choice not in ['encrypt', 'decrypt']:
        print("Invalid choice. Please choose either 'encrypt' or 'decrypt'.")
        return

    message = input("Enter your message: ")
    shift = int(input("Enter the shift value (a positive integer): "))

    if choice == 'encrypt':
        encrypted_message = caesar_cipher_encrypt(message, shift)
        print(f"Encrypted message: {encrypted_message}")
    elif choice == 'decrypt':
        decrypted_message = caesar_cipher_decrypt(message, shift)
        print(f"Decrypted message: {decrypted_message}")

if __name__ == "__main__":
    main()
