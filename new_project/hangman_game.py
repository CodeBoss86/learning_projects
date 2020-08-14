import csv
import random


filename = "word.csv"
lines = []
with open(filename) as csv_file:
    csv_reader = csv.reader(csv_file)
    for line in csv_reader:
        lines.append(line[0])


def greet_user():
    print('Welcome to gift guess game.')
    name = (input("What is your name?"))
    print("Hey " + name.title() + ' I have a word, guess any letter in it.')
    print("You have only 6 tries. Good luck!")
    return ask_user()


def ask_user():
    print('\nPlease enter your guess')
    num_of_guess = 0
    answer = random.choice(lines)
    while num_of_guess < 6:
        user_input = input()
        num_of_guess += 1
        if user_input.upper() in answer:
            print("you are correct, you got it in " + str(num_of_guess) + ' tries.')
            print("The word is " + ''.join(answer))
            correct = True
            break
        else:
            print("Wrong, try again.")
            correct = False

    if correct == False:
        print("You are wrong, the letter in the word are " + "".join(answer))


greet_user()
