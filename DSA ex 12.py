class ECommerceProductManagement:
    def __init__(self):
        # List to store products as dictionaries
        self.products = []

    def add_product(self):
        # Get new product details from the user
        print("Enter new product details:")
        try:
            product_id = int(input("Enter product ID: "))
            name = input("Enter product name: ")
            price = float(input("Enter product price: $"))
            stock = int(input("Enter stock quantity: "))

            # Create a product dictionary
            new_product = {"product_id": product_id, "name": name, "price": price, "stock": stock}

            # Add the product to the list
            self.products.append(new_product)
            print(f"Product '{name}' added successfully.\n")
        except ValueError:
            print("Invalid input. Please enter valid values.")

    def display_products(self):
        # Iterating through the list of products to display all product details
        if not self.products:
            print("No products available.\n")
            return
        for index, product in enumerate(self.products):
            print(f"Product {index + 1}: {product['name']} (ID: {product['product_id']})")
            print(f"  Price: ${product['price']} | Stock: {product['stock']} units\n")

    def update_product(self):
        # Get the index of the product to update
        self.display_products()
        try:
            product_index = int(input(f"Enter the product number to update (1 to {len(self.products)}): ")) - 1
            if 0 <= product_index < len(self.products):
                print("Enter new details for the product:")
                new_name = input(f"Enter new name (current: {self.products[product_index]['name']}): ")
                new_price = float(input(f"Enter new price (current: ${self.products[product_index]['price']}): "))
                new_stock = int(input(f"Enter new stock quantity (current: {self.products[product_index]['stock']}): "))

                # Update the product details
                self.products[product_index]['name'] = new_name
                self.products[product_index]['price'] = new_price
                self.products[product_index]['stock'] = new_stock

                print(f"Product {self.products[product_index]['product_id']} updated successfully.\n")
            else:
                print("Invalid product number.\n")
        except ValueError:
            print("Invalid input. Please enter valid values.\n")

    def remove_product(self):
        # Get the index of the product to remove
        self.display_products()
        try:
            product_index = int(input(f"Enter the product number to remove (1 to {len(self.products)}): ")) - 1
            if 0 <= product_index < len(self.products):
                removed_product = self.products.pop(product_index)
                print(f"Product {removed_product['name']} (ID: {removed_product['product_id']}) removed successfully.\n")
            else:
                print("Invalid product number.\n")
        except ValueError:
            print("Invalid input. Please enter a valid product number.\n")

    def highlight_products(self):
        # Use slicing to highlight a range of products
        try:
            start = int(input(f"Enter the start index for highlighting (1 to {len(self.products)}): ")) - 1
            end = int(input(f"Enter the end index for highlighting (1 to {len(self.products)}): ")) - 1

            if 0 <= start <= end < len(self.products):
                highlighted_products = self.products[start:end + 1]
                print("\nHighlighted Products for Marketing:")
                for product in highlighted_products:
                    print(f"- {product['name']} (ID: {product['product_id']})")
                    print(f"  Price: ${product['price']} | Stock: {product['stock']} units\n")
            else:
                print("Invalid range. Please enter a valid range.\n")
        except ValueError:
            print("Invalid input. Please enter valid indices.\n")

# Example usage
def main():
    ecommerce_system = ECommerceProductManagement()

    while True:
        print("\n--- E-Commerce Product Management ---")
        print("1. Display All Products")
        print("2. Add New Product")
        print("3. Update Product")
        print("4. Remove Product")
        print("5. Highlight Products for Marketing")
        print("6. Exit")

        try:
            choice = int(input("Enter your choice: "))

            if choice == 1:
                ecommerce_system.display_products()
            elif choice == 2:
                ecommerce_system.add_product()
            elif choice == 3:
                ecommerce_system.update_product()
            elif choice == 4:
                ecommerce_system.remove_product()
            elif choice == 5:
                ecommerce_system.highlight_products()
            elif choice == 6:
                print("Exiting the system.")
                break
            else:
                print("Invalid choice! Please select a valid option.\n")
        except ValueError:
            print("Invalid input. Please enter a valid choice.\n")

if __name__ == "__main__":
    main()
