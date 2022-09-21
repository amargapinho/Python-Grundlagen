zahl1 = int(input("Zahl 1:"))
zahl2 = int(input("Zahl 2:"))

operator = input("Operator:")

if(operator == "+"):
    print(zahl1, "+", zahl2, "=", zahl1 + zahl2)
    
elif(operator == "-"):
    print(zahl1, "-", zahl2, "=", zahl1 - zahl2)
    
elif(operator == "*"):
    print(zahl1, "*", zahl2, "=", zahl1 * zahl2)
    
elif(operator == "/"):
    print(zahl1, "/", zahl2, "=", zahl1 / zahl2)

else:
    print("Error.")

input()