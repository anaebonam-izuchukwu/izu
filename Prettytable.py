from prettytable import PrettyTable
Table = PrettyTable()
 
Table.add_column("City Name", ["fin", "bin", "man"]) 
Table.add_column("States",["asaba","gave","tree"])

Table.align = "r"
print(Table)