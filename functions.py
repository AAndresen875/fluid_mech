import math
#more info to fill out later; https://en.wikipedia.org/wiki/Hagen%E2%80%93Poiseuille_equation
def poiseuille(length, radius, viscosity):
    a = 8*length*viscosity
    b = math.pi*(radius)**4
    c = a/b
    return(c)