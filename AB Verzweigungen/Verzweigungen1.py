zahl1 = int(input("Zahl 1:"))
zahl2 = int(input("Zahl 2:"))

if(zahl1 != 0 and zahl2 != 0):
    if(zahl1 > zahl2):
        ergebnis = zahl1 / zahl2

    else:
        ergebnis = zahl2 / zahl1

    print(ergebnis)

else:
    print("Zahl darf nicht 0 sein!")

input()
