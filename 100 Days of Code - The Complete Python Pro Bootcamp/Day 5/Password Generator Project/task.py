letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

import random
password = ""

for l in range(1,nr_letters + 1):
    letter = random.choice(letters)
    password += f"{letter}"
for n in range(1,nr_numbers + 1):
    number = random.choice(numbers)
    password += f"{number}"
for s in range(1, nr_symbols + 1):
    symbol = random.choice(symbols)
    password += f"{symbol}"

# Convert the string to a list of characters
char_list = list(password)

# Shuffle the list
random.shuffle(char_list)

# Join the characters back into a string
password = ''.join(char_list)

print(f"Your password is: {password}.")


