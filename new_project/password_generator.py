import random
# A function do shuffle all the characters of a string


def shuffle(string):
  tempList = list(string)
  random.shuffle(tempList)
  return ''.join(tempList)

# Generating the password


uppercaseLetter1 = chr(random.randint(65, 90))
uppercaseLetter2 = chr(random.randint(65, 90))
lowercaseLetter1 = chr(random.randint(97, 122))
lowercaseLetter2 = chr(random.randint(97, 122))
digit1 = chr(random.randint(48, 53))
digit2 = chr(random.randint(48, 53))
symbol1 = chr(random.randint(32, 64))
symbol2 = chr(random.randint(32,64))
# Generate more characters

# Generate password using all the characters, in random order
password1 = uppercaseLetter2 + lowercaseLetter1 + lowercaseLetter2 + digit1 + digit2 + symbol1
password2 = uppercaseLetter1 + uppercaseLetter2 + lowercaseLetter1 + lowercaseLetter2 + digit1 + digit2 + symbol1
password3 = uppercaseLetter1 + uppercaseLetter2 + lowercaseLetter1 + lowercaseLetter2 + digit1 + digit2 + symbol1 + symbol2
password1 = shuffle(password1)
password2 = shuffle(password2)
password3 = shuffle(password3)
print("\nHello, how many character password do you want?")
user = int(input())
if user == 6:
    print(password1)
elif user == 7:
    print(password2)
elif user == 8:
    print(password3)
else:
    print("You can only generate 6-8 character password.")



