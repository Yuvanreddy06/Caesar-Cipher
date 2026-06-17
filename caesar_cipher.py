def encrypt_char(char, shift):
    if char.isalpha():
        base = ord('A') if char.isupper() else ord('a')
        return chr((ord(char) - base + shift) % 26 + base)
    return char

def encrypt(message, shift):
    return ''.join(encrypt_char(c, shift) for c in message)

def decrypt(message, shift):
    return encrypt(message, -shift)

def brute_force(message):
    print("\n--- Brute Force: All Possible Shifts ---")
    for shift in range(1, 26):
        print(f"Shift {shift:2}: {decrypt(message, shift)}")

def main():
    print("=== Caesar Cipher ===")
    while True:
        print("\n1. Encrypt")
        print("2. Decrypt")
        print("3. Brute Force Crack")
        print("4. Quit")
        choice = input("\nEnter choice (1/2/3/4): ").strip()

        if choice == '1':
            message = input("Enter message to encrypt: ")
            shift = int(input("Enter shift value (1-25): ")) % 26
            print(f"Encrypted: {encrypt(message, shift)}")

        elif choice == '2':
            message = input("Enter message to decrypt: ")
            shift = int(input("Enter shift value (1-25): ")) % 26
            print(f"Decrypted: {decrypt(message, shift)}")

        elif choice == '3':
            message = input("Enter encrypted message to crack: ")
            brute_force(message)

        elif choice == '4':
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please enter 1, 2, 3, or 4.")

main()
