import random
print("This is a rock, paper, scissors game just select one and hope you win")
rock = 0
paper = 1
scissors = 2
user1 = int(input (" Type 0 for Rock, 1 for paper and 2 for scissors\n"))
comput = random.randint(0,2)
print (f"The computer choose {comput} ")

if user1 < comput :
    print("wins")
elif user1  > comput:
    print("lose")
elif comput == user1 :
    print("Draw")
