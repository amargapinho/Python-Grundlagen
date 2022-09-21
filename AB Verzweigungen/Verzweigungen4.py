niederschlagsmenge1 = int(input("Niederschalgsmenge 1:"))
niederschlagsmenge2 = int(input("Niederschalgsmenge 2:"))
niederschlagsmenge3 = int(input("Niederschalgsmenge 3:"))
niederschlagsmenge4 = int(input("Niederschalgsmenge 4:"))
niederschlagsmenge5 = int(input("Niederschalgsmenge 5:"))

kleinsteNiederschlagsmenge = min(niederschlagsmenge1, niederschlagsmenge2, niederschlagsmenge3, niederschlagsmenge4, niederschlagsmenge5)
groessteNiederschlagsmenge = max(niederschlagsmenge1, niederschlagsmenge2, niederschlagsmenge3, niederschlagsmenge4, niederschlagsmenge5)

print("Die größte der eingegebenen Niederschlagsmenge ist", groessteNiederschlagsmenge, 
"und die kleinste der eingegebenen Niederschlagsmenge ist", kleinsteNiederschlagsmenge)

input()