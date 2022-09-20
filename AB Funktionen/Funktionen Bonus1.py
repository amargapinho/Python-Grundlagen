import math

def KanteBerechnen(laengeGrundflaechediagonale):
    kante = laengeGrundflaechediagonale / math.sqrt(2)
    return kante

def PyramideOberflaeche(laengeGrundflaechediagonale, hoehe):
    kante = KanteBerechnen(laengeGrundflaechediagonale)
    hoeheKante = math.sqrt(hoehe^2 + (kante/2)^2)
    oberflaeche = kante^2 + 2*kante*hoeheKante

    return oberflaeche
    

def PyramideVolumen(laengeGrundflaechediagonale, hoehe):
    kante = KanteBerechnen(laengeGrundflaechediagonale)
    volumen = 1/3*kante^2*hoehe

    return volumen
