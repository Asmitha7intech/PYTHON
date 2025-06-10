# List to hold voters' information
voters = []

# Function to register a new voter
def register_voter():
    voter_id = input("Enter Voter ID: ")
    name = input("Enter Voter Name: ")
    age = input("Enter Voter Age: ")
    address = input("Enter Voter Address: ")
    
    voter = {
        "id": voter_id,
        "name": name,
        "age": age,
        "address": address
    }
    
    voters.append(voter)
    print(f"Voter {name} registered successfully.")

# Function to update voter information
def update_voter():
    voter_id = input("Enter Voter ID to update: ")
    
    for voter in voters:
        if voter["id"] == voter_id:
            print(f"Found Voter {voter['name']}.")
            voter["name"] = input(f"Enter new name (Current: {voter['name']}): ")
            voter["age"] = input(f"Enter new age (Current: {voter['age']}): ")
            voter["address"] = input(f"Enter new address (Current: {voter['address']}): ")
            print(f"Voter {voter['name']} updated successfully.")
            return
    
    print("Voter ID not found!")

# Function to delete a voter
def delete_voter():
    voter_id = input("Enter Voter ID to delete: ")
    
    for voter in voters:
        if voter["id"] == voter_id:
            voters.remove(voter)
            print(f"Voter {voter['name']} deleted successfully.")
            return
    
    print("Voter ID not found!")

# Function to list all voters
def list_all_voters():
    if not voters:
        print("No voters registered yet.")
        return
    
    print("\nList of all registered voters:")
    for voter in voters:
        print(f"ID: {voter['id']}, Name: {voter['name']}, Age: {voter['age']}, Address: {voter['address']}")

# Function to search for a voter by ID or name
def search_voter():
    search_type = input("Search by ID or Name? (Enter 'id' or 'name'): ").lower()
    if search_type == 'id':
        voter_id = input("Enter Voter ID: ")
        for voter in voters:
            if voter["id"] == voter_id:
                print(f"Voter found: ID: {voter['id']}, Name: {voter['name']}, Age: {voter['age']}, Address: {voter['address']}")
                return
        print("Voter ID not found!")
    elif search_type == 'name':
        name = input("Enter Voter Name: ")
        for voter in voters:
            if voter["name"].lower() == name.lower():
                print(f"Voter found: ID: {voter['id']}, Name: {voter['name']}, Age: {voter['age']}, Address: {voter['address']}")
                return
        print("Voter Name not found!")
    else:
        print("Invalid search option. Please enter 'id' or 'name'.")

# Main function to interact with the user
def main():
    while True:
        print("\nVoter Management System (VMS)")
        print("1. Register Voter")
        print("2. Update Voter Information")
        print("3. Delete Voter")
        print("4. List All Voters")
        print("5. Search Voter")
        print("6. Exit")
        
        choice = input("Enter your choice: ")

        if choice == '1':
            register_voter()
        elif choice == '2':
            update_voter()
        elif choice == '3':
            delete_voter()
        elif choice == '4':
            list_all_voters()
        elif choice == '5':
            search_voter()
        elif choice == '6':
            print("Exiting Voter Management System.")
            break
        else:
            print("Invalid choice. Please try again.")

# Run the program
main()
