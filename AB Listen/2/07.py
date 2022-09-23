zahlenliste = [5, 2, 9, 13, 16, 27, 1, 67, 12, 56]

def entferneGeradeZahlen (liste):
    
    for zahl in liste:
        ergebnis = zahl / 2
        ganzeZahl = int(ergebnis)
        
        if(ganzeZahl == ergebnis):
            liste.remove(zahl)
            
    return liste


def entferneGeradeZahlen (liste):
    for zahl in liste:
        ergebnis = zahl % 2
        
        if ergebnis == 0:
            liste.remove(zahl)
            
    return liste
        