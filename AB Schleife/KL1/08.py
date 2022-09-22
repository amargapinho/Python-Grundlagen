eingabe = input("bitte geben sie ein Zahl ein")
zahl = int(eingabe)

fakultät = 1

for i in range(1, zahl+1):
    fakultät = i*fakultät
    
print(fakultät)