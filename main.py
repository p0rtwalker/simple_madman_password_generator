import random
import string

#this is a simple code in python to generate passwords 

def generate_password(length=20): #<== here you can modify the length or the password to be generated
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

if __name__ == "__main__":
    password = generate_password()
    print("Generated Password:", password)
