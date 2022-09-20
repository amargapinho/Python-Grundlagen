import math

def BerechneA(volumen):
    a = volumen**(1/3)

    return a

def BerechneWuerfeloberflaeche(a):
    oberflaeche = (a*a) * 6 

    return oberflaeche

def Loesung(volumen):
    oberflaeche = BerechneWuerfeloberflaeche(BerechneA(volumen))
    
    return oberflaeche