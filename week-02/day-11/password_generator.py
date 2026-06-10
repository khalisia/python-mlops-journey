import random


def generate_password(length):
    characters =  ("abcdefghijklmnopqrstuvwxyz"
                    "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
                    "0123456789"
                    "!@#$%^&*")

    password = ""

    for _ in range(length):
        password += random.choice(characters)

    return password


length = int(input("Password length: "))

for _ in range(5):
    print(generate_password(length))