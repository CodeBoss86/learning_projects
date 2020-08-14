list_of_num = []
numbers = range(0, 101, 2)
for number in numbers:
    list_of_num.append(number)
length = len(list_of_num)


def greet_user():
    name = input("What is your name?")
    print("Hello," + name + 'I have a list of number range from 1-100, guess a number from the list.')
    digit = int(input('Enter number'))
    return search(list_of_num, digit)


def search(numbs, digit):
    first = 0
    last = length - 1
    found = False
    while first <= last and not found:
        mid = (first + last)//2
        if numbs[mid] == digit:
            found = True
        elif numbs[mid] > digit:
            last = mid-1
        else:
            first = mid + 1
    if found:
        return 'correct ' + str(digit) + ' is in list.'
    else:
        return str(digit) + ' is not in list'


while True:
    print(greet_user())





