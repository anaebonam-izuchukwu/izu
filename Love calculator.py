#Love Calculator
#step 1: Define your variables
print("Welcome to Love Calcualtor, be prepared to meet your destiny ")
name1 = input(" What's the boy's name? \n".lower())
name2 = input(" What's the girls's name? \n".lower())

com_name = name1 + name2
#Applied .count()function here to show the count of the character in the bracket
t = com_name.count('t')
r = com_name.count('r')
u = com_name.count('u')
e = com_name.count('e')

true_score = t + r + u + e

l = com_name.count('l')
o = com_name.count('o')
v = com_name.count('v')
e = com_name.count('e')

love_score = l + o + v + e 
#Used the str function to calculate the count as a string e.g 5+6=56 not 11
#used the int fucction to show the result as an interger for the logical operation to function
comapactable = int(str(true_score) + str(love_score))
#Our conditions for compatability
if comapactable < 10 or comapactable > 90:
    print(f"Your score is {comapactable}, and you are ok together ")
elif comapactable >= 40 and comapactable <= 50:
    print(f"Your score is {comapactable}, and you are ok ")
else:
    print(f"Your score is {comapactable}")


