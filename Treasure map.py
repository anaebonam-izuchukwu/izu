row1 = ["a" ,"b", "c"]
row2 = ["d", "e", "f"]
row3 = ["g", "h", "i"]
mapp = [ row1, row2, row3]

print(f"{row1}\n{row2}\n{row3}")
coordinate = input("Whats the row and column you're looking for ")
horizontal = int(coordinate[0])
vertical = int(coordinate[1])
mapp[vertical-1][horizontal-1]= "X"

print(f"{row1}\n{row2}\n{row3}")