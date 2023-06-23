import random
print("Welcome to the password generator ")
letters = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '@', '#', '$', '%', '&', '_', '~']
num_letters = int(input("How many letters do you need: "))
num_numbers = int(input("How many numbers do you need: "))
num_symbols = int(input("How many symbols do you need: "))
password_l = []
for char in range(1,num_letters):
    password_l += random.choice(letters)
for char in range(1,num_numbers):
    password_l += random.choice(numbers)
for char in range(1,num_symbols):
    password_l += random.choice(symbols)
Your_password = random.shuffle(password_l)
Your_password = ""
for cah in password_l:
    Your_password += cah

print(f"Your password is {Your_password}")
 