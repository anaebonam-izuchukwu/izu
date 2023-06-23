# TODO calculate the area of a space to be painted
import math
Height = int(input("What's the height of the place "))
Width = int(input("What's the width of the place "))
Coverage = 5
Number_of_cans = (Height * Width) / Coverage
print(f"You will be needing {math.ceil(Number_of_cans)} cans of paint")