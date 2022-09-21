zahl1 = int(input("Zahl 1:"))
zahl2 = int(input("Zahl 2:"))
zahl3 = int(input("Zahl 3:"))
zahl4 = int(input("Zahl 4:"))

if(zahl1 < zahl2 and zahl1 < zahl3 and zahl1 < zahl4):
    print("Zahl 1:", zahl1)

elif(zahl2 < zahl1 and zahl2 < zahl3 and zahl2 < zahl4):
    print("Zahl 2:", zahl2)

elif(zahl3 < zahl1 and zahl3 < zahl2 and zahl3 < zahl4):
    print("Zahl 3", zahl3)

else:
    print("Zahl 4:", zahl4)

input()