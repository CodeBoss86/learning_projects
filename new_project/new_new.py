import random
import secrets
import string

uppercase = string.ascii_uppercase
lowercase = string.ascii_lowercase
number = string.digits
special = string.punctuation


def greetings():
    print("Welcome to cheezy password random generator.")
    print("Enter the number of each character you want in your password.")
    print(ask_user())


def ask_user():
    upper = int(input("How many upper case do you want?"))
    lower = int(input("How many lower case do you want?"))
    spec = int(input("How many special case do you want?"))
    num = int(input("How many number do you want?"))
    return generate_password(upper, lower, spec, num)


def generate_password(upper, lower, spec, num):
    password = ''
    if (upper + lower + spec + num) < 6:
        print('You can only generate password of 6 minimum character')
    else:
        for _ in range(upper):
            password += secrets.choice(uppercase)
        for _ in range(lower):
            password += secrets.choice(lowercase)
        for _ in range(spec):
            password += secrets.choice(special)
        for _ in range(num):
            password += secrets.choice(number)
        new_password = list(password)
        random.shuffle(new_password)
        new_pass = ''.join(new_password)
        return new_pass


greetings()