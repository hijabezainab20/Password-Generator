import random
import string

print("=== Strong Password Generator ===")

while True:
    length = int(input("Enter password length: "))

    characters = string.ascii_letters + string.digits + string.punctuation

    password = ''.join(random.choice(characters) for _ in range(length))

    print("\nGenerated Password:")
    print(password)

    choice = input("\nGenerate another password? (y/n): ")

    if choice.lower() != 'y':
        print("Thank you for using Password Generator!")
        break