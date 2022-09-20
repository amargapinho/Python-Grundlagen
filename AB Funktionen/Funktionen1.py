def wuerfelOberflaeche(kantenlaenge):
    ergebnis = kantenlaenge * kantenlaenge * 6
    return ergebnis

def wuerfelVolumen(kantenlaenge):
    ergebnis = kantenlaenge * kantenlaenge * kantenlaenge
    return ergebnis

def quaderOberflaeche(laenge, hohe, breite):
    ergebnis = laenge * hohe * 2 + hohe * breite * 2 + laenge * breite * 2
    return ergebnis

def quaderVolumen(laenge, hohe, breite):
    ergebnis = laenge * hohe * breite
    return ergebnis 

def kugelOberflaeche(radius):
    ergebnis = 4 * 3.14 * radius^2 
    return ergebnis

def kugelVolumen(radius):
    ergebnis = 4 / 3 * 3.14 * radius^3
    return ergebnis

def kegelOberflaeche(radius, hoehe):
    ergebnis = 3.14 * radius^2 + 3.14 * radius * hoehe
    return ergebnis

def kegelVolumen(radius, hoehe):
    ergebnis = 1 / 3 * 3.14 * radius^2 * hoehe
    return ergebnis

def zylinderOberflaeche(radius, hoehe):
    ergebnis = 2 * 3.14 * radius^2 + 2 * 3.14 * radius * hoehe 
    return ergebnis 

def zylinderVolumen(radius, hoehe):
    ergebnis = 3.14 * radius^2 * hoehe 
    return ergebnis