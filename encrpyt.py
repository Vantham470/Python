# Encryption program
import random
import string

chars = " " + string.punctuation + string.digits + string.ascii_letters
chars = list(chars)
key = chars.copy()

random.shuffle(key)

# print(f"chars: {chars}")
# print(f"key  : {key}")

# encrypt
plain_text= input("Enter a message to encrypt: ")
cipher_text = ""

for letter in plain_text:
    index = chars.index(letter)
    cipher_text += key[index]

print(f"original message : {plain_text}")
print(f"encrypt message  : {cipher_text}")

# Decrypt
cipher_text_input= input("Enter a message to decrypt: ")
decrypted_text = ""

for letter in cipher_text_input:
    index = key.index(letter)
    decrypted_text += chars[index]

print(f"encrypt message  : {cipher_text_input}")
print(f"original message : {decrypted_text}")
