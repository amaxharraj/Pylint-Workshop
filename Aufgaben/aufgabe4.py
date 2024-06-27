#AUFGABE 3


# a) Im folgenden Code für die Verwaltung von Produkten haben sich einige Fehler eingeschlichen.
#    Verbessere den Code.
 
def Get_Product_Input():
    name = input("Produktname(oder 'stop' zum Beenden): ")
    if name.lower() == 'stop':
        return None
    P = float(input("Produktpreis: "))
    A = int(input("Produktanzahl: "))
    return {'name': name, 'preis': P, 'anzahl': A}

def displayproduct(pr):
    print("Produkt:" + pr['name'] + ",Preis:" + (pr['preis']) + ", Anzahl:" + str(pr['anzahl']))

def main():
    products = []
    while True:
        Product = Get_Product_input()
        if product == None:
            break
        products.append(Product)
    for p in products:
        DisplayProduct(p)

if __name__ == "__main__":
    main()





