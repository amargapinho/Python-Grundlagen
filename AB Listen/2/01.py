zahlenliste = [5, 2, 9, 13, 16, 27, 1, 67, 12, 56]

def multipliziereAlleZahlenInListe (liste):
    zwischenprodukt = 1
    
    for zahl in liste:
        zwischenprodukt = zwischenprodukt * zahl
    return zwischenprodukt

print(multipliziereAlleZahlenInListe(zahlenliste))