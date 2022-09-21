jahreszahl = int(input("Jahreszahl:"))

if(jahreszahl % 4 == 0):
    if(jahreszahl % 100 == 0):
        if(jahreszahl % 400):
            print("Das Jahr ist ein Schaltjahr.")
        else:
            print("Das Jahr ist kein Schaltjahr.")
    else:
        print("Das Jahr ist ein Schaltjahr.")
else:
    print("Das Jahr ist kein Schaltjahr.")