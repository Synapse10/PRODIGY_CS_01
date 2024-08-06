def caesar_cipher_encrypt(text, shift):
    encrypted_message = ""
    for ch in text:
        if ch.isalpha():
            start = ord('A') if ch.isupper() else ord('a')
            new_char = chr((ord(ch) - start + shift) % 26 + start)
            encrypted_message += new_char
        else:
            encrypted_message += ch
    return encrypted_message


def caesar_cipher_decrypt(text, shift):
    return caesar_cipher_encrypt(text, -shift)


def main():
    while True:
        print("\nCaesar Cipher Program")
        print("1. Encrypt a message")
        print("2. Decrypt a message")
        print("3. Exit")

        choice = input("Choose an option: ").strip()

        if choice == '1':
            message = input("Enter the message to be encrypted: ").strip()
            shift = int(input("Enter the key (shift value): "))
            encrypted_message = caesar_cipher_encrypt(message, shift)
            print(f"Encrypted Message: {encrypted_message}")

        elif choice == '2':
            encrypted_message = input("Enter the message to be decrypted: ").strip()
            shift = int(input("Enter the key (shift value): "))
            decrypted_message = caesar_cipher_decrypt(encrypted_message, shift)
            print(f"Decrypted Message: {decrypted_message}")

        elif choice == '3':
            print("Exiting the program.")
            break

        else:
            print("Invalid choice. Please choose a valid option.")


if __name__ == "__main__":
    main()
