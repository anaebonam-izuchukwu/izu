import random
test_para = int(input(" Write down your seed number: "))
random.seed(test_para)
random_var = random.randint( 0, 1)
if random_var == 1:
    print("Heads")
else:
    print("Tails")
