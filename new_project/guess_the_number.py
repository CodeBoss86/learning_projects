from random import randint
# Creating a list of numbers
numbers = randint(0,20)
num_of_guess = 0
user = input("Hello what is your name?")
print("Hey " + user.title() + " guess a number from 1-20, you have only 3 tries.")
while num_of_guess < 3:
    guess = int(input())
    num_of_guess += 1
    if guess > numbers:
        print("your guess is too high")
    if guess < numbers:
        print("Your guess is too low")
    if guess > 20:
        print("Your guess isn't within the range.")
    if guess == numbers:
        break
if guess == numbers:
    print("You are correct, you got it in " + str(num_of_guess) + ' tries!')
else:
    print("You got it wrong, the number is " + str(numbers))


