import random
import string

#this is a simple code in python to generate passwords, you can modify the lenght at the (length=20) <==

def generate_password(length=20):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

if __name__ == "__main__":
    password = generate_password()
    print("Generated Password:", password)
