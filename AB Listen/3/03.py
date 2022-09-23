#a

def algorithmik1():
    badmintonturnier = [] 
    for spieler1 in range(1,5):
        for spieler2 in range(spieler1+1, 6):
            badmintonturnier.append([spieler1, spieler2])
            
    return badmintonturnier


#b

def algorithmik2(spielerzahl):
    badmintonturnier = [] 
    for spieler in range(spielerzahl ** 2):
        spieler1 = spieler // spielerzahl
        spieler2 = spieler % spielerzahl 
        if spieler1 > spieler2:
            badmintonturnier.append([spieler1, spieler2])
            
    return badmintonturnier

print(algorithmik2(5))