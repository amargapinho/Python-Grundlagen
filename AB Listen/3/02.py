#a

meine2DListe = [[0,1,2,3], [1,2,3,4], [2,3,4,5], [3,4,5,6]]


#b

def b1():
    meineListe = []
    for array in range(4):
        
        row = []
        
        for element in range(array, array + 4):
            row.append(element)
            
        meineListe.append(row)
        
    return meineListe


#c

def c1():
    neueListe = [ [array for array in range(element, element + 4)] for element in range(4)]
    return neueListe


#d

def d1():
    return [ [array, array +1, array +2, array +3] for array in range(4)]


