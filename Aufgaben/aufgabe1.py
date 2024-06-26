#AUFGABE 1

# a) Versuche folgenden Code zu verbessern
# TIPP: pylint --help

def calc(r):
    p=3.14159
    a=p*r**2
    return a


rad=5
area=calc(rad)
print("Area", area)