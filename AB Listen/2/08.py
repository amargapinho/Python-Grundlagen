
zahlenliste = [5, 2, 9, -13, 16, -27, 1, -67, 12, 56]

def sindAlleZahlenPositiv (liste):
    flag = True
    for zahl in liste:
        if(zahl<0):
            flag = False
            
    return flag


def sindAlleZahlenPositiv1 (liste):
    for zahl in liste:
        if(zahl<0):
           return False
            
    return True

print(sindAlleZahlenPositiv(zahlenliste))
print(sindAlleZahlenPositiv1(zahlenliste))