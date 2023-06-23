import random
random_seed = int(input(" Put in a random number "))
random.seed(random_seed)

payers_list = input(" Everyone input your names separated by a comma  ")
names = payers_list.split(",")
num_items = len(names)
choicce = (random.randint(0 ,num_items-1))
payer = names[choicce]
print(f"{payer}, would be paying for this dinner")