#AUFGABE 3

# Stellt euch vor Ihr arbeitet in einem Unternehmen, welches
# einfache Python-Anwendungen zur Verwaltung von Produkten und Kundenbestellungen entwickelt hat.

# a) Im folgenden Code für die Verwaltung von Produkten haben sich Fehler eingeschlichen.
# Verbessere den Code
 
def Get_Product_Input():
    name = input("Enter product name (or 'stop' to finish): ")
    if name.lower() == 'stop':
        return None
    P = float(input("Enter product price: "))
    Q = int(input("Enter product quantity: "))
    return {'name': name, 'price': P, 'quantity': Q}

def displayproduct(pr):
    print("Prdct:" + pr['name'] + ",price:" + str(pr['price']) + ", Quantity:" + str(pr['quantity']))

def main():
    products = []
    while True:
        product = Get_Product_input()
        if product == None:
            break
        products.append(product)
    for p in products:
        DisplayProduct(p)

if __name__ == "__main__":
    main()

# b) EXKURS: Continous Integration (CI/CD) mit Pylint in GitHub
