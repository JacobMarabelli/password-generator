#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))
#------------------------------------------------------------------

#Fetch random letters and put into a list
rando_letters = []
for _ in range(nr_letters):
  rando_letters.append(random.choice(letters))

#Fetch random numbers and put into a list
rando_numbers = []
for _ in range(nr_numbers):
  rando_numbers.append(random.choice(numbers))
  
#Fetch random symbols and put into a list
rando_symbols = []
for _ in range(nr_symbols):
  rando_symbols.append(random.choice(symbols))

#Put previous lists into nested list and shuffle the order
password_list = [rando_letters, rando_numbers, rando_symbols]
random.shuffle(password_list)

#Create a random password with randomized order of letter, numbers, and symbols
print("Your password is: ")
for passwrd in password_list:
  print("".join(map(str, passwrd)), end="")