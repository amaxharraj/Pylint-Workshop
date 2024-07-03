#AUFGABE 1

# a) Versuche folgenden Code zu verbessern
# TIPP: pylint --help
'''Modul'''
def calc(r):
    '''Funktion'''
    p=3.14159
    a=p*r**2
    return a


rad=5
AREA=calc(rad)
print("Area", AREA)
