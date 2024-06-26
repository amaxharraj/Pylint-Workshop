#AUFGABE 4

# Das Unternehmen hat ebenfalls Python-Skripte
# zur Verwaltung von Kundenbestellungen

# a) Verbessert den folgenden Code:

# Beispielcode für Pylint-Workshop: Kundenbestellungen verwalten
'''Verwaltung von Kundenbestellungen'''
class Order:
    '''Klasse zu Kundenbestellungen'''
    def __init__(self, customer_name, order_date, products):
        self.customer_name = customer_name
        self.order_date = order_date
        self.products = products

    def calculate_total_price(self):
        '''Preisberechnung'''
        total_price = 0
        for product in self.products:
            total_price += product['price'] * product['quantity']
        return total_price

    def print_order_details(self):
        '''Verarbeitung der Bestellungsdetails'''
        print("Order Details:")
        print(f"Customer: {self.customer_name}")
        print(f"Date: {self.order_date}")
        print("Products:")
        for product in self.products:
            print(f"- {product['name']}: ${product['price']} x {product['quantity']}")

def main():
    '''Funktion zur Anwendung'''
    product = [
        {'name': 'Product A', 'price': 10, 'quantity': 2},
        {'name': 'Product B', 'price': 20, 'quantity': 1},
        {'name': 'Product C', 'price': 15, 'quantity': 3},
    ]
    order = Order("Max Mustermann", "2023-06-27", product)
    order.calculate_total_price()
    order.print_order_details()

if __name__ == "__main__":
    main()
