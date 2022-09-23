# a 
def a1():
    
    meineListe = []
    
    for zahl in range(10, 100):
        rest = zahl % 2
        if(rest == 0):
            meineListe.append(zahl)
    
    return meineListe

def a2():
    return range(10, 100, 2)

def a3():
    
    return [zahl for zahl in range(10, 100) if zahl%2 == 0]

#b 
def b1(): 
    
    meineListe = []
    
    for zahl in range(-50, 50):
        rest2 = zahl % 2
        rest3 = zahl % 3
        if(rest2 == 0 and rest3 == 0):
            meineListe.append(zahl)
    
    return meineListe

def b2():
    return [zahl for zahl in range(-50,50) if zahl%2 == 0 and zahl%3 == 0]

print(b2())

#c 

def c1():
    
    meineListe = []
    
    for zahl in range(-9, 9):
        quadrat = zahl * zahl
        meineListe.append(quadrat)
        
    return meineListe

def c2():
    return [zahl*zahl for zahl in range (-9,10)]


#d
def d1():
    
    meineListe = []
    
    for zahl in range(-5, 5):
        wert = 2*zahl**2-4*zahl+6
        meineListe.append(wert)
        
    return meineListe

def d2():
    return [2*zahl**2-4*zahl+6 for zahl in range(-5,5)]



        
