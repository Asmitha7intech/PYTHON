# Initialize the back and forward stacks
back_stack = []
forward_stack = []
current_page = None

def visit(url):
    global current_page
    if current_page:
        back_stack.append(current_page)
    forward_stack.clear()  # Clear forward stack when a new page is visited
    current_page = url
    print(f"Visiting: {url}")

def back():
    global current_page
    if not back_stack:
        print("No more pages to go back to.")
    else:
        forward_stack.append(current_page)
        current_page = back_stack.pop()
        print(f"Going back to: {current_page}")

def forward():
    global current_page
    if not forward_stack:
        print("No more pages to go forward to.")
    else:
        back_stack.append(current_page)
        current_page = forward_stack.pop()
        print(f"Going forward to: {current_page}")

def current():
    if current_page:
        print(f"Current page: {current_page}")
    else:
        print("No page visited yet.")

def main():
    while True:
        print("\nBrowser History Management System")
        print("1. Visit a page")
        print("2. Go back to the previous page")
        print("3. Go forward to the next page")
        print("4. Show current page")
        print("5. Exit")
        
        choice = input("Enter your choice: ")

        if choice == '1':
            url = input("Enter the URL to visit: ")
            visit(url)
        elif choice == '2':
            back()
        elif choice == '3':
            forward()
        elif choice == '4':
            current()
        elif choice == '5':
            print("Exiting the browser history management system.")
            break
        else:
            print("Invalid choice. Please try again.")

# Run the program
main()

