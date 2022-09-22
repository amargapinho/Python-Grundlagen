eingabe = input("bitte geben sie ein Zahl ein")
zahl = int(eingabe)

summe = 0

for i in range(2, zahl+1, 2):
    summe = i+summe

print(summe)