zahl1 = int(input("Zahl 1:"))
zahl2 = int(input("Zahl 2:"))
zahl3 = int(input("Zahl 3:"))

if(zahl1 < zahl2 and zahl1 < zahl3):
    print(zahl1)
    
    if(zahl2 < zahl3):
        print(zahl2, zahl3)

    else:
        print(zahl3, zahl2)

elif(zahl2 < zahl1 and zahl2 < zahl3):
    print(zahl2)

    if(zahl1 < zahl3):
       print(zahl1, zahl3)

    else:
        print(zahl3, zahl1)

elif(zahl3 < zahl1 and zahl3 < zahl2):
    print(zahl3)

    if(zahl1 < zahl2):
        print(zahl1, zahl2)

    else:
        print(zahl2, zahl1)

input()