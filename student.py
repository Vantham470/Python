import json
import os

DATA_FILE = "students.json"


def load_students():
    """Load students from JSON file."""
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE, "r") as file:
        return json.load(file)


def save_students(students):
    """Save students to JSON file."""
    with open(DATA_FILE, "w") as file:
        json.dump(students, file, indent=4)


def add_student(students):
    """Add a new student."""
    student_id = input("Enter student ID: ")
    name = input("Enter name: ")

    try:
        age = int(input("Enter age: "))
    except ValueError:
        print("Invalid age. Please enter a number.")
        return

    major = input("Enter major: ")

    students.append({
        "id": student_id,
        "name": name,
        "age": age,
        "major": major
    })

    print("Student added successfully!")


def view_students(students):
    """Display all students."""
    if not students:
        print("No students found.")
        return

    for s in students: # s = student
        print(f"{s['id']} | {s['name']} | {s['age']} | {s['major']}")


def main():
    students = load_students()

    while True:
        print("\n===== Student Management System =====")
        print("1. Add Student")
        print("2. View All Students")
        print("3. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            add_student(students)
        elif choice == "2":
            view_students(students)
        elif choice == "3":
            save_students(students)
            print("Goodbye!")
            break
        else:
            print("Invalid option. Try again.")


if __name__ == "__main__":
    main()

# first choice 

def caesar_encrypt(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            start = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - start + shift) % 26 + start)
        else:
            result += char
    return result


def caesar_decrypt(text, shift):
    return caesar_encrypt(text, -shift)


# Main Program
message = input("Enter your message: ")
shift = int(input("Enter shift number: "))

encrypted = caesar_encrypt(message, shift)
print("Encrypted:", encrypted)

decrypted = caesar_decrypt(encrypted, shift)
print("Decrypted:", decrypted)

# second choice 
# Caesar Cipher Program

import string

def encrypt(text, shift):
    result = ""
    for letter in text:
        if letter.isalpha():
            start = ord('A') if letter.isupper() else ord('a')                # ord() converts letter ➜ number
            result += chr((ord(letter) - start + shift) % 26 + start)         # chr() converts number ➜ letter 
        else:
            result += letter
    return result


def decrypt(text, shift):
    return encrypt(text, -shift)


# Main Program
shift = int(input("Enter shift value: "))

plain_text = input("Enter a message to encrypt: ")
cipher_text = encrypt(plain_text, shift)

print(f"Original message : {plain_text}")
print(f"Encrypted message: {cipher_text}")

cipher_text_input = input("Enter a message to decrypt: ")
decrypted_text = decrypt(cipher_text_input, shift)

print(f"Encrypted message: {cipher_text_input}")
print(f"Original message : {decrypted_text}")