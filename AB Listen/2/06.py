zahlenliste = [5, 2, 9, 13, 16, 27, 1, 67, 12, 56]

def zaehleZweistelligeZahlen(liste):
    count = 0
    
    for zahl in liste:
        if(zahl <= 99 and zahl >= 10):
            count = count + 1
            
    return count

print(zaehleZweistelligeZahlen(zahlenliste))