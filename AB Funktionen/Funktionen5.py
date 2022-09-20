import math

def BerechneKugelRadius(volumen):
    radius = (math.sqrt((3*volumen) / (4*3.14))) ^(1/3)
    return radius