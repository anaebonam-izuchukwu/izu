# A simple text game called treasure Island
print(" Welcome to Treasure Island ")
print(" Your mission if you choose to accept is to find the treasure ")
print(" For this game just type left or right ")
print(" Lets begin ")
print(" left or right")
decisions = ['left', 'right', 'swim', 'wait', 'red', 'blue', 'yellow']
value1 = input("What way " )
if  value1 == decisions[0]:
    print(" swim or wait ")
    value2 = input("What way  " )
    if value2 == decisions[2]:
        print(" Which door, red or blue or yellow")
        value3 = input("What way  " )
        if value3 == decisions[5]:
            print(" You win ")
        elif value3 == decisions[4]:
            print("You've entered fire, game over")
        elif value3 == decisions[6]:
            print("You've entered a hole, game over")
    else:
        print("You've drowned, game over")

else:
    print(" Game Over ")
    