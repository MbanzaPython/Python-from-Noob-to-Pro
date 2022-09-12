import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

Password = []

for lettersAmount in range(0, nr_letters):
  randomLetter = random.randint(0, len(letters) - 1)
  Password.append(letters[randomLetter])

for symbolsAmount in range(0, nr_symbols):
  randomSymbol = random.randint(0, len(symbols) - 1)
  Password.append(symbols[randomSymbol])

for numbersAmount in range(0, nr_numbers):
  randomNumber = random.randint(0, len(numbers) - 1)
  Password.append(numbers[randomNumber])

random.shuffle(Password)
print("Here is your password: ", end = "")
print("".join(Password))