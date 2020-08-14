import random
import secrets
# import string


# A function do shuffle all the characters of a string
# def shuffle(string):
#     tempList = list(string)
#     random.shuffle(tempList)
#     new = ''.join(tempList)
#     return new




# Generating the password randint
uppercase = chr(random.randint(65, 90))
lowercase = chr(random.randint(97, 122))
number = chr(random.randint(48, 53))
special = chr(random.randint(32, 64))

# Generate password using all the characters, in random order
# password = ''
# password = shuffle(password)


def greet_msg():
    print("Welcome to cheezy random password generator")
    print("Put in the number of each character you want in your password")
    print(user_msg())


def user_msg():
    upper = int(input("How many upper case letters:"))
    lower = int(input("How many lower case letters:"))
    spec = int(input("How many special characters:"))
    num = int(input("How many numbers:"))
    return pass_gen(upper, lower, spec, num)


def pass_gen(upper, lower, spec, num):
    new_password = ''
    if (upper + lower + spec + num) < 6:
        print('Please enter minimum of 6 numbers.')
    else:
        for _ in range(upper):
            new_password += uppercase
            print('I want you ', new_password)
        for _ in range(lower):
            new_password += lowercase
            print('I hate you ' + new_password)
        for _ in range(spec):
            new_password += special
            print('hey ' + new_password)
        for _ in range(num):
            new_password += number
            print('hello ' + new_password)
        pass_word = list(new_password)
        random.shuffle(pass_word)
        new_pass = "". join(pass_word)
        return new_pass

greet_msg()


