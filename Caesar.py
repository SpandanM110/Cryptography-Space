def encrypt(plaintext, n):
    sol = ""

    for i in range(len(plaintext)):
        ch = plaintext[i]

        if ch == ' ':
            sol += " "
        elif ch.isupper():
            sol += chr((ord(ch) + n - 65) % 26 + 65)
        else:
            sol += chr((ord(ch) + n - 97) % 26 + 97)

    return sol


def decrypt(ciphertext, n):
    sol = ""

    for i in range(len(ciphertext)):
        ch = ciphertext[i]

        if ch == ' ':
            sol += " "
        elif ch.isupper():
            sol += chr((ord(ch) - n - 65) % 26 + 65)
        else:
            sol += chr((ord(ch) - n - 97) % 26 + 97)

    return sol


plaintext = input("Enter the plain text: ")
n = int(input("Enter the shift value: "))

encrypted_text = encrypt(plaintext, n)
print("Encrypted text:", encrypted_text)

decrypted_text = decrypt(encrypted_text, n)
print("Decrypted text:", decrypted_text)
