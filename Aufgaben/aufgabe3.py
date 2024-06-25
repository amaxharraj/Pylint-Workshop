#AUFGABE 3

# Stellt euch vor Ihr arbeitet in einem Unternehmen, welches
# einfache Python-Anwendungen zur Verwaltung von Produkten und Kundenbestellungen entwickelt hat.

# a) Verbessert folgenden Code für die Verwaltung von Produkten

def Get_Product_input():
    name = input("Enter product name (or 'stop' to finish): ")
    if name.lower() == 'stop':
        return None
    P = float(input("Enter product price: "))
    Q = int(input("Enter product quantity: "))
    return {'name': name, 'price': P, 'quantity': Q}

def DisplayProduct(pr):
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
