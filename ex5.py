# Product Class
class Product:
    def __init__(self, name, price, quantity=1):
        # Initialize the product with a name, price, and quantity
        self.name = name  # The name of the product (e.g., "Apple")
        self.price = price  # The price of a single unit of the product (e.g., 1.50)
        self.quantity = quantity  # The quantity of the product being bought (default is 1)

    def __str__(self):
        # Return a string representation of the product in the format:
        # "Product Name - $Price x Quantity"
        return f"{self.name} - ${self.price} x {self.quantity}"

# ShoppingCart Class
class ShoppingCart:
    def __init__(self):
        # Initialize an empty shopping cart to hold products
        self.products = []  # List to store the products added to the cart

    def add_product(self, product):
        # Add a product to the shopping cart
        self.products.append(product)  # Append the product to the products list
        print(f"Added {product.name} to the cart.")  # Print confirmation message

    def remove_product(self, product_name):
        # Remove a product from the shopping cart based on its name
        for product in self.products:
            # Compare product names in a case-insensitive manner
            if product.name.lower() == product_name.lower():
                self.products.remove(product)  # Remove the product from the list
                print(f"Removed {product_name} from the cart.")  # Print confirmation message
                return True  # Return True to indicate that the product was removed
        # If product was not found in the cart
        print(f"Product {product_name} not found in the cart.")  # Print an error message
        return False  # Return False to indicate that the product was not found

    def total_price(self):
        # Calculate the total price of all products in the cart
        total = 0  # Initialize total price to 0
        for product in self.products:
            # Add the price of each product multiplied by its quantity to the total
            total += product.price * product.quantity
        return total  # Return the total price

    def display_cart(self):
        # Display all the products currently in the shopping cart
        if not self.products:  # If the cart is empty
            print("Your shopping cart is empty.")  # Notify the user
            return  # Exit the method as there is nothing to display
        print("Shopping Cart:")  # Print header for the cart
        for product in self.products:
            # Display each product in the cart using the __str__ method of the Product class
            print(f"- {product}")  # Print product in the format "Product Name - $Price x Quantity"

# Testing the shopping cart application
if __name__ == "__main__":
    # Create several product instances with specific names, prices, and quantities
    product1 = Product("Apple", 1.50, 3)  # 3 apples, each costing $1.50
    product2 = Product("Banana", 0.80, 5)  # 5 bananas, each costing $0.80
    product3 = Product("Orange", 2.00, 2)  # 2 oranges, each costing $2.00
    product4 = Product("Milk", 1.20, 1)  # 1 milk carton, costing $1.20

    # Create an instance of ShoppingCart
    cart = ShoppingCart()

    # Add products to the shopping cart
    cart.add_product(product1)  # Add apples to the cart
    cart.add_product(product2)  # Add bananas to the cart
    cart.add_product(product3)  # Add oranges to the cart

    # Display the contents of the cart and the total price
    cart.display_cart()  # Display all the products in the cart
    print(f"Total Price: ${cart.total_price():.2f}")  # Calculate and display the total price

    # Remove a product from the cart (e.g., "Banana")
    cart.remove_product("Banana")  # Try to remove bananas from the cart

    # Display the cart contents and total price after removal
    cart.display_cart()  # Display remaining products after removing bananas
    print(f"Total Price: ${cart.total_price():.2f}")  # Display the updated total price

    # Add another product (Milk) to the cart
    cart.add_product(product4)  # Add milk to the cart

    # Display the final cart contents and total price
    cart.display_cart()  # Display all products in the cart
    print(f"Total Price: ${cart.total_price():.2f}")  # Display the final total price
