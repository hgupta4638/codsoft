import random
import string

print("---Welcome to random password generator app!---")

letters_num = int(input("Enter how many letters want you add:"))
digits_num =  int(input("Enter how many digits want you add:"))
symbols_num = int(input("Enter how many symbols want you add:"))

letters = string.ascii_letters
numbers = string.digits
symbols = string.punctuation

password_list = []
for i in range(letters_num):
    password_list.append(random.choice(letters))
for i in range(digits_num):
    password_list.append(random.choice(numbers))
for i in range(symbols_num):
    password_list.append(random.choice(symbols))

random.shuffle(password_list)
password = " ".join(password_list)

print("Generated password :",password)