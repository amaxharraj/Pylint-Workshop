#AUFGABE 4

# Stellt euch vor Ihr arbeitet in einem Unternehmen, welches
# einfache Python-Anwendungen zur Verwaltung von Produkten und Kundenbestellungen entwickelt hat.

# a) Verbessert den folgenden Code:

class Order:
    def __init__(self, Customer_Name, Order_Date, Product):
        self.customer_name = Customer_Name
        self.order_date = Order_Date
        self.products = Product

    def Calculate_Total_Price(self):
        total_price = 0
        for product in self.products:
            total_price += product['preis'] * product['anzahl']
        return total_price

    def Print_Order_Details(self):
        print("Order Details:")
        print(f"Customer: {self.customer_name}")
        print(f"Date: {self.order_date}")
        print("Products:")
        for product in self.products:
            print(f"- {product['name']}: ${product['price']} x {product['quantity']}")

def main():
    product = [
        {'name': 'Product A', 'price': 10, 'quantity': 2},
        {'name': 'Product B', 'price': 20, 'quantity': 1},
        {'name': 'Product C', 'price': 15, 'quantity': 3},
    ]
    order = Order("Max Mustermann", "2023-06-27", product)
    order.Calculate_Total_Price()
    order.Print_Order_Details()

if __name__ == "__main__":
    main()
