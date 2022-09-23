zahlenliste = [5, 2, 9, 13, 16, 27, 1, 67, 12, 56]

def istListeLeer (liste):
    listeLaenge = len(liste)
    
    return listeLaenge == 0


print(istListeLeer(zahlenliste))