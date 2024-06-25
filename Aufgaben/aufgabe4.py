#AUFGABE 4

# Das Unternehmen hat ebenfalls Python-Skripte
# zur Verwaltung von Kundenbestellungen

# a) Verbessert den folgenden Code:

# Beispielcode für Pylint-Workshop: Kundenbestellungen verwalten

class Order:
    def __init__(self, customer_name, order_date, products):
        self.customer_name = customer_name
        self.order_date = order_date
        self.products = products
    
    def Calculate_total_price(self):
        total_price = 0
        for product in self.products:
            total_price += product['price'] * product['quantity']
        return total_price
    
    def Print_order_details(self):
        print("Order Details:")
        print(f"Customer: {self.customer_name}")
        print(f"Date: {self.order_date}")
        print("Products:")
        for product in self.products:
            print(f"- {product['name']}: ${product['price']} x {product['quantity']}")

def main():
    products = [
        {'name': 'Product A', 'price': 10, 'quantity': 2},
        {'name': 'Product B', 'price': 20, 'quantity': 1},
        {'name': 'Product C', 'price': 15, 'quantity': 3},
    ]
    order = Order("John Doe", "2023-06-24", products)
    order.Calculate_total_price()
    order.Print_order_details()

if __name__ == "__main__":
    main()

