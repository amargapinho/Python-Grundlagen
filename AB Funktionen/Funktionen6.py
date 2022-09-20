import math

def BerechneFallgeschwindigkeit(sekunden):
    fallgeschwindigkeit = 9.81
    for _ in range(sekunden):
        fallgeschwindigkeit = fallgeschwindigkeit * 2
    
    return fallgeschwindigkeit


def BerechneFallstrecke(sekunden):
    fallstrecke = 0
    for i in range(sekunden):
        fallstrecke = fallstrecke + BerechneFallgeschwindigkeit(i)
    
    return fallstrecke
    